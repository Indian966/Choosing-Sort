S = [5,9,2,4,6]
M = [9,5,1,4,3,2]

def exchangeSort(a) :
   n = len(a)
   for i in range(n) :
      for j in range(i+1, n) :
         if a[j] > a[i] :
            a[j],a[i] = a[i], a[j]

def selctionSort(a) :
   n = len(a)
   for i in range(n) :
      small = i
      for j in range(i+1, n) :
         if a[j] < a[small] :
            small = j
      a[i], a[small] = a[small], a[i]

def insertionSort(a) :
   n = len(a)
   for i in range(1, n) :
      x = a[i]
      j =i-1
      while (j>=0 and a[j] > x) :
         a[j+1] = a[j]
         j = j-1
      a[j+1] = x


# def merge_sort(a, left=0, right=-1):
#     def merge(a, left, middle, right):
#     	n1 = middle + 1 - left 
#     	n2 = right - middle
#     	L = [0] * (n1)
#     	R = [0] * (n2)
#     	for i in range(0, n1): L[i]=a[left+i]
#     	for j in range(0, n2): R[j]=a[middle+1+j]
#     	i = j = 0
#     	k = left
#     	while i<n1 and j<n2:
#     		if L[i]<=R[j]: a[k]=L[i]; i+=1; k+=1
#     		else: a[k]=R[j]; j+=1; k+=1
#     	while i<n1: a[k]=L[i]; i+=1; k+=1
#     	while j<n2:	a[k]=R[j]; j+=1; k+=1
#     if right==-1: right=len(a)-1
#     if left>=right: return
#     middle = (left+right-1)//2
#     merge_sort(a, left, middle)
#     merge_sort(a, middle+1, right)
#     merge(a, left, middle, right)

def merge_sort(list) :
   if len(list) <= 1 : return list

   mid = len(list) // 2
   left = list[:mid]
   right = list[mid:]

   left1 = merge_sort(left)
   right1 = merge_sort(right)
   return merge(left1, right1)

def merge(left, right) :
   result = []
   i = 0
   j = 0

   while (i<len(left)) and (j<len(right)) :
      if left[i] < right[j] :
         result.append(left[i])
         i+=1
      else : 
         result.append(right[j])
         j+=1
   while (i<len(left)) :
      result.append(left[i])
   while (j<len(right)) :
      result.append(right[i])
      j+=1
   return result

      


print(merge_sort(M))