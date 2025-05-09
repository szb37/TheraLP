import os

src = os.path.dirname(os.path.abspath(__file__))
codebase = os.path.abspath(os.path.join(src, os.pardir))
exports = os.path.abspath(os.path.join(codebase, 'exports'))
exports_tscripts = os.path.abspath(os.path.join(exports, 'tscripts'))
exports_diars = os.path.abspath(os.path.join(exports, 'diars'))

models = os.path.abspath('C:/local_models/whisper')
data = os.path.abspath('C:/local_data/TheraLP/')

bap1_audios = os.path.abspath(os.path.join(data, 'BAP1', 'prepped'))
soap_audios = os.path.abspath(os.path.join(data, 'SOAP', 'prepped'))
pdp1_audios = os.path.abspath(os.path.join(data, 'PDP1', 'prepped'))
