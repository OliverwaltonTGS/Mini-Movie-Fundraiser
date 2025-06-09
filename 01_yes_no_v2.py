# functions go here 
def yes_no(question):

    while True:
        response = input(question) .lower()

        if response == "yes" or response == "y":
            return "yes"
        
        if response == "no" or response == "n":
            return "no"
        

        else:
            print("Please enter yes / no ")


# main routine goes here 
while True:
    instructions = yes_no("Would you like Instructions? ")

    if instructions == "yes":
        print("The instructions")

    print("program continues...")