print("<<<<<<<<<<     Welcome to the Letter Converter Robot     >>>>>>>>>>")
print("        // Convert Uppercase to Lowercase or Vice versa!! //        ")

conv = None

while True:
    ulc = input("Would you like to convert to U) UPPERCASE or l)lowercase?: ")
    if ulc == "U":
        conv = input("Please introduce the word/sentence you'd like to convert: ")
        print(conv.upper())
    elif ulc == "l":
        conv = input("Please introduce the word/sentence you'd like to convert: ")
        print(conv.lower())
    else:
        print("Please enter [U] or [l]")
        ulc = input("Would you like to convert to U) UPPERCASE or l)lowercase?: ")
        if ulc == "U":
            conv = input("Please introduce the word/sentence you'd like to convert: ")
            print(conv.upper())
        elif ulc == "l":
            conv = input("Please introduce the word/sentence you'd like to convert: ")
            print(conv.lower())


    nextconv = input("Would you like to do another conversion yes/no?:")
    if nextconv == "yes":
        print(" ")
    elif nextconv == "no":
        print("Thank you for using the Letter Converter, Goodbye!")
        break
    else:
        print("Please enter yes or no")
        nextconv = input("Would you like to do another conversion [yes/no]?: ")
        if nextconv == "no":
            print("Thank you for using the Letter Converter, Goodbye!")
            break






