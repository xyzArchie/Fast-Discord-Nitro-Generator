import random
import string

amount = int(input('How many nitro codes do you want to generate?: '))
value = 1
while value <= amount:
    nitro = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('nitro.txt', "a+")
    f.write(f'{nitro}\n')
    f.close()
    print(f'{nitro}')
    value += 1
