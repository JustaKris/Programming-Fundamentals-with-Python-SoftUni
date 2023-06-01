# def repeater(text, counter):
#     return text * counter


repeater = lambda text, counter: text * counter

string = input()
n = int(input())

print(repeater(string, n))
