# Reading first input and building a dictionary of words and their definitions
words_and_definitions = input().split(" | ")
words_dictionary = {}
for word_and_definition in words_and_definitions:
    word, definition = word_and_definition.split(": ")
    if word not in words_dictionary.keys():
        words_dictionary[word] = [definition]
    else:
        words_dictionary[word].append(definition)

# Reading possible test words
test_words = input().split(" | ")

# Reading final command on which to base the printouts
command = input()

# Printouts logic
if command == "Test":
    for word in test_words:
        if word in words_dictionary.keys():
            print(f"{word}:")
            for definition in words_dictionary[word]:
                print(f" -{definition}")
elif command == "Hand Over":
    print(*words_dictionary.keys(), sep=" ")
