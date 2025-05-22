#from pyannote.audio.pipelines.utils.hook import ProgressHook
from concurrent.futures import ProcessPoolExecutor
from pyannote.audio import Pipeline
import src.folders_local as folders
import src.tokens as tokens
import pandas as pd
import warnings
import torch
import time
import os

warnings.filterwarnings("ignore", category=UserWarning) # Suppress all UserWarnings
print(f'Is CUDA available: {torch.cuda.is_available()}.')

### setup audio batch
dir_audios = folders.pdp1_audios
fnames = [fname for fname in os.listdir(dir_audios) if fname.endswith('.mp3')]

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=tokens.auth_token_hg)
pipeline = pipeline.to(torch.device("cuda"))

def main():
    # Number of parallel workers (adjust as needed)
    max_workers = 3
    files_with_index = list(enumerate(fnames))
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        list(executor.map(process_file, files_with_index))

def process_file(args):
    idx, fname = args

    output_fpath = os.path.join(folders.exports_diars, f'diar_{fname[:-4].lower()}.csv')
    if os.path.isfile(output_fpath):
        print(f'Already finished: {fname} ({idx+1}/{len(fnames)})')
        return

    print(f"Processing: {fname} ({idx+1}/{len(fnames)})")

    start_time = time.time()
    diarization = pipeline(os.path.join(dir_audios, fname))
    end_time = time.time()
    elapsed_time = float(f'{round((end_time-start_time)/60, 1)}')
    print(f'Finished: {fname}; this file took: {elapsed_time} mins. ({idx+1}/{len(fnames)})')

    # Re-import here to avoid issues with multiprocessing
    from diar_local_parallel import diarization2df
    df = diarization2df(diarization)
    df.to_csv(output_fpath)

def diarization2df(diarization):
    '''
        Type: The type of event. Common values include SPEAKER, NON-SPEECH, NOISE, etc. The most common value is SPEAKER.
        File ID: The identifier for the audio file. This is a unique identifier for the recording being annotated.
        Channel ID: The channel number. This is typically 1 for single-channel (mono) recordings.
        Start Time: The start time of the event, in seconds, from the beginning of the audio file.
        Duration: The duration of the event, in seconds.
        Orthography Field: This field is often left blank or used for orthographic transcription (i.e., the actual words spoken).
        Speaker Type: This field typically indicates the type of speaker (e.g., male, female). It can be left blank.
        Speaker Name: The identifier for the speaker (e.g., spk1, spk2). This is used to distinguish between different speakers in the recording.
        Confidence Score: A confidence score for the event, if available. This field is often left blank.
        Slat: This stands for “Speaker Labeled Attribute Type” and is often left blank.
    '''

    columns = ['audio_type','fname','channelID','start','dur','orthography','speakerID','speakerName','confidence','slat']
    data = []
    for line in diarization.to_rttm().splitlines():
        fields = line.strip().split()
        data.append(fields)

    df = pd.DataFrame(data, columns=columns)
    return df

if __name__ == '__main__':
    main()
