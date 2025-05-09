import src.folders_remote as folders
import src.tokens as tokens
from pyannote.audio import Pipeline
import pandas as pd
import torch
import json
import os

### convenience functions
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

### setup audio batch
dir_audios = folders.audio_mp3
fnames = [fname for fname in os.listdir(dir_audios) if fname.endswith('.mp3')]

### pyannote setup
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token=tokens.auth_token_hg)
pipeline = pipeline.to(torch.device("cuda"))

for idx, fname in enumerate(fnames):
    if idx!=0:
        continue

    diarization = pipeline(os.path.join(dir_audios, fname), hook=hook)
    df = diarization2df(diarization)
    df.to_csv(os.path.join(folders.exports, f'diar_{fname[:-4].lower()}.csv'))
