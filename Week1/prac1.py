def one():
    name=input("what is your Name? ")
    output=open('name.txt','w')
    print(name,file=output)
    output.close()

def two():
    file=open('name.txt','r')
    name=file.read().strip()
    print(name)
    file.close()

def three():
    file=open('numbers.txt','r')
    total=0
    for line in file:
        num=int(line)
        total+=num
    print(total)

three()
