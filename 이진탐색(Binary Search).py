찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하여 찾는 알고리즘
데이터가 정렬되어 있어야함,속도가 log이므로 데이터가 1000만 이상의 큰 값이라면 이진탐색을 의심
반복문형
O(logN)
def binary_search(array,target,start,end):
    while(start<=end):
        mid=(start+end)//2
        if(array[mid]==target):
            return mid
        #중간점의 값이 찾고자 하는 값보다 작은 경우
        elif(array[mid]> target): 
            end= mid-1
        #중간점의 값이 찾고자 하는 값보다 큰 경우
        else:    
            start= mid +1
    return None

n,target=list(map(int,input().split()))
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)
if result==None:
    print("찾으시는 원소가 존재하지 않습니다.")
else:
    print(result+1)
