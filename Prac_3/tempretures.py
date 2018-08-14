def main():
    user=input("convert to (f)arenheit or (c)elcius")
    num=int(input("what do you want to convert?"))
    if user==f:
        res=far(num)
    else:
        res=cel(num)
    print("converted num is",num)
def cel(num):
    num=num+32*1.8
    num=round(num)
    return num

def far(num):
    num=num-32*9/5
    num=round(num)
    return num
main()