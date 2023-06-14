version_list = list(map(int, input().split(".")))

for i in range(len(version_list) - 1, -1, -1):
    if version_list[i] == 9:
        version_list[i] = 0
    else:
        version_list[i] += 1
        break

print(".".join(map(str, version_list)))
