targets = [int(target) for target in input().split()]
command = input()

shot_targets = 0

while command != "End":
    index = int(command)

    if index in range(len(targets)):
        current_target = targets[index]
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > current_target:
                    targets[i] -= current_target
                else:
                    targets[i] += current_target

        targets[index] = -1
        shot_targets += 1

    command = input()

print(f"Shot targets: {shot_targets} -> ", end="")
print(*targets)

