# countdown
# def countdown(n):
#    if n==0:
#        print("Stop")
#    else:
#        print(n)
#        countdown(n-1)
# num = int(input("Enter a number"))
# countdown(num)


# Sum of n natural numbers
# def sum(n):
#    if n==1:
#        return 1
#    else:
#        return n+sum(n-1)
# num = int(input("Enter a number"))
# print("The sum of natural number is",sum(num))


# fibonacci number 
# def fibonacci(n):
#    if n==0:
#        return 0
#    elif n==1:
#        return fibonacci(n-1)+fibonacci(n-2)
# n = int(input("Enter a number "))
# print("The fibonnaci for the following number is",fibonacci(n))


# Sum of given digits
# def sum(n):
#    if len(n) == 0:return 0
#    else:
#        return n[0]+sum(n[1:])
# print(sum([1,2,3,4,5,6]))

        
# Reverse the string 
# def reverse(text):
#    if len(text)==0:
#        return text
#    else:
#        return reverse(text[1:])+text[0]
# print (reverse("HELLO"))


# Sum of digits in given number
# def digit_sum(n):
#    if n==0:
#        return 0
#    else:
#        return (n % 10) +digit_sum(n // 10)
# num=int(input("Enter a number :"))
# print(digit_sum(num))


# Students by marks
# s1=int(input("Enter your English Marks"))
# s2=int(input("Enter your Maths Marks"))
# s3=int(input("Enter your Science Marks"))
# s4=int(input("Enter your Geography Marks"))
# s5=int(input("Enter your History Marks"))

# sum = s1+s2+s3+s4+s5
# print("Total=",sum,"/500")

# if sum>400:
#     print("A Grade")
# elif sum>300:
#     print("B Grade")
# elif sum>200:
#     print("C Grade")
# else:
#     print("Fail !!")