print("TESTING"[::-2])
print("TESTING"[::-1])

number = 1234556
check = "HOW"


def find_unique_characters(String):
    lowerStr = String
    count = 0
    unique_characters = []
    for i in range(0, len(lowerStr)):
        if String[i] not in unique_characters:
            unique_characters.append(lowerStr[i])
    return unique_characters


def find_maximum_char(UniqueCharacter, String):
    print(f"--------------{UniqueCharacter}")
    char_count = []
    for i in range(0, len(UniqueCharacter)):
        count = 0
        for j in range(0, len(String)):
            if UniqueCharacter[i] == String[j]:
                count += 1
        char_count.append(f"{UniqueCharacter[i]}{count}")
    return char_count


String = "Muhammad Taha Tariq".strip().lower().replace(' ','')
print(String)
value = ''.join(find_maximum_char(find_unique_characters(String), String))
print(value)
