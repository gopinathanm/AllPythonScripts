import math

print("testing my Pythong in PyCharm")
print('o----')
print(' ||||')
print(10 * 10)
price = 10
price = 10 +10
rating = 4.9
name = 'John Smith'
age  = 20
is_new = True

#name = input('Enter the Name: ')
#age  = input('Enter the Age : ')
#is_new = input('Enter the Patient is New/Old ')
#is_published = False

#print ('The patient name ' + name + ' Age is '+ age + ' and he is new patient ' + is_new)
test = '''
        print ('the price has been multiplied by 10 ', (price*rating),(price * 10))
        
        year_born = int(input('Enter the year you born : '))
        print(type(year_born))
        age       = 2019 - year_born
        
        print('your age is ', age)
        
        weight  = float(input("Enter the weight in pounds"))
        weight_in_kg = weight * 0.453592
        print("Weight in KG :",weight_in_kg)
        
        course = "Python's Course for Beginners"
        another = course[:]
        
        print(another)
        
      
        '''
#test_for_multiple_lines = '''
#Hi,
#This is the test for multiple lines.
#
#Thanks
#Test Team
#
#'''
#print (test_for_multiple_lines)
'''
first_name = 'John'
last_name  = 'Smith'
print(first_name+' ['+last_name+'] is a coder')
#how to format the string
msg = f'{first_name} [{last_name}] is a coder'
print('formated string ',msg.title())#just like caps initial letters
print(msg[0:len(msg)])
'''
'''
math_test = 5

print(math.factorial(math_test), math.frexp(math_test), math.remainder(3,2))

hot_or_cold = input("Enter hot day or cold day")

if (hot_or_cold.lower() == 'hot'):
    print("It's a hot day")
    print("Drink plenty of Water.")
elif (hot_or_cold.lower() == 'cold'):
    print("it is a Cold Day")
    print("wear cloth appropirate")
else:
    print("have a nice day")


price_of_a_house = 1000000
has_good_credit = False
if has_good_credit:
    down_payment = price_of_a_house *.1
else:
    down_payment = price_of_a_house * .2

print_condition = f'you need to put down  ${down_payment}'
print(print_condition)

name_entered = input ("Enter the name : ")
if (len(name_entered) < 3):
    print("Name must be at least 3 characters long")
elif (len(name_entered) > 50):
    print("Name must be a maximum of 50 characters")
else:
    print("name looks good! "+ name_entered)


weight = int(input("Enter the Weight : "))
l_or_k = str(input("(L)bs or (K)g    : "))

if l_or_k.lower() == 'k':
    convert = round(float(weight) * 2.20462,2)
    print(f"The weight in Lbs is  {convert}")
elif l_or_k.lower() == 'l':
    convert = round(float(weight) * 0.453592,2)
    print(f"The weight in KG is  {convert}")

guess_count = 1
while guess_count <= 3:
    guess = int(input("Guess:"))
    if guess == 9:
        print("You Win")
        break
    guess_count += 1
else:
    print("Game Over!")

command = ''
user_input = ''
while True:
    command = input(">").lower()
    if command == 'help':
        print('''
'''
start - to start the car
stop  - to stop the car
quit  - to exit
             '''
'''
    elif command == 'start' and user_input != 'start':
        print("car started..... Ready to go")
    elif command == 'start' and user_input == 'start':
        print("Car already started...")
    elif command == 'stop' and user_input != 'stop':
        print("car stopped.")
    elif command == 'stop' and user_input == 'stop':
        print("Car already stopped.")
    elif command == 'quit':
        break
    else:
        print("I don't understand!")

    if command != user_input:
        user_input = command


list_items = [10,20,30]
list_sum = 0
for i in list_items:
    list_sum += i

print(f"Total items {len(list_items)} and total prices {list_sum}")


for i in range(5):
    for j in range(3):
        print(f"({i},{j})")

numbers = [5,2,5,2,2]
for i in numbers:
    print_value = ''
    for j in range(i):
        print_value += 'X'
    print(print_value)

names = ['John','Bob','Mosh','Sarah','Mary']
print(names[2:])

numbers = [10,0,20,15,22,35,36,9,8]
#first method
largest_number = numbers[0]
for x in numbers:
    if x > largest_number:
        largest_number = x
print (largest_number)
#second method
numbers.sort()
print(numbers[-1])

numbers = [0,3,5,0,3,4,2]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print (unique)


number_dict = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five"
}

phone = input("Phone: ")
print_list = ''
for x in phone:
   print_list += number_dict.get(x)+' '
print (print_list)


def  greet_user(first_name,last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcom Aboard")


greet_user(first_name="John",last_name="Smith")


def  square(number):
    return number*number


print(f"The square of {5} = {square(5)}")

print(f"total = {55.5+76.6+30.3}")

try:
    age = int(input ("Age:"))
    income = 20000
    risk   = income/age
    print (age)
except ValueError:
    print("Please enter integer")
except ZeroDivisionError:
    print("Age cannot be 0")
'''
class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"{self.name} talks a lot")

person = Person("John")
person.talk()