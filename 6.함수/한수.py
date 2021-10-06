"""

문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

"""
import sys

def solve(limit):
    i = 1
    count = 0
    while i <= limit:
        if i < 100:
            count += 1
        elif i < 1000:
            str_i = str(i)
            index = len(str_i)-1
            if int(str_i[index-2]) - int(str_i[index-1]) == int(str_i[index-1]) - int(str_i[index]):
                count += 1
        else:
            pass
        i += 1
    return count
limit = int(sys.stdin.readline())

print(solve(limit))      
        
