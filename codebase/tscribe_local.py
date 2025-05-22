import src.folders_local as folders
import whisper
import torch
import json
import time
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f'Using device: {device}')
tscribe_overview = open(os.path.join(folders.exports, 'tscribe_overview.txt'), "w")

audio_dir_path = folders.soap_prepped
fnames = [fname for fname in os.listdir(audio_dir_path) if fname.endswith('.mp3')]

model = whisper.load_model('medium.en', download_root=folders.models, device=device)
model = model.to(device)

for idx, fname in enumerate(fnames):

    fpath_out = os.path.join(folders.exports, f'tscript_{fname[:-4].lower()}.json')
    if os.path.exists(fpath_out):
        print(f'Already processed: {fname} ({idx+1}/{len(fnames)})')
        continue

    print(f'Processing {fname} ({idx+1}/{len(fnames)})')

    start_time = time.time()
    result = model.transcribe(os.path.join(audio_dir_path, fname))
    end_time = time.time()
    elapsed_time = float(f'{round((end_time-start_time)/60, 2)}')

    with open(fpath_out, 'w') as json_file:
        json.dump(result, json_file, indent=4)

    newline = f'{fname}\nElapsed time: {elapsed_time}mins\nStart:{result['text'][0:250]}\n\n'
    tscribe_overview.writelines(newline)
    print(newline)

tscribe_overview.close()