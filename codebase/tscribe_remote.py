import src.folders_remote as folders
import whisper
import torch
import json
import time
import os

fnames = [fname for fname in os.listdir(folders.pdp1_audios) if fname.endswith('.mp3')]

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f'Using device: {device}')
model = whisper.load_model('medium.en', download_root=folders.models, device=device)
model = model.to(device)

tscribe_overview = open(os.path.join(folders.exports, 'tscribe_overview.txt'), "w")

for idx, fname in enumerate(fnames):

    print(f'Processing {fname} ({idx+1}/{len(fnames)})')

    fpath_out = os.path.join(folders.exports_tscripts, f'tscript_{fname.lower()}.json')
    if os.path.exists(fpath_out):
        continue

    start_time = time.time()
    result = model.transcribe(os.path.join(folders.pdp1_audios, fname))
    end_time = time.time()
    elapsed_time = float(f'{round((end_time-start_time)/60, 2)}')

    with open(fpath_out, 'w') as json_file:
        json.dump(result, json_file, indent=4)

    newline = f'{fname}\nElapsed time: {elapsed_time}mins\nStart:{result['text'][0:250]}\n\n'
    tscribe_overview.writelines(newline)
    print(newline)

tscribe_overview.close()
