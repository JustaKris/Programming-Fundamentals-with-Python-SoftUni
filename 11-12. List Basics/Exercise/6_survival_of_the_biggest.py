integers_list = input().split(" ")
n = int(input())

integers_list = [int(x) for x in integers_list]

smallest = integers_list[::]
smallest.sort()
smallest = smallest[:n]

for element in smallest:
    integers_list.remove(element)

for i in range(len(integers_list)-1):
    print(f"{integers_list[i]}, ", end="")
print(integers_list[-1])
