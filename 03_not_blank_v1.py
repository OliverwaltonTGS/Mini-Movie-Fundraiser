# functions goes here

# check users response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("This cannot be blank, please try again!")

        else:
            return response

# main routine goes here 

while True:
    name = not_blank("Enter your Name or 'xxx' to quit: ")
    if name == "xxx":
        break

print("we are done")