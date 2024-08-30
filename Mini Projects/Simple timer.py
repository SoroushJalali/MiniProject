import datetime
import time

while True:
    print("Choose the option you want")
    choose = input("\t1)timer\n\t2)exit\n\t")
    if choose == "1":
        hour = int(input("enter your time hours:"))
        minute = int(input("enter your time minutes:"))
        second = int(input("enter your seconds:"))
        total = hour * 60 * 60 + minute * 60 + second
        delta = datetime.timedelta(seconds=second, minutes=minute, hours=hour)
        print("starting...")
        time.sleep(2)
        while total >= 0:
            print(delta)
            delta = (delta - datetime.timedelta(seconds=1))
            time.sleep(1)
            total -= 1
        else:
            print("your time is over")
            print("*" * 40, "\n")
    elif choose == "2":
        print("good bye")
        print("*" * 40, "\n")
        break
    else:
        print("The selected option is not correct,try again")
        print("*" * 40, "\n")
