def sort_list(list_to_sort):
    return sorted(list_to_sort)


# Lambda approach
# sort_list_lambda = lambda list_to_sort: sorted(list_to_sort)


numbers = list(map(int, input().split()))

print(sort_list(numbers))
