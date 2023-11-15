"""
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 : lab 9-2
"""

text = "There's a reason some people are working to make \
    it harder to vote, especially for people of color. \
        It’s because when we show up, things change."

# 띄어쓰기로 문자열을 분리하고, 단어의 갯수를 찾아라.
split_text = text.split()
print(split_text)
print(len(split_text))


# 도전문제 9-1

text = "[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) "

# 회사 이름을 * 로 표기하기
# 모든 문자를 소문자로 치환


split_text = text.split()
for i, word in enumerate(split_text):
    if word.lower() in ["kt", "skt", "lg", "samsung"]:
        split_text[i] = "*"
print(" ".join(split_text))


low_text = text.lower()
low_text = (  # 각각 4개의 기업을 전부 * 로 표기해줌
    low_text.replace("kt", "*")
    .replace("samsung", "*")
    .replace("lg", "*")
    .replace("skt", "*")
)
print(low_text)


for word in low_text.split(" "):
    if word == "kt" or word == "samsung" or word == "lg" or word == "skt":
        text += "*"
    else:
        text += word + " "
# 결과 출력
print("text 1 : ", text)
