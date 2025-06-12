# calculate the ticket price based on the age
def calc_ticket_price(ver_age):


    # ticket is $7.50 for users under 16 
    if ver_age < 16:
        price = 7.5


    # ticket is $10 for users between 16 and 65
    elif ver_age < 65:
        price = 10.5


    # ticket is $6.50 for 65+ for seniors 
    else:
        price = 6.5

    return price
    
# loop for testing...

while True:

    age = int(input("whats your age?"))

    ticket_cost = calc_ticket_price(age)
    print("Age: {} Ticket price: ${:.2f}"
          .format(age, ticket_cost))