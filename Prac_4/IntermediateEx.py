
def task1():
    listt=[]
    for i in range(5):
        num=int(input("give me a number: "))
        listt.append(num)

    print("first num is",listt[0])
    print("last num is",listt[4])
    print("smallest:",min(listt))
    print("largest:",max(listt))
    avg=sum(listt)/len(listt)
    print("avgerage is: ", avg)

def task2():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    userinput=input("What is your username? ")
    if userinput in usernames:
        print("valid")
    else:
        print("not valid")
task2()