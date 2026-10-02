리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는방법
def sequential_search(n,target,array):
    for i in range(n):
        if array[i]==target:
            return i + 1
