#! /usr/bin/env bash
#$ -S /bin/bash  # run job as a Bash shell [IMPORTANT]
#$ -cwd          # run job in the current working directory

source ~/.bashrc
conda init
conda activate theralp
python diar_remote_pyannot.py
