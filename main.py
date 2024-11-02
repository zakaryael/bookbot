file_path = "books/frankenstein.txt"
with open(file_path) as f:
    contents = f.read()

def count_words(content: str) -> int:
    """
        function to count the words in a text
        :param content: content of the text
        :return: the number of words in content
    """
    return len(content.split())

def count_character_occurences(content: str) -> dict:
    """
        function to count the number of occurences of each character in a text
        :param content: content of the text
        :return: a maping between characters in the text and their number of occurences
    """
    occurences = {}
    for character in content.lower():
        if character in occurences:
            occurences[character] += 1
        else:
            occurences[character] = 1

    return occurences


n_words = count_words(contents)
occurences = count_character_occurences(contents)
sorted_occurences = dict(sorted(occurences.items(), key=lambda item: item[1], reverse=True))
print(f"--- Begin report of {file_path} ---")
print(f"{n_words} words found in the document \n")

for character, n_occurences in sorted_occurences.items():
    if character.isalpha():
        print(f"The \'{character}\' character was found {n_occurences} times")

print("--- End report ---")
