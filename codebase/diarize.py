import src.folders_local as folders
import src.tokens as tokens
from pyannote.audio import Pipeline
from pyannote.audio.pipelines.utils.hook import ProgressHook
import pandas as pd
import warnings
import torch
import time
import os


dir_audios = folders.soap_prepped  # folder for prepped audio files
dir_diars = os.path.join(folders.exports, 'SOAP', 'diars') # folder where diarization output will be placed

### Setup
warnings.filterwarnings("ignore", category=UserWarning) # Suppress all UserWarnings
print(f'Is CUDA available: {torch.cuda.is_available()}.')
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=tokens.auth_token_hg)
pipeline = pipeline.to(torch.device("cuda"))

### Convenience function
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

### Main diarization loop
fnames = [fname for fname in os.listdir(dir_audios) if fname.endswith('.mp3')]
for idx, fname in enumerate(fnames):

    fname_out = f'diar_{fname[:-4]}.csv'
    fpath_out = os.path.join(dir_diars, fname_out)

    if os.path.isfile(fpath_out):
        print(f'Already processed: {fname_out} ({idx+1}/{len(fnames)})')
        continue

    start_time = time.time()
    with ProgressHook() as hook:
        diarization = pipeline(os.path.join(dir_audios, fname), hook=hook)
    end_time = time.time()
    elapsed_time = float(f'{round((end_time-start_time)/60, 1)}')
    print(f'Finished: {fname_out} ({idx+1}/{len(fnames)}; took {elapsed_time} mins)')

    df = diarization2df(diarization)
    df.to_csv(fpath_out)