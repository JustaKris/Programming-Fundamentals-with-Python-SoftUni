def josephus_permutation(people, k):
    people_list = people.split()
    k = int(k)
    n = len(people_list)
    result = []

    index = 0
    while n > 0:
        index = (index + k - 1) % n
        result.append(people_list.pop(index))
        n -= 1

    print(f"[{','.join(result)}]")


input_people = input()
input_k = input()
josephus_permutation(input_people, input_k)
