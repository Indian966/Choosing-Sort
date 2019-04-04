t = 0
print("원하시는 정수를 5개 입력해주세요:\n")
unsorted = []
while t < 5:
          n = input()
          unsorted.append(n)
          t = t + 1

print("원하시는 정렬 방식이 있나요?\n")
print("1. 힙정렬  2. 버블정렬  3. 퀵정렬\n")
call = int(input())

def heapsort(unsorted):
        size = len(unsorted) #정렬크기
        for i in range(size, -1, -1) : heapify(unsorted, size, i)
        for i in range(size-1, -1, -1) :
                unsorted[i], unsorted[0] = unsorted[0], unsorted[i]
                heapify(unsorted, i, 0)

def heapify(a, size, i):
        largest = i
        L = 2 * i + 1
        R = 2 * i + 2
        if L < size and a[L] > a[i]:
                largest = L
        if R < size and a[R] > a[largest]:
                largest = R
        if largest != i:
                a[largest], a[i] = a[i], a[largest]
                heapify(a, size, largest)

if call == 1:
        heapsort(unsorted)
        print("정렬 결과는 이렇습니다.\n")
        print(unsorted)

def bubble_sort(a):
	size = len(a)
	for i in range(size-1):
		for j in range(size-i-1):
			if a[j]>a[j+1]: a[j],a[j+1] = a[j+1],a[j]

if call == 2:
        bubble_sort(unsorted)
        print("정렬 결과는 이렇습니다.\n")
        print(unsorted)


print("정렬 결과는 이렇습니다.\n")
