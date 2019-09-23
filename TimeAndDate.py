import time
from time import perf_counter as my_timer
import random

while True:
    input("press enter to start")

    wait_time = random.randint(1,6)
    time.sleep(wait_time)
    start_time = my_timer()

    input("press enter to stop")

    end_time = my_timer()

    print("Started at " + time.strftime("%X", time.localtime(start_time)))
    print("Ended at " + time.strftime("%X", time.localtime(end_time)))

    print("Your reaction time was {} seconds".format(end_time-start_time))

    str1 = input("Do you wanna try again?(y/n)")

    if str1=='y':
        continue
    elif str1=='n':
        break
    else:
        print("Sorry , Wrong Input , the game is terminating.....")
        break
