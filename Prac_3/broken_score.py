def main():
    num=get_score()
    print(num)
def get_score(message):
    score=input("score: ")
    if score>85:
        r="HD"
    elif score>75:
        r="D"
    elif score>65:
        r="C"
    elif score>50:
       r="P"
    else:
        r="F"
    return score