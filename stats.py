def get_word_count(whole_book):
    words = whole_book.split()
    return len(words)

def get_character_count(whole_book):
    characters = {}
    for letter in whole_book:
        character = letter.lower()
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sorting_dictionary(dictionary):
    dictionaries = []
    for item in dictionary:
        new_dict = {}
        if item.isalpha():
            new_dict["char"] = item
            new_dict["num"] = dictionary[item]
            dictionaries.append(new_dict)
    dictionaries.sort(reverse=True, key=lambda x: x["num"])
    return dictionaries