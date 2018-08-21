import random
picks=int(input("how many quick picks? "))
for i in range(picks):
    line=[]
    for y in range(6):
        number=random.randint(1,45)
        while number in line:
            number=random.randint(1,45)
        line.append(number)
    line.sort()
    print(" ".join("{:2}".format(number) for number in line))