k = 0
age = int(input('Input your age'))
if (age >= 18):
    print('Welkom'.upper())
    k = k + 1
if age < 18:
    print('worning'.upper())
print('Access is permited: ' + str(age >= 18))

First_name = str(input('What is your name?'))
if (First_name == 'Vladislav'):
    k = k + 1
print('Hello ' + First_name)
print('Name is ' + str(First_name == 'Vladislav'))

Surname = str(input('What is your surname?'))
if (Surname == 'Belash'):
    k = k + 1
print('Hello ' + First_name +' ' + Surname)
print('Surname is: ' + str(Surname == 'Belash'))
Patronage = str(input('What is your Patronage?'))
if (Patronage == 'Leonidovich'):
    k = k + 1
print('Hello ' + First_name + ' ' + Surname + ' ' + Patronage)
print('Patronage is: ' + str(Patronage == 'Leonidovich'))

Multiplication = int(input('What is the answer 5 * 5?'))
print('The answer is: ' + str(Multiplication == 25))
if (Multiplication == 25):
    print('Correct  is 25')
    k = k + 1
else:
    print('NOT, correct answer is 25')
if(k >= 3):
    print('Good')
if(k < 3):
    print('Bad')

