import src.core as core
import src.folders_local as folders

fpaths = core.get_audio_fpaths(folders.bap1_audios_raw)
core.process_single_audio_file(
    filepath = fpaths[0],
    out_dir = folders.bap1_audios_preprocessed)

'''
if True:
    fpaths = core.get_audio_fpaths(folders.bap1_audios_raw)
    core.process_audio_files(
        filepaths=folders.bap1_audio_fpaths,
        out_dir=folders.bap1_audios_preprocessed
    )
    core.process_single_audio_file(
        filepath,
        out_dir=None, )
'''
