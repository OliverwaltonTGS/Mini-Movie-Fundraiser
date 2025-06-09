# main routine goes here 

#set maximum number of tickets below 
MAX = 3

# loop to sell tickets 
tickets_sold = 0
while tickets_sold < MAX:
    name = input("Please enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break
    
    tickets_sold += 1

# output number of total sold

if tickets_sold == MAX:
    print("Congratulations, you have sold all the tickets!")
else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining"
          .format(tickets_sold, MAX - tickets_sold))


