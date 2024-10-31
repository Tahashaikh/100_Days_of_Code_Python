#
#
# def palindrome_check(String):
#     if String == String[::-1]:
#         print("String is palindrome")
#     else:
#         print("String is not palindrome")
#
#
#
# print(palindrome_check("ATA"))


word = "ATTAA"
new_word = ""
reversed_word = "AATTA"
count = len(word)
for i in range(0, count):
    new_word = new_word + word[count-1]
    count = count -1

if new_word == word:
    print("this is pelandrom")
else:
    print("not a pelandrom")

if new_word == reversed_word:
    print("Reversed ")
else:
    print("not reversed")



