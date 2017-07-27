# this program will check your reaction time
import random
import time
from time import perf_counter as my_counter

input('You ready! hit ENTER to check your reaction time!')
wait = random.randint(1,5)
time.sleep(wait)
start_time = my_counter()
input('Hit Enter, now!!!')
end_time = my_counter()
result = end_time - start_time
if 0.3 < result < 0.55:
    print("You've got excellent REFLEXES")
    print("Your Reaction time: {0:2.10f}".format(result))
elif 0.55 <= result < 1:
    print("Practice on your REFLEXES")
    print("Your Reaction time is {0:2.10f}".format(result))
elif result > 1:
    print("You've got slow reflexes, need improvement")
    print("Your Reaction time is {0:2.10f}".format(result))
elif result < 0.1:
    print("Don't Cheat!!!")
