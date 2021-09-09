k = 0
z = 0
age = int(input('Input your age'))
if (age >= 18):
    print('Welkom'.upper())
    k = k + 1
if (age < 18):
    z = z + 1
    print('worning'.upper())
print('Access is permited: ' + str(age >= 18))

First_name = str(input('What is your name?'))
if (First_name == 'Vladislav'):
    k = k + 1
if(First_name != 'Vladislav'):
    z = z + 1
print('Hello ' + First_name)
print('Name is ' + str(First_name == 'Vladislav'))

Surname = str(input('What is your surname?'))
if (Surname == 'Belash'):
    k = k + 1
if(Surname != 'Belash'):
    z = z + 1
print('Hello ' + First_name +' ' + Surname)
print('Surname is: ' + str(Surname == 'Belash'))
Patronage = str(input('What is your Patronage?'))
if (Patronage == 'Leonidovich'):
    k = k + 1
if(Patronage != 'Leonidovich'):
    z = z + 1
print('Hello ' + First_name + ' ' + Surname + ' ' + Patronage)
print('Patronage is: ' + str(Patronage == 'Leonidovich'))

Multiplication = int(input('What is the answer 5 * 5?'))
print('The answer is: ' + str(Multiplication == 25))
if (Multiplication == 25):
    print('Correct  is 25')
    k = k + 1
if(Multiplication != 25):
    print('NOT, correct answer is 25')
    z = z + 1
if(k >= 5):
    print('Good 5 correct out of 5 answers')
if(k == 4):
    print('4 correct out of 5 answers')
if(k == 3):
    print('3 correct out of 5 answers')
if (k == 2):
    print('2 correct out of 5 answers')
if (k == 1):
    print('1 correct out of 5 answers')
if(z == 5):
    print('5 wrong answers')
if(z == 4):
    print('4 wrong answers')
if(z == 3):
    print('3 wrong answers')
if(z == 2):
    print('2 wrong answers')
if(z == 1):
    print('1 wrong answers')


