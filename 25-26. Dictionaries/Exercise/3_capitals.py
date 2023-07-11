countries = input().split(", ")
capitals = input().split(", ")

capitals_dict = {countries[i]: capitals[i] for i in range(len(capitals))}  # Dictionary comprehension
# capitals_dict = dict(zip(countries, capitals))  # Zip collection

for k, v in capitals_dict.items():
    print(f"{k} -> {v}")

'''
Bulgaria, Romania, Germany, England
Sofia, Bucharest, Berlin, London
'''