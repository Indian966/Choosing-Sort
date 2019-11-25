M = [9,5,1,4,3,2]

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