from os import linesep
import googletrans

translator = googletrans.Translator()

read_file_path = r"project9/영어파일.txt"

with open(read_file_path,'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines,dest='ko')
    # print(result1.text)

# Translated 객체
# translate() 함수를 호출하면 반환됨
# src : 입력언어
# dest : 출력언어
# text : 실제 번역 완료한 str
# extra_data : 결과에 대한 추가 정보

print(result1)
# Translated(
#  src=en,
#  dest=ko,
#  text=고통이 없으면 얻는 것도 없다,
#  extra_data="{'confiden...")

print(result1.extra_data)
# {
#     'confidence': None,
#     'parts': [<googletrans.models.TranslatedPart object at 0x7f1b82254290>],
#     'origin_pronunciation': None,
#     'parsed': [
#         [None, None, 'en', [
#             [[0, [[[None, 15]], [True]]]],
#             [['No pain No gain', None, None, 15]],
#             None,
#             ['No pain No gain', 'auto', 'ko', True]
#         ]],
#         [
#             [[None, 'gotong-i eobs-eumyeon eodneun geosdo eobsda', None, True, None, [
#                 ['고통이 없으면 얻는 것도 없다', None, None, None, [
#                     ['고통이 없으면 얻는 것도 없다', [2], []],
#                     ['통증이 없습니다', [5], []],
#                     ['통증 없음이 없습니다', [11], []]
#                 ]]
#             ]]],
#             'ko',
#             1,
#             'en',
#             ['No pain No gain', 'auto', 'ko', True]
#         ],
#         'en'
#     ]
# }