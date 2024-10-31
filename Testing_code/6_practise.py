def remove_any_character(character, string):
    new_string = ""
    for i in range(0, len(string)):
        if string[i] != character:
            new_string = new_string + string[i]

    return new_string


print(remove_any_character("a","Taha shaikh") )
