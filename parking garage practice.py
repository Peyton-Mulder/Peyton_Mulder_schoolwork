parking_garage=['space 1','space 2','space 3','space 4','space 5','space 6','space 7','space 8','space 9','space 10'
                'space 11','space 12','space 13','space 14','space 15','space 16','space 17','space 18','space 19','space 20']
filled_spaces=[]
currentTickets=['space 1','space 2','space 3','space 4','space 5','space 6','space 7','space 8','space 9','space 10'
                'space 11','space 12','space 13','space 14','space 15','space 16','space 17','space 18','space 19','space 20']
usedTickets=[]
unpaidTickets=[]
paidtickets=[]
payments_received=[]
condition='true'
help=("Available actions are: help, park, pay, take ticket, space count, ledger, and quit.")
thanks=("Thank you for parking at Super Python Express parking garage!")
print("Welcome to Super Python Express parking garage!")
if condition == "true":
    while True:
        command=input("What would you like to do? \nFor a list of available actions please type 'help' \n>")
        if command == "park":
            filled_spaces.append(parking_garage.pop())
            usedTickets.append(currentTickets.pop())
            print("\nPlease take your ticket with you.")
        elif command =="help":
            print(help)
        elif command =='space count':
            print("\nSpaces open:",parking_garage)
            print("Spaces filled:",filled_spaces)
        elif command =='pay':
            check=input("\nPlease enter the amount you owe for your ticket, the rate is $5 per hour.\n>")
            payments_received.append(check)
        elif command == 'take ticket':    
            print("\nThank you for your payment of $",check)
            parking_garage.append(filled_spaces.pop())
            currentTickets.append(usedTickets.pop())
            print(thanks)
        elif command =='ledger':
            print(payments_received)
        elif command == 'quit':
            print("\nThank you for using my parking simulator, have a great day!\n")
            break