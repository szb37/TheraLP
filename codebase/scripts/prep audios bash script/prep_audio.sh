#!/bin/bash

# run from git bash
SILENCE_DURATION="2" # Minimum duration of silence in seconds
MIN_DURATION="5" # Minimum duration of non-silence to be considered not silence
SILENCE_THRESHOLD="-50dB" # Silence threshold in dB

# Loop through all m4a files in the current directory
for input_file in *.m4a; do
    base_name=$(basename "$input_file" .m4a)
    output_file="${base_name}.mp3"

    ffmpeg -i "$input_file" -vn -af "silenceremove=start_periods=1:start_duration=$MIN_DURATION:start_threshold=$SILENCE_THRESHOLD:detection=rms" "$output_file"

done
