# myDeviation.py

# 표준 편차 구하기
import math # 수학과 관련된 모듈

def deviation(list1):
    avg = sum(list1)/len(list1) # 평균
    powSum = 0
    for i in list1:
        powSum += pow(i-avg, 2) # (점수 - 평균)의 제곱
    result = math.sqrt(powSum/len(list1))
    print(result)


# 다음 리스트를 이용하여 표준 편차를 구해주는 함수 deviation을 구현해 보세요.
mylist = [10, 30, 40, 80]

print(math.sqrt(650))
print(math.sqrt(4))

deviation(mylist)
'''
1) 평균을 구합니다.
평균 = 총합(160)/요소갯수 = 160/4 = 40

2) (점수 - 평균)을 제곱을 모두 누적시킵니다.
900 + 100 + 0 + 1600 = 2600

3) 2)의 결과에 돗수를 나눕니다.
2600/요소갯수 = 2600/4 = 650

4) 3)에 루트를 씌웁니다.
루트 650 = 25.4950975

힌트 : sqrt( 650 )
루트는 외부 모듈인 math 모듈의 sqrt를 사용하면 됩니다.
'''