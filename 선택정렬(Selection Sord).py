O(N제곱)

이중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 그다음 작은 데이터를 앞에서 두번쨰 데이터와
바꾸는 과정을 반보가면 어떨까?
가장 기본이 되는 정렬,실행시간은 느리지만 이 구조 자체는 알아둘 필요가 있음

array=[]
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i],array[min_index] = array[min_index].array[i]
print(array)
