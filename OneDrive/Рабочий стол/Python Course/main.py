# print("Введите первое число : " )
# a =  int(input ())
# b =  int(input('Введите Второе число : '))

# print(a ,'+', b, '=', a + b)

# a = 1 < 4 and  5 > 3
# print(a)

# a = 1 == 2
# print(a)

# a= 1!=2
# print(a)

# a ='kjg'
# b ='kjg'
# print(a == b)

# a = 1 < 3 < 5 < 8 < 10
# print(a)

# n = 42359
# sum = 0
# while n >0:
#     x = n%10
#     sum = sum + x
#     n = n//10
# print(sum)


# def quick_sort(array):
#     if len(array) <= 1:
#         return
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if  i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([14,45,8]))

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left =nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len (right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1, 5, 6, 9, 8, 7, 12, 55, 2, 4, 1 ,7]
merge_sort(list1)
print(list1)


