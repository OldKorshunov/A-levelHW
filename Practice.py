def Task1():
    num_of_ent = int(input("Введите количество подъездов: "))
    gr = int(input("Введите количество этажей: "))
    fl = int(input("Введите количество квартир на этаже: "))
    flnum = int(input("Введите номер квартиры: "))

    flat_am = gr * fl * num_of_ent
    if flnum > flat_am:
        print ("Такой квартиры не существует!")
    else:
        fl_gr = gr * fl  # квартир в подъезде
        if flnum % (gr * fl) == 0:
            entr = (flnum - 1) // (gr * fl)
        else:
            entr = flnum // (gr * fl)
        print(entr + 1, ' :подъезд')
        ground = (flnum - (entr * gr * fl)) // fl
        print(ground, ' :этаж')

def Task2():
    wide = 0
    line = ''
    space_am = 0
    star_am = 1
    while wide % 2 == 0:
        try:
            wide = int(input("Введите ширину ромба(нечётное число): "))
        except:
            print("Нужно нечётное!")
        else:
            space_am = int(wide - 1)
            for i in range(0, int(wide/2)):
                print(" " * int(space_am/2) + "*" * int(star_am) + " " * int(space_am/2))
                star_am += 2
                space_am -= 2
            for i in range(0, int(wide/2)+ 1):
                print(" " * int(space_am/2) + "*" * int(star_am) + " " * int(space_am/2))
                star_am -= 2
                space_am += 2
            

def Task3():
    f = open('TestFile.txt', 'r')
    tmp = []
    i = 0
    nums = []
    pre_res = []
    res = 0
    sum_num = 0
    for line in f:
        tmp = line.split(';')
        nums = tmp[0].split(' ')
        pre_res = tmp[1].split(' ')
        res = int(pre_res[0]) + (int(pre_res[1]) * 0.1)
        for i, item in enumerate(nums):
            nums[i] = int(item)
        sum_num = sum(nums) / len(nums)
        if sum_num == res:
            print(nums, res, 'True')
        else:
            print(nums, res, 'False   Правильно: ', sum_num)
    f.close()


def switch():#меню выбора
   t=1
   while t != 0: 
       try: 
        t = int(input(" \nTask1 => 1(курьер); \nTask2 => 2(бриллиант);\nTask3 => 3(файл-тест); \nExit => 0 \nEnter task number: ")) 
       except: 
        print("Incorrect") 
       else: 
           if t == 1: 
            Task1()#курьер 
           elif t == 2: 
            Task2()#бриллиант
           elif t == 3: 
            Task3()#файл-тест
           elif t == 0: 
            print("Exit...")#выход из программы
           else: 
            print("Wrong task!")

switch()
