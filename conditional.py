"""conditional statements:This are the statements that are used execute based upon the condition ,based upon the condition  the number of times it will execute
                       And here are the following statements that we have in this conditional control statements."""
"""if statement:In this if statement if the condition is true the true statement will execute , if not it goes out of if."""
"""If the grade is greater than 70  pass?"""
marks=int(input("enter the marks"))
if marks>=70:
    print("the student is  got passed")
print("marks")
#if- else statement:if the condition is true the true statement will execute ,else false statement will excute.# write a program weather the number enter by user is  odd or even?
num=int(input("enter the num"))
if num%2==0:
    print("the num is even")
else:
    print(" the num is odd")
# write a program to print hello if the number given by the user is divible by 5 other wize  print bye:
num=int(input("enter the num:"))
if num/5==0:
    print("hello")
else:
    print("bye")
  #write a program weather the  number  enter by the user is divisible by 7 or not?
number=int(input("enter the number:"))
if number%7==0:
    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")
#write a program weather the  number  enter by the user is divisible by 3 or not?
number=int(input("enter the number:"))
if number%3==0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")
"""write a program to accept the percentage from the user and display  the grade according to the following criteria
 conditions >90  A >80 And <=90 B ,>=60 and <=80 C , below 60 D"""
marks=int(input("enter the marks:"))
if marks>90:
    print("A grade")
elif marks>80 and marks<=90:
    print(" B grade")
elif marks>=60 and marks<=80:
    print("C grade")
elif marks<60:
    print("D grade")
 # bank transaction
pin=int(input("enter the pin"))
amount=int(input("enter the amount"))
if pin==pin:
    if amount>=30000:
        print(" Transaction:")
    else:
        print("money will not transact")
else:
    print(" pin is not correct")
