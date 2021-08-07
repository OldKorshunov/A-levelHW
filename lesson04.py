import random

brands =  [
"BMW",
"Mercedes",
"Toyota",
"Audi",
"Lamborgini",
"Chevrolet",
"Nissan",
"Hyndai",
"Ford",
"Honda"
]

models = [
 ['x5', 'x6', 'm3', 'i8', 'e39'],
 ['GL350', 'SLK', 'Maybach', 'Brabus', 'S600'],
 ['Land Cruser', 'Supra', 'Hilander', 'Avalon', 'RAV4'],
 ['s6', 'a1', 'a5', 'a7', 'q7'],
 ['SVG', 'Aventador', 'Galarda', 'Hurakan', 'Diablo'],
 ['Aveo', 'Camaro', 'Traverse', 'Lachetti', 'Volt'],
 ['Silvia', 'Rogue', 'Juke', 'GTR', 'Leaf'],
 ['Sonata', 'Santa Fe', 'Elantra', 'i30', 'i20'],
 ['Focus', 'Explorer', 'Expedition', 'Fusion', 'Fiesta'],
 ['CRV', 'Civic', 'CRZ', 'Jazz', 'Accord']
]


i = 0
S = "I have {} {}"

for i in range (0,5):
    a = (random.randint(0,9))
    b = (random.randint(0,4))
    print(S.format(brands[a], models[a][b]))
   
