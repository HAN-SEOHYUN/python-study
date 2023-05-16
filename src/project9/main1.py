import googletrans
# 파이썬 구글번역 APi

translator = googletrans.Translator()
# translator 변수에 Translator 객체를 넣음

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en', src='auto')
# translate(번역하고자 하는 str, dest='번역언어 key', src='auto')
# src='auto': src 기본값은 auto 이며, auto 로 설정되어있으면 자동으로 번역하고자 하는 문자가 어떤 문자인지 인식을 한다.
# 어떤 문자를 번역할 것인지 명시해주고 싶으면 ? src="ko"
print(f"행복하세요 => {result1.text}")

str2 = "I am happy"
result2 = translator.translate(str2, dest='ko', src='en')
print(f"I am happy => {result2.text}")

