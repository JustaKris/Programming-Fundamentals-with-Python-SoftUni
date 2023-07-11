class Party:
    def __init__(self):
        self.people = []


line = input()

party = Party()
while line != "End":
    party.people.append(line)
    line = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
