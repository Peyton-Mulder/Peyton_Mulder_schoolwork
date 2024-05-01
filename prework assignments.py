#question 1
def hello_name(user_name):
    user_name=input("What is your username?\n>")
    print("Hello", user_name)
    print("\n")
#question 2

def first_odds():
    for first_odds in range(101):
        if first_odds % 2 != 0:
            print(first_odds, end=" ")
        elif first_odds > 101:
            break
print("\n")
#question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    a_list= range(100)
    print(max(a_list))
    print("\n")

#question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
#unless it is also divisible by 400. The return should be boolean Type (true/false).
condition1="true"
def is_leap_year(a_year):
    while condition1=="true":
        a_year=int(input("What year would you like to check? Enter 101 to end the program, it is not a leap year.\n>"))
        if a_year % 4 ==0:
            print("That is a leap year")
        elif a_year==101:
            break
        else:
            print("That is not a leap year.")

print("\n")

#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type.

def is_consecutive(a_list2):
    a_list2 = [2, 3, 1, 4, 5, 10]
    sorted_a_list2 = sorted(a_list2)
    is_consecutive = all(sorted_a_list2[first_odds] == sorted_a_list2[first_odds-1] + 1 for first_odds in range(1, len(sorted_a_list2)))
    print(is_consecutive)

print("Thank you for your time.")
