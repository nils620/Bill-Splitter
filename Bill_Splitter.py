import random


def create_group():
    print("Enter the number of friends joining (including you):")
    try:
        count = int(input())

    except ValueError:
        print("No one is joining for the party")

    else:
        if count <= 0:
            print("No one is joining for the party")
        else:
            dic = {}
            print("Enter the name of every friend (including you), each on a new line:")
            for _ in range(count):
                dic[input()] = 0
    return dic


def bill_split(dic):
    print("Enter the total bill value: ")
    bill = float(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
    if input().lower() == "yes":
        lucky_one = random.choice(list(dic.keys()))
        count = len(dic) - 1
        print(lucky_one + " is the lucky one!")
    else:
        print("No one is going to be lucky")
        count = len(dic)

    s_bill = round(bill / count, 2)
    for friend in dic:
        if count == len(dic):
            dic[friend] = s_bill

        else:
            if friend != lucky_one:
                dic[friend] = s_bill
    return dic


print(bill_split(create_group()))