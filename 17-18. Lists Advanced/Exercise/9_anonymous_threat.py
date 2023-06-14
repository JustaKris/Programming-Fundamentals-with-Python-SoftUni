def merge(strings, start_index, end_index):
    merged_bit = ''.join(strings[start_index:end_index + 1])
    strings = strings[:start_index] + [merged_bit] + strings[end_index + 1:]
    return strings


def divide(strings, index, partitions):
    partition_length = len(strings[index]) // partitions
    final_partition_length = len(strings[index]) % partitions + partition_length
    element_to_divide = strings[index]
    divided = []
    for partition in range(0, len(element_to_divide) - final_partition_length, partition_length):
        divided.append(element_to_divide[partition:partition + partition_length])
    divided.append(element_to_divide[len(element_to_divide) - final_partition_length:len(element_to_divide)])
    strings = strings[:index] + divided + strings[index + 1:]
    return strings


strings = input().split()
command = input()

while command != "3:1":
    command = command.split()
    if "merge" in command:
        start_index, end_index = int(command[1]), int(command[2])
        strings = merge(strings, start_index, end_index)
    elif "divide" in command:
        index, partitions = int(command[1]), int(command[2])
        strings = divide(strings, index, partitions)
    command = input()

print(" ".join(strings))
