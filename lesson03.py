import sys
from random import randint as rand

def Task1():#Нахождение суммы списка
    a=[1,2,3,4,5]
    i = 0
    j = 0
    sum1 = 0
    sum2 = 0
    l=len(a)
    while i < l:
        sum1 += a[i]
        i += 1
    print ('WHILE: ',sum1)

    for j in range (0,l):
        sum2 += a[j]
    print ('FOR: ',sum2)

def Task2():#вывод текста программы
    filename = sys.argv[0]
    f = open(filename, 'r')
    for line in f:
        print(line.strip())
    f.close


def Task3():#вывод текста программы задом наперёд
    filename = sys.argv[0]
    f = open(filename, 'r')
    for text in reversed(f.readlines()):
        print(text, end='')

    f.close()

def Task4():#банкомат крупными купюрами
    cash = ''
    sum = int(input("Enter sum: "))
    if sum % 10 != 0:
        print("Error! We have only: 10, 20, 50, 100, 200, 500 and 1000 bins")
    else:
        hundr = sum % 1000
        ten = sum % 100

        thous = sum // 1000
        cash += str(thous) + ' - (1000) '
        sum = sum - thous * 1000

        fivehundr = sum // 500
        cash += str(fivehundr) + ' - (500) '
        sum = sum - fivehundr * 500

        twohundr = sum // 200
        cash += str(twohundr) + ' - (200) '
        sum = sum - twohundr * 200

        hundr = sum // 100
        cash += str(hundr) + ' - (100) '
        sum = sum - hundr * 100

        fifty = sum // 50
        cash += str(fifty) + ' - (50) '
        sum = sum - fifty * 50

        twenty = sum // 20
        cash += str(twenty) + ' - (20) '
        sum = sum - twenty * 20

        ten = sum // 10
        cash += str(ten) + ' - (10) '
        sum = sum - ten * 10

        print(cash)#вывод результата

def Task5():#FizzBuzz2.0 с файлами
    output = ''
    f = open('input.txt', 'w')#открытие файла для заполнения рандомными тройками
    i = 0
    while i < 20:
        f.write(str(rand(1,10)) + ' ' + str(rand(1,10)) + ' ' + str(rand(1,50)) + '\n')
        i += 1
    f.close # закрытие файла

    f = open('input.txt', 'r') #открытие файла для чтения троек
    for line in f: # для каждой строки в файле
        output += 'Для: ' + line
        input = line.split()
        FB = ''
        i = 0
        while i < int(input[2]):#цикл для решения FizzBuzz
            if i % int(input[0]) == 0 and i % int(input[1]) == 0:
                FB += "FB "
            elif i % int(input[0]) == 0:
                FB += "F "
            elif i % int(input[1]) == 0:
                FB += "B "
            else:
                FB += str(i) + ' '
            i += 1
        output += FB + '\n\n'
    f.close() # закрытие файла
    
    f = open('output.txt', 'w')#открытие файла для заполнения выходными данными
    f.write(output)
    f.close # закрытие файла




def switch():#меню выбора
   t=1
   while t != 0: 
       try: 
        t = int(input("Task1 => 1; \nTask2 => 2; \nTask3 => 3; \nTask4 => 4; \nH/W(FizzBuzz#2) => 5; \nExit => 0 \nEnter task number: ")) 
       except: 
        print("Incorrect") 
       else: 
           if t == 1: 
            Task1()#Нахождение суммы списка
           elif t == 2: 
            Task2()#вывод текста программы 
           elif t == 3: 
            Task3()#вывод текста программы задом наперёд 
           elif t == 4: 
            Task4()#банкомат крупными купюрами
           elif t == 5:
            Task5()#FizzBuzz2.0 с файлами
           elif t == 0: 
            print("Exit...")#выход из программы
           else: 
            print("Wrong task!")

switch()