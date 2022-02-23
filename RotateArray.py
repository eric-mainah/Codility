def solution(lists, num):
    output_list = []
 
    # Will add values from n to the new list
    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])
 
    # Will add the values before
    # n to the end of new list
    for item in range(0, len(lists) - num):
        output_list.append(lists[item])
 
    return output_list

rotate_num = 3
list_1 = [1, 2, 3, 4, 5, 6]
 
print(solution(list_1, rotate_num))
