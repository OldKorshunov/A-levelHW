def spam(number):
    '''Function should return something like this:
    spam(1);#bulochka
    spam(3);#bulochkabulochkabulochka
    But it is broken. Fix it please!

    Эта функция принимает числовой параметр. Должна вернуть строку, которая
    повторяется столько раз, сколько параметров передано. Она уже написана,
    но не работает. Любым способом заставьте ее работать.
    '''
    str = ('bulochka' * number)
    return str


def my_sum(list_of_numbers):

    """Function receives a list with integer numbers,
    should return its sum as an integer. Do not use built in summarize functions.
    :param list

    Функция получает на вход массив чисел, должна вернуть сумму этих чисел.
    Не использовать встроенные функции суммирования.
    
    """
    pass
    #  ...wite your code here
    sum = 0
    for i in list_of_numbers:
        sum += i
    return sum


def shortener(string):
    """
    Function receives a long string with many words.
    It should return the same string, but words,
    larger then 6 symbols should be changed, symbols
    after the sixth one should be replaced by symbol *
    :param string
    :returns string

     Функция получает на вход длинную строку с множеством слов.
     Она должна вернуть ту же строку, но в словах, которые длиннее 6 символов,
     функция должна вместо всех символов после шестого поставить одну звездочку.
     Пример: Из слова 'verwijdering' должно получиться 'verwij*'
     

    """
    pass
    #  ...wite your code here
    
    
    #list = []
    #list = string.split()
    #i = 0
    #for i in range (0, len(list)):
    #    if len(list[i]) > 6:
    #        list[i] = list[i][:6] + '*'
    #    else: continue
    #string = ' '.join(list)

    #map
    list = []
    list = string.split()
    string = ' '.join(map(lambda x: (x[:6] + '*' if len(x) > 6 else x), list))

    return string

def compare_ends(words):
    """
    Function receives an array of strings.
    Please return number of strings, which
    length is at least 2 symbols and first character
    is equal to the last character

    Функция получает на вход массив строк. Вернуть надо количество строк,
    которые не короче двух символов и у которых первый и последний
    символ совпадают.

    """
    pass
    #  ...wite your code here

    count = 0
    for elem in words:
        if len(elem) >= 2 and elem[0] == elem[-1]:
            count += 1
        else: continue
    return count