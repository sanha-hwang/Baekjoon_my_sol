"""

문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.




"""

import sys

string = sys.stdin.readline().strip().upper()
set_string = set(string)
counting = dict()
for i in set_string:
    counting[i] = 0
for j in string:
    counting[j] += 1
candidate = [k for k, v in counting.items() if max(counting.values()) == v]
if len(candidate) == 1:
    print(candidate[0])
else:
    print("?")