def win_or_lose(comp,human):
    if(comp == 's' and human == 'w'):
        print("computer choosed snake and human choosed water thus computer wins !")
    elif(comp == 'w' and human == 's'):
        print("computer choosed water and human choosed snake thus Human wins !")
    elif(comp == 'g' and human == 's'):
        print("computer choosed gun and human choosed snake thus computer wins !")
    elif(comp == 's' and human == 'g'):
        print("computer choosed snake and human choosed gun thus human wins !")
    elif(comp == 'g' and human == 'w'):
        print("computer choosed gun and human choosed water thus human wins !")
    elif(comp == 'w' and human == 'g'):
        print("computer choosed water and human choosed gun thus computer wins !")
    elif(comp == 's' and human == 's' or comp == 'g' or human == 'g' and comp == 'w' and human == 'w'):
        print("Both choosed the same one so none of them win the game ! ")


def main():
    import random as rand

    comp = rand.randint(1, 3)

    if comp == 1:
        comp = 's'
    if comp == 2:
        comp = 'w'
    if comp == 3:
        comp = 'g'

# print(comp)
    human = input("ENter the choice among snake(s),water(w) and gun(g)")

    win_or_lose(comp, human)


while(True):
    import time
    time.sleep(2)
    val = int(input("Enter 0 to stop the game: "))
    if(val == 0):
        break
    else:
        main()








