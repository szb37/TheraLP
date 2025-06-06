This codebase has been developed to transcribe audio files. 
You need to run the pipeline from the included conda environment (theralp_env.yaml) and have ffmpeg installed (ffmpeg installation is not handeled by conda).
Pipline was developed with ffmpeg version 7.1-essentials_build (from www.gyan.dev).

Here are the steps to run it:
- Put all files to be converted into a folder
- Copy 'prep_audio.sh' into that folder and run it. Its a bash script that executes an ffmpeg command that
    - if the audio starts with a silent period it removes that silent period. Based on experimentation, Whisper makes a lot of mistakes if audio starts with silence, so best to remove prior to transcribing.
    - converts file to mp3. pyannote (which we use for diarization) supports a limited number of audio formats, mp3 is one of them.
- Change src/folders.py so that folders point to the right place in your system
- Run tscribe.py, which uses Whisper to transcribe the audio files; dir_audios should point to the folder where the audios prepocessed by ffmpeg are stored. There are two outputs:
    - The transcription of each audio file, will be saved in dir_tscripts
    - The audit file saved in dir_audit, which contains the first 250 characters of each transcription plus the time each file took to transcribe. If an audio is mistranscribed, it typically shows up as '...' or the same word/phrase repeated (like 'thank you. thank you. thank you.'). Therefore, this file allows to quickly check if each file was transcribed correctly. 
- Run diarize.py, which uses pyannote which speaker is doing the talking when. It outputs a single CSV for each audio file, saved in dir_diars

Notes:
    - The diarization and the transcribe are independent processes, can be run in any order. 
    - The tscribe.sh and diarize.sh are bash scripts that run the python scripts on UCSF Wynton cluster. You can ignore them unless you use the cluster.
    - To use pyannotate you will need to accept their terms on Hugging Face and provide access token.The access token should be stored as variable auth_token_hg in src/tokens.py