population = [int(num) for num in input().split(", ")]
minimum_wealth = int(input())

if sum(population) / len(population) < minimum_wealth:
    print("No equal distribution possible")
else:
    # richest = max(population)
    # richest_index = population.index(max(population))
    for i in range(len(population)):
        richest_index = population.index(max(population))
        if population[i] < minimum_wealth:
            population[richest_index] -= minimum_wealth - population[i]
            population[i] = minimum_wealth
    print(population)
