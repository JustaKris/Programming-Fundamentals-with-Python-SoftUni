pokemons = [int(num) for num in input().split()]

pokemon_value = 0
while pokemons:
    index = int(input())
    if index < 0:
        removed_pokemon = pokemons[0]
        pokemons[0] = pokemons[-1]
    elif index > len(pokemons) - 1:
        removed_pokemon = pokemons[-1]
        pokemons[-1] = pokemons[0]
    else:
        removed_pokemon = pokemons.pop(index)
    pokemon_value += removed_pokemon
    for i in range(len(pokemons)):
        if pokemons[i] <= removed_pokemon:
            pokemons[i] += removed_pokemon
        elif pokemons[i] > removed_pokemon:
            pokemons[i] -= removed_pokemon
print(pokemon_value)
