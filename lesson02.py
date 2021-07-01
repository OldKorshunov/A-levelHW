#FizzBuzz
print("Enter fizz, buzz and amount: ")
Fizz = int(input("Fizz: "))
Buzz = int(input("Buzz: "))
Amount = int(input("Amount: "))
i = 1
line = ''
while i < Amount:
    if i % Fizz == 0 and i % Buzz == 0:
        line += "FB "
    elif i % Fizz == 0:
        line += "F "
    elif i % Buzz == 0:
        line += "B "
    else:
        line += str(i) + ' '
    i += 1

print (line)


#1 Task
print("Task 1")
a = int(input("Enter number: "))
if a % 2 == 0:
    print(a,"- is an even number")
else:
    print(a,"- is an odd number")

#2 Task
print ("\nTask 2")
b = int(input("Enter odd number: "))
if b % 2 == 0:
    print(b, "- is an even number!")
elif b % 3 == 0 and b % 5 == 0 and b % 10 != 0:
    print(b, "- делится на 3 и на 5 но не делится на 10.")
else:
    print(b, "- не делится на 3 и на 5 либо делится на 10.")

#3 Task
print ("\nTask 3")
c = int(input("Введите число что бы узнать его делители: "))
print("Делители числа: ", end = " ",)
i = 0
for i in range(c, 0, -1):
    if (c % i == 0):
        print(i, end = "  ")

#4 Task
print ("\n\nTask 4")
num = int(input("Введите число что бы узнать его розряды и их делители: "))
tmp = 0
res = []

while num >= 1:
   tmp = num // 10
   res.append(num - tmp*10)
   num = tmp

digits = (1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000)
l = len(res)
for i in range (0,l):
   print(digits[i], "=>", res[i])

k = 0
while k < l:
    print("Делители числа ", res[k], ': ')
    for j in range(res[k], 0, -1):
        if (res[k] % j == 0):
            print(j, " ")
    k += 1