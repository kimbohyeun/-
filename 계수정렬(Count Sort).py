데이터의 크기 범위가 제한되어 정수 형태로 사용할수 있을떄만 사용가능
가장 작은 데이터와 큰 데이터의 값 차이가 1000000을 넘지 않을때가 효과적, 데이터 개수에 비해 범위가 작을수록 효과적
시간,공간복잡도: O(N+K) 데이터최대값:K

array=[]

count=[0] * (max(array)+1) #모든 범위를 포함하는 리스트 선언(전부 0으로 초기화)

for i in range(len(array)):
    count[array[i]] +=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i,end=' ')
    
