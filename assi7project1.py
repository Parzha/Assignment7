import random

boys = ['ali', 'reza', 'yasin', 'benyamin',"mehrdad", "sajjad", "aidin", "shahin"]
girls = ["sara", "zari", "neda", "homa", "eli","goli", "mary", "mina"]


couples = []

for i in range(len(boys)):
    couple = []
    boy=random.choice(boys)
    girl=random.choice(girls)

    boy_index = boys.index(boy)
    girl_index =girls.index(girl)


    couple.append(boy)
    couple.append(girl)

    couples.append(couple)

    boys.pop(boy_index)
    girls.pop(girl_index)

print(couples)
print("and everybody is married and happy ")