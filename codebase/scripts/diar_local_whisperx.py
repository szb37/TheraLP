import src.folders as folders
import whisperx
import gc
import json
import time
import os

import torch
torch.backends.cuda.matmul.allow_tf32 = True
torch.backends.cudnn.allow_tf32 = True

### WhisperX setup
batch_size = 16 # reduce if low on GPU mem
device = 'cuda'
model = whisperx.load_model('large-v2', device, compute_type='float16', download_root='C:\models\whisperX')

dir_audios = folders.audio
fnames = [fname for fname in os.listdir(dir_audios) if fname.endswith('.m4a')]
file_results = open(os.path.join(folders.exports, 'results_summary.txt'), "w")

for idx, fname in enumerate(fnames):

    if idx!=0:
        continue

    start_time = time.time()

    # 1. Transcribe with original whisper (batched)
    audio = whisperx.load_audio(os.path.join(dir_audios, fname))
    result = model.transcribe(audio, batch_size=batch_size)

    # 2. Align whisper output
    model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

    # 3. Assign speaker labels
    diarize_model = whisperx.DiarizationPipeline(use_auth_token=YOUR_HF_TOKEN, device=device)
    diarize_segments = diarize_model(audio)
    # diarize_model(audio, min_speakers=min_speakers, max_speakers=max_speakers)
    result = whisperx.assign_word_speakers(diarize_segments, result)


    end_time = time.time()
    elapsed_time = float(f'{round((end_time-start_time)/60, 2)}')

    with open(os.path.join(folders.exports, f'tscript_{fname[:-4][12:].lower()}.json'), 'w') as json_file:
        json.dump(result, json_file, indent=4)

    newline = f'{fname}\nElapsed time: {elapsed_time}mins\nStart:{result['text'][0:250]}\n\n'
    file_results.writelines(newline)
    print(newline)

file_results.close()



###




# 1. Transcribe with original whisper (batched)

# save model to local path (optional)
# model_dir = "/path/"
# model = whisperx.load_model("large-v2", device, compute_type=compute_type, download_root=model_dir)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"]) # before alignment

# delete model if low on GPU resources
# import gc; gc.collect(); torch.cuda.empty_cache(); del model

# 2. Align whisper output
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

print(result["segments"]) # after alignment

# delete model if low on GPU resources
# import gc; gc.collect(); torch.cuda.empty_cache(); del model_a

# 3. Assign speaker labels
diarize_model = whisperx.DiarizationPipeline(use_auth_token=YOUR_HF_TOKEN, device=device)

# add min/max number of speakers if known
diarize_segments = diarize_model(audio)
# diarize_model(audio, min_speakers=min_speakers, max_speakers=max_speakers)

result = whisperx.assign_word_speakers(diarize_segments, result)
print(diarize_segments)
print(result["segments"]) # segments are now assigned speaker IDs
