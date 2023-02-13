"""
def file_read(filepath:str):
    try:
       with open(filepath,"rt") as file:
            print(file.read().upper())
    except FileNotFoundError as e:
        print(e)

path = input("enter your file path with the extension: \n")
file_read(path)
"""



'''read the file then put into a list''' 
"""
def file_read(filepath:str):
    try:
       with open(filepath,"rt") as file:
            print(file.read().split())
    except FileNotFoundError as e:
        print(e)

path = input("enter your file path with the extension: \n")
file_read(path)
"""


'''if the file is demofile.txt don't open the file.
    if the file doesn't exist raise an error
    if the file other than demofile.txt open the file and read'''

"""
import os
def file_read(filepath:str):
    file_name = os.path.basename(filepath) 
    # location = os.path.dirname(filepath) 
    # print(file_name)
    # print(location)
    if file_name != 'demofile.txt':
        try:
            with open(filepath,"rt") as file:
                print(file.read())
        except FileNotFoundError as e:
            print(e)
    else:
        print("the file demofile.txt is confidential")

path = input("enter your file path with the extension: \n")
file_read(path)
"""

"""
# code for reference
chooseFile = input("Enter the file name: ")
try:
    if chooseFile == 'demofile.txt':
        print("I JUST DON'T FEEL LIKE OPENING THE FILE!")
except:
    print("File not found.")
    exit()
"""


"""
# 31/01/2023
# i have mdox-short.txt file and the file contains the email sender and reciever informations along with email data
def email_sender(file_name):
    output_file_path = r"E:\Pavan Learnings\Braineest\week_03\sender.txt"
    try:
        with open(file_name,"rt") as file:
            with open(output_file_path,"wt") as output_file:
                for line in file:
                    if line.startswith('From '):
                        line = line.rstrip().split()
                        output_file.writelines("Sender: " +line[1]+"\n")
    except:
        print("The file not existed in a specified path")


file_path = r"E:\Pavan Learnings\Braineest\week_03\mbox-short.txt"
email_sender(file_path)

"""
"""
def email_sender(file_name:str):
    weekday = dict()
    try:
        with open(file_name,"rt") as file:

            for line in file:
                if line.startswith('From '):
                    line = line.rstrip().split()
                    if line[2] not in weekday:
                        weekday[line[2]] = 1
                    else:
                        weekday[line[2]] += 1 
            print(weekday)
                        
    except:
        print("The file not existed in a specified path")

file_path = "E:\\Pavan Learnings\\Braineest\\week_03\\mbox-short.txt"
email_sender(file_path)
"""

"""
set1 = {1,2,3,4}
set2 = {2,4,5,6}
set3 = set1.symmetric_difference(set2)
print(set3)
"""


"""
# adding prime nubers to set from a list
def prime_numbers(elements:list):
    prime_set = set()
    
    for ele in elements:
        count = 0
        for i in range(1,ele):
            if ele%i == 0:
                count += 1
        if count == 1:
            prime_set.add(ele)

    print(prime_set)

prime_numbers([1,2,3,5,4,7,89,6552,2])
"""

"""
from collections import Counter

def most_common_elements(t):
    return [x for x,y in Counter(t).most_common()]
    # return [x for x in Counter(t).most_common()]

print(most_common_elements((1,2,3,5,4,6,7,1,2,3,5,2,5)))
"""



# 06/02/2023
"""
def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

def decor2(func):
    def inner():
        x = func()
        return 2 * x
    return inner

@decor1
@decor2
def num():
    return 2

@decor2
@decor1
def num2():
    return 2

print(num())
print(num2())
"""

"""write a function named greet(func)

inside greet(func) create another function that does the following:
	1. print something
	2. a variable that uses func to access different arguments (*args)

define another function called say_hello() which prints something
and by calling say_hello() at the end, also the greet(func) should be
provoked.
"""
"""
def greet(func):
    def inside_greet(*args):
        print("I am inside inner function")
        var1 = func(*args)
        return var1
    return inside_greet

@greet
def say_hello():
    print("hello from say_hello function")

print(say_hello())
"""


"""
write a function called authorize(func)
define a wrapper (func inside another func) inside and return
"Unathorized access" if not authorized.
define another function to check whether authorized or not. (True or False)
define the last function named secret_data() 
to say "This is confidential data" if user is authorized.
By calling secret_data you should see if the data is confidential or 
you will provoke the other function that says "Unauthorized access"
"""
"""
def authorize(func):
    def wrapper(*args,**kwargs):
        if not is_auth(*args):
            return "Unathorized access"
        x = func(*args,**kwargs)
        return x
    return wrapper

def is_auth(user: str):
    if user=="pavan":
        return True
    
@authorize
def secret_data(user: str):
   return "This is confidential data"

print(secret_data("pavan"))
print(secret_data("avan"))

"""




"""
write a function called validate(func), define a wrapper inside,
see if arguments were not integer, return and error.
define a function called add(a, b).
when calling the func add in the end, if the args are integers return 
the sum, if even one of them in str, return that error you defined in the
first function.
"""
"""
def validate(func):
    def wrapper(*args,**kwargs):
        '''
        try:
            a = int(input("enter a value: "))
            b = int(input("enter b value: "))
            sum = func(a,b)
            return sum
        except:
            print("enter integer values")
        '''
        for arg in args:
            if not isinstance(arg, int):
                return "Invalid argument type"
        return func(*args, **kwargs)
    return wrapper

@ validate
def adding(a,b):
    return a+b


print(adding(5,6))
print(adding(5,'p'))

"""


# generators

"""10 prime numbers"""
"""
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    return False

def prime_numbers(n):
    num = 2
    count = 0
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


prime_generator = prime_numbers(10)
print(list(prime_generator))

"""

"""write a function to look into a txt file and if a certain word exists, yield the line."""
'''
def find_word(file_name, word:str):
    with open(file_name, "r") as file:
        for line in file:
            if word in line:
                yield line

result = find_word(r'E:\Pavan Learnings\Braineest\week_03\romeo.txt','sun')
print(next(result))
'''


#07/02/2023

"""
def list_ele(ele):
    new_list = []
    [new_list.extend(i) for i in ele]
    print(new_list)

list_ele([[1,2,3],[4,5,6],[7,8,9]])
"""

'''
def list_ele1(ele):
    # print(ele)

    new_list = [i for i in ele]
    print(new_list)

list_ele1([{"apple": 2, "banana": 3},{"movies": ["comedy", "sci-Fi", "Drama"]}])
'''


"""
# cartesian product:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

print([[(i,j) for j in list2] for i in list1])
"""

'''Write a regular expression that matches a date in the format dd/mm/yyyy. 
For example, the string "01/01/2021" should match.'''
"""
import re

pattern = re.compile(r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$")
print(pattern.search('04/06/1997'))

"""


"""Write a regular expression that matches a phone number in the format xxx-xxx-xxxx, where x is a digit. 
For example, the string "123-456-7890" should match."""

"""
import re

pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$")
print(pattern.search('123-456-7891'))
"""

"""Write a regular expression that matches a valid email address. 
For example, the string "example@example.com" should match."""
"""
import re

pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern.search("smth@mail.com"))
"""

"""Write a regular expression that matches a string that starts with a word, followed by one or more whitespace characters, followed by another word. 
For example, the string "hello world" should match."""

"""
import re

pattern = re.compile(r"\b\w+\b\s+\b\w+\b")
print(pattern.search("He know 90 all"))
"""

"""Write a regular expression that matches a string that contains a number with exactly two decimal places.
For example, the string "1.23" should match, but the string "1.234" should not match."""
"""
import re

pattern = re.compile(r"^\d+\.\d{2}$")
print(pattern.search("1.25"))
print(pattern.search("1.2578"))
"""

# 13/02/2023

"""Create methods in a class: In the Person class, add methods like introduce() and greet(). 
The introduce() method should print a brief introduction about the person and the greet() method should print a friendly greeting."""

"""
class Person:
    def __init__(self,name,profession):
        self.name = name
        self.profession = profession


    def introduce(self):
        print(f"I am {self.name} and am a {self.profession}")

    def greet(self):
        print(f"Welcome {self.name}")

object_1 = Person("Pavan","student")
object_1.introduce()
object_1.greet()
"""

"""
Inheritance: Create a subclass called Student that inherits from the Person class. 
Add a new attribute called university to the Student class and initialize it in the constructor. 
Also, override the introduce() method to include information about the student's university.
"""
"""
class Person:
    def __init__(self,name,profession):
        self.name = name
        self.profession = profession


    def introduce(self):
        print(f"I am {self.name} and am a {self.profession}")

    def greet(self):
        print(f"Welcome {self.name}")

class Student(Person):
    def __init__(self,name,profession,university):
        Person.__init__(self,name,profession)
        self.university = university

    def introduce(self):
        print(f"I am {self.name} and am a {self.profession}. I am studying in the {self.university}.")


object_1 = Student("Pavan","student","Ernst Abbe Fachhochschule Jena")
object_1.introduce()
object_1.greet()

"""


"""Define a class Pet with an attribute called name and a method speak(). Create two subclasses Dog and Cat that inherit from the Pet class. 
Override the speak() method in the Dog and Cat classes to return a string that is specific to each type of pet."""

"""
class Pet:
    def __init__(self,sound):
        self.sound = sound
    def speak(self):
        pass

class Dog(Pet):
    def speak(self):
        print(f"sounds like {self.sound}")

class Cat(Pet):
    def speak(self):
        print(f"sounds like {self.sound}")


dog_object = Dog("Bow Bow...")
dog_object.speak()
cat_object = Cat("Mewo Mewo...")
cat_object.speak()
"""

"""Define a class BankAccount with a class variable bank_name and instance variables account_holder_name, balance. 
Initialize the class variables in the constructor and add methods like deposit() and withdraw() to perform transactions. 
Create two instances of the BankAccount class and verify that the class variable is shared among all instances."""

"""
class BankAcccount:
    bank_name = "deutsch bank"
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        print(amount,f"deposited in the {self.bank_name}")
        self.balance = self.balance + amount 
        return self.balance


    def withdraw(self, amount: float):
        print(amount,f"withdrawed in the {self.bank_name}")
        self.balance = self.balance - amount 
        return self.balance

object_1 = BankAcccount("pavan",1000.00)
print(object_1.deposit(100.00))
print(object_1.withdraw(100.00))

"""


"""Write a lambda function that takes a list of numbers as input, 
and returns a new list containing only the positive numbers from the original list."""

"""
fun_list = [lambda arg=i: arg for i in [1,-2,9,10,-56,12] if i > 0]

new_list = []
for ele in fun_list:
    new_list.append(ele())

print(new_list)
"""

"""Write a lambda function that takes a list of dictionaries and 
returns a new list of dictionaries sorted by a specified key."""

dic_in = [{"age":21,"name":"ram"},{"age":24,"name":"Jhon"},{"age":18,"sam":"ram"}]
print(sorted(dic_in, key=lambda t: t["age"]))



"""Write a lambda function that takes a string and 
returns a new string with the first letter of each word capitalized."""