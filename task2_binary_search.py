# Завдання 2. Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. 
# Написана функція для двійкового пошуку повинна повертати кортеж, 
# де першим елементом є кількість ітерацій, потрібних для знаходження елемента. 
# Другим елементом має бути "верхня межа" — це найменший елемент, який є 
# більшим або рівним заданому значенню.


def binary_search_recursive(array, item):
    global counter
    counter+=1
    mid = len(array) // 2

    if len(array) == 1 and array[0] == item:
        return counter, item
    elif len(array) == 1 and array[0]!= item:
        return counter, array[0]
    if item == array[mid]:
        return counter, item
    else:
        if array[mid] > item:
            return binary_search_recursive(array[:mid], item)
        if array[mid] < item:
            return binary_search_recursive(array[mid+1:], item)

def print_binary(lst, i):
    i = i if type(i) != str else eval(i)
    if binary_search_recursive(lst, i)[1] == i:
        print(f"Number found: {binary_search_recursive(lst, i)}")
    else:
        print(f"Number not found. Closest number: {binary_search_recursive(lst, i)}")


counter = 0
lst3 = ['1/21', '2/11', '1/2', '3/4', '11/12', '7/5', '16/5', '10/3']
lst3 = [eval(i) for i in lst3]


print_binary(lst3, '2/11')
print_binary(lst3, '17/4')

