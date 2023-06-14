words = input().split()
palindrome = input()

occurrences = words.count(palindrome)
palindrome_words = [word for word in words if word == word[::-1]]

print(palindrome_words)
print(f"Found palindrome {occurrences} times")
