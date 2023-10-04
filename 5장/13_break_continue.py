"""
    작성일 : 2023년 10월 04일
    작성자 : 컴퓨터공학부 202395013 김현탁
    설명 :  반복을 제어하는 break, continue
            교재 137 페이지

            Test word : programming
"""
word = input("단어를 입력하시오 : ")  # 단어를 입력받는 부분

print(":: break1 ::")
for i in word:  # word (aeiou 를 만났을떄 break 가 걸려서 멈춤)
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        break
    else:  # aeiou 가 아닌 글자들을 만났을떄 출력해줌
        print(i, end="")

print()

print(":: break2 ::")
for i in word:
    if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:  # 모음을 만나면 반복 종료
        break  # 반복을 중단한다. 반복을 빠져 나간다.
    else:
        print(i, end="")

print()

print(":: continue ::")
for i in word:
    if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        continue  # 반복의 시작으로 돌아간다. / 반복을 계속한다 ==> 아래 문장을 만날 수 없다.
    print(i, end="")  # 결과 예상
