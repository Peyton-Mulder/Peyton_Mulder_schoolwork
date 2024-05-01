#question 1
username=input("What is your username?\n>")
print("Hello", username)
print("\n")
#question 2
for i in range(101):
    if i % 2 != 0:
       print(i, end=" ")
    elif i > 101:
        break
print("\n")
#question 3
#Please write a Python function, max_num_in_list to return the max number of a given list.
list1= range(100)
print(max(list1))
print("\n")

#question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, 
#unless it is also divisible by 400. The return should be boolean Type (true/false).
condition1="true"
while condition1=="true":
    year=int(input("What year would you like to check? Enter 101 to end the program, it is not a leap year.\n>"))
    if year % 4 ==0:
        print("That is a leap year")
    elif year==101:
        break
    else:
        print("That is not a leap year.")

print("\n")

#Write a function to check to see if all numbers in list are consecutive numbers.
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type.
list2 = [2, 3, 1, 4, 5, 10]
sorted_list2 = sorted(list2)
is_consecutive = all(sorted_list2[i] == sorted_list2[i-1] + 1 for i in range(1, len(sorted_list2)))
print(is_consecutive)

print("Thank you for your time.")