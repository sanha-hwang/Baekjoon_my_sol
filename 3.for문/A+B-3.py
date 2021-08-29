"""

문제
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

출력
1부터 n까지 합을 출력한다.
"""
T = int(input(""))  # 테스트 케이스 개수 t를 입력받음

for i in range(T):  # t 만큼 반복
    a,b = map(int,input("").split())
    print(a+b)