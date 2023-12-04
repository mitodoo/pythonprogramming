maths = int(input("Enter Mark of Maths :"))
eng   = int(input("Enter Mark of English : "))
java  = int(input("Enter Mark of JAVA : "))
python= int(input("Enter Mark of Python: "))
php   = int(input("Enter Mark of PHP: "))

total_marks = maths + eng + java + python + php
print("Total Marks ", total_marks)

per = total_marks / 5
print("Percentage : ", per)

if per >= 35:
    print("Pass")
else:
    print("Fail")
