import src.folders_remote as folders
#import src.folders_local as folders
from datetime import datetime
import whisper
import torch
import json
import time
import os


dir_audios = folders.soap_prepped                                # folder of prepped audios
dir_tscripts = os.path.join(folders.exports, 'SOAP', 'tscripts') # folder for tscripts 
dir_audit = os.path.join(folders.exports, 'SOAP')                # folder for tscripts audit 

### Setup
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f'Using device: {device}')
model = whisper.load_model('medium.en', download_root=folders.models, device=device)
model = model.to(device)

### Setup audit file
# Add date to audit filename in format YYYYMMDD-HHMM (dynamic)
current_time_str = datetime.now().strftime("%Y%m%d-%H%M")
fname_audit = f'tscripts_audit_{current_time_str}.txt'
audit = open(os.path.join(dir_audit, fname_audit), "w")

### Main transcribe loop
fnames = [fname for fname in os.listdir(dir_audios) if fname.endswith('.mp3')]
for idx, fname in enumerate(fnames):

    fname_out = f'tscript_{fname}.json'
    fpath_out = os.path.join(dir_tscripts, fname_out )

    if os.path.isfile(fpath_out):
        print(f'Already processed: {fname_out} ({idx+1}/{len(fnames)})')
        continue

    start_time = time.time()
    result = model.transcribe(os.path.join(dir_audios, fname))
    end_time = time.time()
    elapsed_time = float(f'{round((end_time-start_time)/60, 2)}')
    print(f'Finished: {fname_out} ({idx+1}/{len(fnames)}; took {elapsed_time} mins)')

    # Write first 250 chars to audit file
    newline = f'{fname}\nElapsed time: {elapsed_time}mins\nStart:{result['text'][0:250]}\n\n'
    audit.writelines(newline)

    # Save tscript
    with open(fpath_out, 'w') as json_file:
        json.dump(result, json_file, indent=4)

audit.close()