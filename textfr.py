while True:

    user_input = str(input("Please enter the text file you wish to read.\nYou can also input the full path of the file. "))

    if len(user_input) > 0:
        file = open(user_input, "r")
        print(file.read())
        

    else:
        print("Please select a file and try again")

