

#Bai3
print("\n 1")
print("\n 1,2")
print("\n 1,2,3,")
print("\n 1,2,3,4 ")
print("\n 1,2,3,4,5")

print("   *")
print("\n *  ", end= "*")
print("\n *   ", end= "*" )
print("\n *    ", end= "*" )
print("\n *     ", end= "*" )
print("*****")

#Bai4
my_list = [90,80,76,68,53,43,30,16,8]
my_list.reverse()

def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

