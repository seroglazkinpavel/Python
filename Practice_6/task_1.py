#35.В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
fnums = 'C:\\Users\\MSI\\PycharmProjects\\mySite\\seminar_5-6\\35_file.txt'

def get_file(numbers):
    data = open(numbers, 'r')
    dlist = data.read() + ' '
    dlist = list(map(int, dlist.split()))
    data.close()
    return dlist

nums = get_file(fnums)
print(nums)

def find_number(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            return nums[i] + 1

print(find_number(nums))

# Добавить недостающее число в список

'''def get_full_nums(nums):
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            nums.insert(i+1, nums[i] + 1)
    return nums

print(get_full_nums(nums_list))'''

#Применяется функция map