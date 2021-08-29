"""
문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
"""
import sys
T = int(sys.stdin.readline())  # 테스트 케이스 개수 t를 입력받음

for i in range(1,T+1):  # t 만큼 반복
    a,b = map(int,sys.stdin.readline().split())
    print("Case #{}: {} + {} = {}".format(i,a,b,a+b))