
sentence = "The Big earth"
sentence_list = sentence.split()
for i in range(0, len(sentence_list)):
    string = sentence_list[i]
    first_char = string[0]
    print(first_char)
    if first_char.islower():
        print("False")

print("True")