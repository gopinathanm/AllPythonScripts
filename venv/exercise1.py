price_of_the_house = 1000000
'''
has_a_good_credit = input("Is Buyer has a good Credit [True/False]: ")

if (has_a_good_credit == "True"):
    print("true condition")
    print(f"Down Payment required : {(price_of_the_house/100)*10}")
else:
    print("false condition")
    print(f"Down Payment required : {(price_of_the_house/100)*20}")
'''

has_a_good_credit = True
has_high_income   = True

if has_a_good_credit and has_high_income:
    down_payment = price_of_the_house * 0.1
else:
    down_payment = price_of_the_house * 0.2

print(f"Down Payment required : ${down_payment}")


car_started = False

while True:
    user_input = input('> ')
    if user_input.lower().strip() == 'help':
        print ("""
        Start - start the car.
        Stop  - stop the car.
        Quit  - exit the program.""")
    elif user_input.lower().strip() == 'start':
        if car_started:
            print("car already started")
        else:
            car_started = True
            print("car started.")

    elif user_input.lower().strip() == 'stop':
        if car_started:
            print("car stopped.")
            car_started = False
        else:
            print("car already stopped please start the car again.")
    elif user_input.lower().strip()== 'quit':
        break
    else:
        print("I cann't understand the command. Type help to get the values.")
print("Done.")


prices = [10,20,30,40,50]
total_price = 0
for item in prices:
    total_price += item

print(f"total price in the shopping cart is {total_price}")

numbers = [5,2,5,2,2,1,3,7,6,6]
for item in numbers:
    item_printed = ''
    for x in range(item):
       item_printed += 'X'
    print(item_printed)

print(f"the largest number in the list {numbers} is {numbers[-1]}")
numbers_copy = numbers.copy()
duplicate_list = []
remove_index = []

for item in numbers_copy:
    if numbers_copy.count(item) > 0 and duplicate_list.count(item) == 0:
        duplicate_list.append(item)
''' if  numbers_copy.count(item) > 0 and duplicate_list.count(item) > 1:
       numbers.remove(item)'''
print(f"Duplicat item in {numbers_copy} = {duplicate_list}")

'''print(f"Duplicates item removed original {numbers_copy}  after removal of duplicate {numbers}")'''

phone = input("Enter Phone number: ")
phone_dict = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output = []
your_number = ''
for x in phone:
    output.append(phone_dict.get(x,'!') )
    your_number +=   phone_dict.get(x,'!') + ' '
print(f" phone number entered : {phone} and the list is {output} and different out put is {your_number.strip()}")


class Person:
    def __init__(self,name):
        self.name = name


    def talk(self):
        print (f"This person {self.name} talks a lot")


person = Person('Gopianthan')
print(person.name)
person.talk()
