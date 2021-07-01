
def Task1():
    stud_mark= {'Korsun Valery':[6, 5, 8, 9], 'Ivanov Ivan':[8, 10, 11, 6], 'Rasputin Mark':[11, 6, 8, 10], 'Gordon Dmitry':[12, 12, 12, 12], 'Adolf Hitler':[10, 10, 11, 9], 'Anatoly Zabivnoy':[12, 3, 4, 3]}
    students = stud_mark.keys()
    for element in list(students):
        aver_mark = sum(stud_mark[element])/len(stud_mark[element])
        stud_mark.update({element:aver_mark})
    print('\nStudents marks: ', stud_mark, '\n')
    for name, mark in stud_mark.items():
        if mark == min(stud_mark.values()):
            print(name, ' get the lowest mark: ', mark)
        elif mark == max(stud_mark.values()):
            print(name, ' get the highest mark: ', mark)
        else:continue


def Task2():
    stud_group = {'Ivashchenko Petro':['Python', 'FullStack'], 
        'Korsun Valery':['Java', 'FrontEnd'], 
        'Ivanov Ivan':['FrontEnd',], 
        'Rasputin Mark':['Python', 'FrontEnd', 'FullStack'],
        'Gordon Dmitry':['Java',],
        'Anatoly Zabivnoy':['FrontEnd', 'FullStack'],
        'Adolf Hitler':['Python',]}
    students = stud_group.keys()
    print('\nThis students go in two or more groups:')
    for element in list(students):
        if len(stud_group[element]) >= 2:
            print(element)

    print("\nThese students don't go to the FrontEnd:")
    l = 'FrontEnd'
    for element in list(students):
        if l in stud_group[element]:
            continue
        else: print(element)

    print("\nThese students go to the Python or Java:")
    l = ['Python', 'Java']
    for element in list(students):
        if l[0] in stud_group[element] or l[1] in stud_group[element]:
            print(element)
        else: continue


def Task3():
    lingerie_sizes = {'XXS':{'rus':42, 'ger':36, 'usa':8, 'fra':38, 'uk':24}, 
                      'XS':{'rus':44, 'ger':38, 'usa':10, 'fra':40, 'uk':26},
                      'S':{'rus':46, 'ger':40, 'usa':12, 'fra':42, 'uk':28},
                      'M':{'rus':48, 'ger':42, 'usa':14, 'fra':44, 'uk':30},
                      'L':{'rus':50, 'ger':44, 'usa':16, 'fra':46, 'uk':32},
                      'XL':{'rus':52, 'ger':46, 'usa':18, 'fra':48, 'uk':34},
                      'XXL':{'rus':54, 'ger':48, 'usa':20, 'fra':50, 'uk':36},
                      'XXXL':{'rus':56, 'ger':50, 'usa':22, 'fra':52, 'uk':38}}

    print ('\n', lingerie_sizes.keys())
    size = input('Enter the international size which you want to convert: ')
    size = size.upper()
    print(lingerie_sizes[size])

def switch():#меню выбора
   t=1
   while t != 0: 
       try: 
        t = int(input(" \nTask1 => 1(успеваемость); \nTask2 => 2(студенты-группы);\nTask3 => 3(таблица размеров); \nExit => 0 \nEnter task number: ")) 
       except: 
        print("Incorrect") 
       else: 
           if t == 1: 
            Task1()#успеваемость
           elif t == 2: 
            Task2()#студенты-группы
           elif t == 3: 
            Task3()#таблица размеров
           elif t == 4: 
            print("Exit...")#выход из программы
           else: 
            print("Wrong task!")

switch()
