# functions goes here

# checks user  enter an interger to a given question
def num_checker(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print(" Please enter an interger")

# main routine goes here 
ticket_sold = 0

while True:

    name = input("Please enter name:" )

    if name == "xxx":
        break

    age = num_checker("Pleaes enter your age: ")

    if 12  <= age <= 120:
        pass
    elif age < 12:
        print("you are too young to purchase a ticket!")
        continue
    else:
        print("That looks like a typo, please try again! ")
        continue

    ticket_sold += 1



    
print("You have sold {} ticket/s"
      .format(ticket_sold))


