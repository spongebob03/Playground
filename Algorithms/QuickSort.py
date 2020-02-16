#Divide and Conquer
def quick_sort(arr):
    low=0
    high=len(arr)-1
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]#pivot값 리스트 정 가운데로
        while low <= high:#두 인덱스가 서로 교차해서 지나칠때까지
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:#두 인덱스 서로 교차해서 지나치지 않았다면 서로 바꿈
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low#분할 기준점이 될 인덱스 반환

    return sort(0, len(arr) - 1)

nlist=[15,20,35,7,19,78,45,36]#정렬되지 않은 배열
print(nlist)