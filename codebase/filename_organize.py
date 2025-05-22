import src.folders_local as folders
import os

dir = folders.soap_raws
rename_dict_soap = {
    ### Clinical assessments
    'SOAP1013_Audio_ClinicalAssessment_07Feb2024.m4a':        'SOAP1013_ClinicalAssessment_07Feb2024.m4a',
    'SOAP1270_Baseline.m4a':                                  'SOAP1270_ClinicalAssessment_.m4a',
    'SOAP1349_BaselineClinicalAssessmentAudio_13Jun2024.m4a': 'SOAP1349_ClinicalAssessment_13Jun2024.m4a',
    'SOAP1060_Clinical AssessmentAudio_3Feb2023.m4a':         'SOAP1060_ClinicalAssessment_03Feb2023.m4a',
    'SOAP1361_ClinicalAsessmentAudio_10Jul2024.m4a':          'SOAP1361_ClinicalAssessment_10Jul2024.m4a',
    'SOAP1338_ClinicalAsessmentAudio_29Feb2024.m4a':          'SOAP1338_ClinicalAssessment_29Feb2024.m4a',
    'SOAP1362_ClinicalAssesmentAudio_24Jun2024.m4a':          'SOAP1362_ClinicalAssessment_24Jun2024.m4a',
    'SOAP1304_ClinicalAssessmentAudio_10Jan2024.m4a':         'SOAP1304_ClinicalAssessment_10Jan2024.m4a',
    'SOAP1319_ClinicalAssessmentAudio_11Apr2024.m4a':         'SOAP1319_ClinicalAssessment_11Apr2024.m4a',
    'SOAP1175_ClinicalAssessmentAudio_13Mar2023.m4a':         'SOAP1175_ClinicalAssessment_13Mar2023.m4a',
    'SOAP1226_ClinicalAssessmentAudio_16Aug2023.m4a':         'SOAP1226_ClinicalAssessment_16Aug2023.m4a',
    'SOAP1201_ClinicalAssessmentAudio_21Apr2023.m4a':         'SOAP1201_ClinicalAssessment_21Apr2023.m4a',
    'SOAP1174_ClinicalAssessmentAudio_22Jun2023.m4a':         'SOAP1174_ClinicalAssessment_22Jun2023.m4a',
    'SOAP1181_ClinicalAssessmentAudio_24Mar2023.m4a':         'SOAP1181_ClinicalAssessment_24Mar2023.m4a',
    'SOAP1021_ClinicalAssessmentAudio_24Oct2022.m4a':         'SOAP1021_ClinicalAssessment_24Oct2022.m4a',
    'SOAP1234_ClinicalAssessmentAudio_27Apr2023.m4a':         'SOAP1234_ClinicalAssessment_27Apr2023.m4a',
    'SOAP1224_ClinicalAssessmentAudio_27Nov2023.m4a':         'SOAP1224_ClinicalAssessment_27Nov2023.m4a',
    'SOAP1215_ClinicalAssessmentAudio_31May2023.m4a':         'SOAP1215_ClinicalAssessment_31May2023.m4a',
    'SOAP1100_ClinicalAssessmentAudio_3Jan2023.m4a':          'SOAP1100_ClinicalAssessment_3Jan2023.m4a',
    'SOAP1212_ClinicalAssessmentAudio_4Apr2023.m4a':          'SOAP1212_ClinicalAssessment_4Apr2023.m4a',
    'SOAP1306_ClinicalAssessmentAudio_5Apr2024.m4a':          'SOAP1306_ClinicalAssessment_5Apr2024.m4a', 
    'SOAP1281_ClinicalAssessmentPart2Audio_1Mar2024.m4a':     'SOAP1281_ClinicalAssessment_1Mar2024.m4a', # part 1 missing
    'SOAP1013_Audio_ClinicalAssessment_07Feb2024.m4a':        'SOAP1013_ClinicalAssessment_07Feb2024.m4a',
    'SOAP1021_ClinicalAssessmentAudio_24Oct2022.m4a':         'SOAP1021_ClinicalAssessment_24Oct2022.m4a',
    'audio1698195164.m4a':                                    'SOAP1032_ClinicalAssessment_29Jun2022.m4a',
    ### Med & Fam hx
    'SOAP1361_Med&FamHxAudio_10Jul2024.m4a':        'SOAP1361_MedFamHx_10Jul2024.m4a',
    'SOAP1319_Med&FamHxAudio_11Apr2024.m4a':        'SOAP1319_MedFamHx_11Apr2024.m4a',
    'SOAP1349_Med&FamHxAudio_13Jun2024.m4a':        'SOAP1349_MedFamHx_13Jun2024.m4a',
    'SOAP1362_Med&FamHxAudio_20Jun2024.m4a':        'SOAP1362_MedFamHx_20Jun2024.m4a',
    'SOAP1338_Med&FamHx_29Feb2024.m4a':             'SOAP1338_MedFamHx_29Feb2024.m4a',
    'SOAP1234_MedandFamHxAudio_27Apr2023.m4a':      'SOAP1234_MedFamHx_27Apr2023.m4a',
    'SOAP1226_MedandFamilyHxAudio_16Aug2023.m4a':   'SOAP1226_MedFamHx_16Aug2023.m4a',
    'SOAP1201_MedandFamilyHxAudio_21Apr2023.m4a':   'SOAP1201_MedFamHx_21Apr2023.m4a',
    'SOAP1174_MedandFamilyHxAudio_26Jun2023.m4a':   'SOAP1174_MedFamHx_26Jun2023.m4a',
    'SOAP1224_MedandFamilyHxAudio_27Nov2023.m4a':   'SOAP1224_MedFamHx_27Nov2023.m4a',
    'SOAP1215_MedandFamilyHxAudio_31May2023.m4a':   'SOAP1215_MedFamHx_31May2023.m4a',
    'SOAP1306_MedandFamilyHxAudio_5Apr2024.m4a':    'SOAP1306_MedFamHx_5Apr2024.m4a',
    'SOAP1304_MedandFamilyHxAudio_8Jan2024.m4a':    'SOAP1304_MedFamHx_8Jan2024.m4a',
    'audio1981743637.m4a':                          'SOAP1270_MedFamHx_6Oct2023.m4a',
    ### Screening
    'SOAP1255_RemoteScreenAudio_14Feb2024.m4a':      'SOAP1255_Screen_14Feb2024.m4a',
    'SOAP1277_RemoteScreenAudio_1Feb2024.m4a':       'SOAP1277_Screen_1Feb2024.m4a',
    'SOAP1281_RemoteScreenAudio_1Mar2024.m4a':       'SOAP1281_Screen_1Mar2024.m4a',
    'SOAP1240_RemoteScreenAudio_30May2023.m4a':      'SOAP1240_Screen_30May2023.m4a',
    'SOAP1322_RemoteScreenAudio_7Aug2024.m4a':       'SOAP1322_Screen_7Aug2024.m4a',
    'SOAP1311_RemoteScreenAudio_8Jan2024.m4a':       'SOAP1311_Screen_8Jan2024.m4a',
    'SOAP1076_ClinicalAssessmentMedHxAudio_23Jan2023 .m4a': 'SOAP1076_Screen_23Jan2023.m4a',
    'SOAP1298_Screening_Assessments_audio_2024-Jul-24.m4a': 'SOAP1298_Screen_24Jul2024.m4a',
    'SOAP1255_RescreenClinicalAssessmentAudio_24May2024.m4a': 'SOAP1255_Screen_24May2024.m4a',
    'SOAP1013_RescreenClinicalAssessment_12Jul2024.m4a': 'SOAP1013_Screen_12Jul2024.m4a',
    'SOAP1270_RepeatClinicalAssessmentAudio_13Oct2023.m4a': 'SOAP1270_Screen_13Oct2023.m4a',
    ### Prep A sessions - remote
    'SOAP1298_PrepA_23Aug2024.m4a':                 'SOAP1298_PrepA_Remote_23Aug2024.m4a',
    'SOAP1013_Prep1.m4a':                           'SOAP1013_PrepA_Remote_10Jan2024.m4a',
    'SOAP1281_RemotePrepA.m4a':                     'SOAP1281_PrepA_Remote_11Mar2024.m4a',
    'SOAP1270_RemotePrepAAudio_17Oct2023.m4a':      'SOAP1270_PrepA_Remote_17Oct2023.m4a',
    'SOAP1322_RemotePrepAAudio_17Sep2024.m4a':      'SOAP1322_PrepA_Remote_17Sep2024.m4a',
    'SOAP1362_RemotePrepAAudio_5Jul2024.m4a':       'SOAP1362_PrepA_Remote_5Jul2024.m4a',
    'SOAP1319_RemotePrepAAudio_7May2024.m4a':       'SOAP1319_PrepA_Remote_7May2024.m4a',
    'SOAP1306_RemotePrepAAudio_8May2024.m4a':       'SOAP1306_PrepA_Remote_8May2024.m4a',
    'SOAP1255_RemotePrepAudio_14Jun2024.m4a':       'SOAP1255_PrepA_Remote_14Jun2024.m4a',
    'SOAP1226_RemotePrepAudio_18Aug2023.m4a':       'SOAP1226_PrepA_Remote_18Aug2023.m4a',
    'SOAP1174_RemotePrepAudio_30Jun2023.m4a':       'SOAP1174_PrepA_Remote_30Jun2023.m4a',
    ### Prep A sessions - in person
    'SOAP1319_InPersonPrepAAudio_10May2024.m4a':    'SOAP1319_PrepA_InPerson_10May2024.m4a',
    'SOAP1281_InPersonPrepAAudio_11Mar2024.m4a':    'SOAP1281_PrepA_InPerson_11Mar2024.m4a',
    'SOAP1322_InPersonPrepAAudio_18Sep2024.m4a':    'SOAP1322_PrepA_InPerson_18Sep2024.m4a',
    'SOAP1362_InPersonPrepAAudio_8Jul2024.m4a':     'SOAP1362_PrepA_InPerson_8Jul2024.m4a',
    'SOAP1255_InPersonPrepAudio_18Jun2024.m4a':     'SOAP1255_PrepA_InPerson_18Jun2024.m4a',
    'SOAP1298_InPersonPrepAudio_28Aug2024.m4a':     'SOAP1298_PrepA_InPerson_28Aug2024.m4a',
    'SOAP1013_InPersonPrepAudio_2Aug2024.m4a':      'SOAP1013_PrepA_InPerson_2Aug2024.m4a',
    ### Prep A sessions - ambigous
    'SOAP1100_Prep Session A Audio_19Jan2023 .m4a': 'SOAP1100_PrepA_19Jan2023.m4a',
    'SOAP1021_Prep1Audio_28Oct2022.m4a':            'SOAP1021_PrepA_28Oct2022.m4a',
    'SOAP1076_Prep1Audio_2Feb2023.m4a':             'SOAP1076_PrepA_2Feb2023.m4a',
    'SOAP1032_Prep1_05July2022.m4a':                'SOAP1032_PrepA_05July2022.m4a',
    'SOAP1361_Prep1_20Aug2024.m4a':                 'SOAP1361_PrepA_InPerson_20Aug2024.m4a', # two prep A, resolving as remote/ inperson
    'SOAP1361_PrepA_15Aug2024.m4a':                 'SOAP1361_PrepA_Remote_15Aug2024.m4a', # two prep A, resolving as remote/ inperson
    'SOAP1311_PrepAAudio_16Jan2024.m4a':            'SOAP1311_PrepA_16Jan2024.m4a',
    'SOAP1277_PrepA_audio_2024-Feb-21.m4a':         'SOAP1277_PrepA_2024-Feb-21.m4a',
    'SOAP1224_DoseAPrep1_audio_2023-Dec-05.m4a':    'SOAP1224_PrepA_05Dec2023.m4a',
    ### Prep B sessions
    'SOAP1076_Prep2Audio_6Mar2023.m4a':             'SOAP1076_PrepB_6Mar2023.m4a',
    'SOAP1021_PrepAudio2_5Dec2022.m4a':             'SOAP1021_PrepB_5Dec2022.m4a',
    'SOAP1181_PrepBAudio_12Jul2023.m4a':            'SOAP1181_PrepB_12Jul2023.m4a',
    'SOAP1311_PrepBAudio_14Feb2024.m4a':            'SOAP1311_PrepB_14Feb2024.m4a',
    'SOAP1174_PrepBAudio_14Sep2023.m4a':            'SOAP1174_PrepB_14Sep2023.m4a',
    'SOAP1270_PrepBAudio_15Nov2023.m4a':            'SOAP1270_PrepB_15Nov2023.m4a',
    'SOAP1322_PrepBAudio_16Oct2024.m4a':            'SOAP1322_PrepB_16Oct2024.m4a',
    'SOAP1255_PrepBAudio_17Jul2024.m4a':            'SOAP1255_PrepB_17Jul2024.m4a',
    'SOAP1226_PrepBAudio_26Sep2023.m4a':            'SOAP1226_PrepB_26Sep2023.m4a',
    'SOAP1032_PrepB_08Aug2022.m4a':                 'SOAP1032_PrepB_08Aug2022.m4a',
    'SOAP1224_PrepB_audio_2024-Jan-08.m4a':         'SOAP1224_PrepB_08Jan2024.m4a',
    'SOAP1100_PrepSessionB Audio_20Mar2023.m4a':    'SOAP1100_PrepB_20Mar2023.m4a',
    'SOAP1319_Addtl_Prep_B_audio_2024-July-10.m4a': 'SOAP1319_PrepB_10Jul2024.m4a',
    'SOAP1298_RemotePrepBAudio_23Oct2024.m4a':      'SOAP1298_PrepB_23Oct2024.m4a',
    'SOAP1298_RemotePrepBAudio_25Sep2024.m4a':      'SOAP1298_PrepB_25Sep2024.m4a',
    'SOAP1362_RemotePrepB_Audio_16Aug2024.m4a':     'SOAP1362_PrepB_16Aug2024.m4a',
    'SOAP1277_Preparation_B_audio_2024-Mar-25.m4a': 'SOAP1277_PrepB_25Mar2024.m4a',
    ### Prep C sessions
    'SOAP1021_Prep3Audio_13Jan2023.m4a':            'SOAP1021_PrepC_13Jan2023.m4a',
    'SOAP1322_PrepCAudio_14Nov2024.m4a':            'SOAP1322_PrepC_14Nov2024.m4a',
    'SOAP1076_PrepCAudio_17Apr2023.m4a':            'SOAP1076_PrepC_17Apr2023.m4a',
    'SOAP1100_PrepCAudio_18Apr2023.m4a':            'SOAP1100_PrepC_18Apr2023.m4a',
    'SOAP1311_PrepCAudio_1Apr2024.m4a':             'SOAP1311_PrepC_1Apr2024.m4a',
    'SOAP1270_PrepCAudio_22Jan2024.m4a':            'SOAP1270_PrepC_22Jan2024.m4a',
    'SOAP1181_PrepCAudio_23Aug2023.m4a':            'SOAP1181_PrepC_23Aug2023.m4a',
    'SOAP1226_PrepCAudio_26Oct2023.mp4.m4a':        'SOAP1226_PrepC_26Oct2023.m4a',
    'SOAP1277_PrepCAudio_29Apr2024.m4a':            'SOAP1277_PrepC_29Apr2024.m4a',
    'SOAP1013_PrepCAudio_2Oct2024.m4a':             'SOAP1013_PrepC_2Oct2024.m4a',
    'SOAP1224_PrepCAudio_5Feb2024.m4a':             'SOAP1224_PrepC_5Feb2024.m4a',
    'SOAP1032_PrepC_02Sept2022.m4a':                'SOAP1032_PrepC_02Sept2022.m4a',
    'SOAP1298_RemotePrepCAudio_4Dec2024.m4a':       'SOAP1298_PrepC_4Dec2024.m4a',
    'SOAP1255_RemotePrepC_Audio_14Aug2024.m4a':     'SOAP1255_PrepC_14Aug2024.m4a',
    ### Prep D sessions
    'SOAP1255_PrepDAudio11Sep2024.m4a':             'SOAP1255_PrepD_11Sep2024.m4a',
    'SOAP1100_PrepDAudio_16May2023.m4a':            'SOAP1100_PrepD_16May2023.m4a',
    'SOAP1076_PrepDAudio_23May2023.m4a':            'SOAP1076_PrepD_23May2023.m4a',
    'SOAP1021_PrepDAudio_24Apr2023.m4a':            'SOAP1021_PrepD_24Apr2023.m4a',
    'SOAP1226_PrepDAudio_6Dec2023.m4a':             'SOAP1226_PrepD_6Dec2023.m4a',
    'SOAP1032_PrepD_24Oct2022.m4a':                 'SOAP1032_PrepD_24Oct2022.m4a',
    'SOAP1224_PrepD_Audio_02May2024.m4a':           'SOAP1224_PrepD_02May2024.m4a',
    'SOAP118_PrepDAudio_20Sep2023.m4a':             'SOAP1181_PrepD_20Sep2023.m4a',
    'SOAP1298_RemotePrepDAudio_10Jan2025.m4a':      'SOAP1298_PrepD_10Jan2025.m4a',
    ### A1 and other A integrations
    'SOAP1319_A1IntegrationAudio_12Jun2024.m4a':    'SOAP1319_A1_Integration_12Jun2024.m4a',
    'SOAP1224_A1IntegrationAudio_13Dec2023.m4a':    'SOAP1224_A1_Integration_13Dec2023.m4a',
    'SOAP1281_A1IntegrationAudio_13Mar2024.m4a':    'SOAP1281_A1_Integration_13Mar2024.m4a',
    'SOAP1322_A1IntegrationAudio_20Sep2024.m4a':    'SOAP1322_A1_Integration_20Sep2024.m4a',
    'SOAP1255_A1IntegrationAudio_21Jun2024.m4a':    'SOAP1255_A1_Integration_21Jun2024.m4a',
    'SOAP1270_A1IntegrationAudio_25Oct2023.m4a':    'SOAP1270_A1_Integration_25Oct2023.m4a',
    'SOAP1277_A1IntegrationAudio_28Feb2024.m4a':    'SOAP1277_A1_Integration_28Feb2024.m4a',
    'SOAP1298_A1IntegrationAudio_30Aug2024.m4a':    'SOAP1298_A1_Integration_30Aug2024.m4a',
    'SOAP1174_A1IntegrationAudio_6Jul2023.m4a':     'SOAP1174_A1_Integration_6Jul2023.m4a',
    'SOAP1076_A1IntegrationAudio_8Feb2023.m4a':     'SOAP1076_A1_Integration_8Feb2023.m4a',
    'SOAP1013_A1IntegrationAudio_9Aug2024.m4a':     'SOAP1013_A1_Integration_9Aug2024.m4a',
    'SOAP1181_A1IntegrationAudio_9Jun2023.m4a':     'SOAP1181_A1_Integration_9Jun2023.m4a',
    'SOAP1311_IntegrationA1_19Jan2024.m4a':         'SOAP1311_A1_Integration_19Jan2024.m4a',
    'SOAP1361_IntegrationA1_22Aug2024.m4a':         'SOAP1361_A1_Integration_22Aug2024.m4a',
    'SOAP1226_IntegrationA1_25Aug2023.m4a':         'SOAP1226_A1_Integration_25Aug2023.m4a',
    'SOAP1021_IntegrationAudio1_2Nov2022.m4a':      'SOAP1021_A1_Integration_2Nov2022.m4a',
    'SOAP1362_A1IntegrationAudio_10Jul2024.m4a':    'SOAP1362_A1_Integration_10Jul2024.m4a',
    'SOAP1032_A1_Integration8Jul2022.m4a':          'SOAP1032_A1_Integration_8Jul2022.m4a',
    'SOAP1100_A1_IntegrationAudio_25Jan2023.m4a':   'SOAP1100_A1_Integration_25Jan2023.m4a',
    # non A1 integrations
    'SOAP1174_A7IntegrationAudio_11Jul2023.m4a':    'SOAP1174_A7_Integration_11Jul2023.m4a',
    'SOAP1281_A7IntegrationAudio_19Mar2024.m4a':    'SOAP1281_A7_Integration_19Mar2024.m4a',
    'SOAP1174_A14IntegrationAudio_18Jul2023.m4a':   'SOAP1174_A14_Integration_18Jul2023.m4a',
    'SOAP1174_A21Integration_audio_26Jul2023.m4a':  'SOAP1174_A21_Integration_26Jul2023.m4a',
    'SOAP1174_A28IntegrationAudio_2Aug2023.m4a':    'SOAP1174_A28_Integration_2Aug2023.m4a',
    ### B1 and other B integrations
    'SOAP1013_B1Integration.m4a':                   'SOAP1013_B1_Integration_10Jan2024.m4a',
    'SOAP1224_B1IntegrationAudio_10Jan2024.m4a':    'SOAP1224_B1_Integration_10Jan2024.m4a',
    'SOAP1181_B1IntegrationAudio_14Jul2023.m4a':    'SOAP1181_B1_Integration_14Jul2023.m4a',
    'SOAP1311_B1IntegrationAudio_16Feb2024.m4a':    'SOAP1311_B1_Integration_16Feb2024.m4a',
    'SOAP1322_B1IntegrationAudio_18Oct2024.m4a':    'SOAP1322_B1_Integration_18Oct2024.m4a',
    'SOAP1255_B1IntegrationAudio_19Jul2024.m4a':    'SOAP1255_B1_Integration_19Jul2024.m4a',
    'SOAP1361_B1IntegrationAudio_19Sep2024.m4a':    'SOAP1361_B1_Integration_19Sep2024.m4a',
    'SOAP1362_B1IntegrationAudio_21Aug2024.m4a':    'SOAP1362_B1_Integration_21Aug2024.m4a',
    'SOAP1298_B1IntegrationAudio_25Oct2024.m4a':    'SOAP1298_B1_Integration_25Oct2024.m4a',
    'SOAP1226_B1IntegrationAudio_6Oct2023.m4a':     'SOAP1226_B1_Integration_6Oct2023.m4a',
    'SOAP1277_B1_Integration_Audio_2024-MAR-27.m4a':'SOAP1277_B1_Integration_27Mar2024.m4a',
    'SOAP1100_Integration B1 Audio_22Mar2023.m4a':  'SOAP1100_B1_Integration_22Mar2023.m4a',
    'SOAP1076_Integration2Audio_8Mar2023.m4a':      'SOAP1076_B1_Integration_8Mar2023.m4a',
    'SOAP1032_IntegrationB_10Aug2022.m4a':          'SOAP1032_B1_Integration_10Aug2022.m4a',
    'SOAP1021_IntegreationAudio2_7Dec2022.m4a':     'SOAP1021_B1_Integration_7Dec2022.m4a',
    ### C1 and other C integrations
    'SOAP1076_C1IntegrationAudio_19Apr2023.m4a':    'SOAP1076_C1_Integration_19Apr2023.m4a',
    'SOAP1277_C1IntegrationAudio_1May2024.m4a':     'SOAP1277_C1_Integration_1May2024.m4a',
    'SOAP1100_C1IntegrationAudio_20Apr2023.m4a':    'SOAP1100_C1_Integration_20Apr2023.m4a',
    'SOAP1322_C1IntegrationAudio_22Nov2024.m4a':    'SOAP1322_C1_Integration_22Nov2024.m4a',
    'SOAP1270_C1IntegrationAudio_24Jan2024.m4a':    'SOAP1270_C1_Integration_24Jan2024.m4a',
    'SOAP1181_C1IntegrationAudio_25Aug2023.m4a':    'SOAP1181_C1_Integration_25Aug2023.m4a',
    'SOAP1311_C1IntegrationAudio_3Apr2024.m4a':     'SOAP1311_C1_Integration_3Apr2024.m4a',
    'SOAP1013_C1IntegrationAudio_4Oct2024.m4a':     'SOAP1013_C1_Integration_4Oct2024.m4a',
    'SOAP1298_C1IntegrationAudio_6Dec2024.m4a':     'SOAP1298_C1_Integration_6Dec2024.m4a',
    'SOAP1224_C1IntegrationAudio_7Feb2024.m4a':     'SOAP1224_C1_Integration_7Feb2024.m4a',
    'SOAP1226_C1Integration_3Nov2023.m4a':          'SOAP1226_C1_Integration_3Nov2023.m4a',
    'SOAP1021_Integration3Audio_18Jan2023.m4a':     'SOAP1021_C1_Integration_18Jan2023.m4a',
    'SOAP1255_IntegrationC1_16Aug2024.m4a':         'SOAP1255_C1_Integration_16Aug2024.m4a',
    'SOAP1032_IntegrationC_07Sept2022.m4a':         'SOAP1032_C1_Integration_07Sept2022.m4a',
    ### D1 and other D integrations
    'SOAP1021_IntegrationD1Audio_26Apr2023.m4a':     'SOAP1021_D1_Integration_26Apr2023.m4a',
    'SOAP1032_IntegrationD_26Oct2022.m4a':           'SOAP1032_D1_Integration_26Oct2022.m4a',
    'SOAP1255_D1IntegrationAudio_13Sep2024.m4a':     'SOAP1255_D1_Integration_13Sep2024.m4a',
    'SOAP1298_D1IntegrationAudio_17Jan2025.m4a':     'SOAP1298_D1_Integration_17Jan2025.m4a',
    'SOAP1100_D1IntegrationAudio_18May2023.m4a':     'SOAP1100_D1_Integration_18May2023.m4a',
    'SOAP1181_D1IntegrationAudio_22Sep2023.m4a':     'SOAP1181_D1_Integration_22Sep2023.m4a',
    'SOAP1076_D1IntegrationAudio_26May2023.m4a':     'SOAP1076_D1_Integration_26May2023.m4a',
    'SOAP1226_D1IntegrationAudio_8Dec2023.m4a':      'SOAP1226_D1_Integration_8Dec2023.m4a',
    ### Close out integrations
    'SOAP1277_C28CloseOutIntegrationAudio_21May2024.m4a': 'SOAP1277_CloseOut_Integration_21May2024.m4a',
    'SOAP1311_CloseOutIntegrationAudio_15May2024.m4a':    'SOAP1311_CloseOut_Integration_15May2024.m4a',
    'SOAP1224_CloseOutIntegrationAudio_22May2024.m4a':    'SOAP1224_CloseOut_Integration_22May2024.m4a',
    'SOAP1319_CloseOutIntegrationAudio_4Sep2024.m4a':     'SOAP1319_CloseOut_Integration_4Sep2024.m4a',
    'SOAP1270_CloseOutIntegration_audio_2024-Mar-01.m4a': 'SOAP1270_CloseOut_Integration_2024-Mar-01.m4a',
    'audio3095519874.m4a':                                'SOAP1013_CloseOut_Integration_18Oct2024.m4a',
    ### Exit interviews
    'SOAP1226_Exit Interview_Audio_12-JUN-2024.m4a': 'SOAP1226_ExitInterview_12Jun2024.m4a',
    'SOAP1281_ExitInterviewAudio_11Sep2024.m4a':     'SOAP1281_ExitInterview_11Sep2024.m4a',
    'SOAP1076_ExitInterviewAudio_17Jun2024.m4a':     'SOAP1076_ExitInterview_17Jun2024.m4a',
    'SOAP1181_ExitInterviewAudio_17Jun2024.m4a':     'SOAP1181_ExitInterview_17Jun2024.m4a',
    'SOAP1277_ExitInterviewAudio_1Nov2024.m4a':      'SOAP1277_ExitInterview_1Nov2024.m4a',
    'SOAP1319_ExitInterviewAudio_24Jan2025.m4a':     'SOAP1319_ExitInterview_24Jan2025.m4a',
    'SOAP1174_ExitInterviewAudio_28Jun2024.m4a':     'SOAP1174_ExitInterview_28Jun2024.m4a',
    'SOAP1270_ExitInterviewAudio_30Aug2024.m4a':     'SOAP1270_ExitInterview_30Aug2024.m4a',
    'SOAP1311_ExitInterviewAudio_9Oct2024.m4a':      'SOAP1311_ExitInterview_9Oct2024.m4a',
    'SOAP1224_ExitInterview_Audio_14Aug2024.m4a':    'SOAP1224_ExitInterview_14Aug2024.m4a',
    'SOAP1255_ExitInterview_audio_24Mar2025.m4a':    'SOAP1255_ExitInterview_24Mar2025.m4a',
    'SOAP1361_Exit_Interview_Audio_3Apr2025.m4a':    'SOAP1361_ExitInterview_3Apr2025.m4a',
    }

def print_sorted_filenames(dir, ignore_chars=8):
    '''
    Print the filename and index of all .mp3 and .m4a files in 'dir' (excluding subdirectories),
    sorted alphanumerically by filename, ignoring the first `ignore_chars` characters in the sort.
    '''
    import os
    filepaths = []
    for file in os.listdir(dir):
        full_path = os.path.join(dir, file)
        if os.path.isfile(full_path) and file.lower().endswith(('.mp3', '.m4a')):
            filepaths.append(full_path)
    # Sort by filename, ignoring the first `ignore_chars` characters
    filepaths.sort(key=lambda x: os.path.basename(x)[ignore_chars:])
    for idx, path in enumerate(filepaths):
        print(f'{idx}: {os.path.basename(path)}')

def rename_files(dir, rename_dict):
    '''
    For each key-value pair in rename_dict, if the key is a filename in dir, rename it to the value.
    Args:
        dir (str): Directory to look for files in (non-recursive).
        rename_dict (dict): Dictionary where keys are current filenames and values are new filenames.
    '''
    not_found = []
    for old_name, new_name in rename_dict.items():
        old_path = os.path.join(dir, old_name)
        new_path = os.path.join(dir, new_name)
        if os.path.isfile(old_path):
            os.rename(old_path, new_path)
        else:
            not_found.append(old_name)
    if not_found:
        print("The following files were not found in the directory and could not be renamed:")
        for fname in not_found:
            print(fname)
    # Print files that are neither key nor value in rename_dict
    all_files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    key_set = set(rename_dict.keys())
    value_set = set(rename_dict.values())
    tracked_set = key_set.union(value_set)
    untracked_files = [f for f in all_files if f not in tracked_set]
    if untracked_files:
        print("The following files in the directory are neither a key nor a value in rename_dict:")
        for fname in untracked_files:
            print(fname)

if __name__ == '__main__':
    #rename_files(dir, rename_dict_soap)
    print_sorted_filenames(dir, ignore_chars=8)