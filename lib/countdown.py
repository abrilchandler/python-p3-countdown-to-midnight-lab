# your code goes here!
import time

def countdown(integer):
    while integer > 0:
        print(f'{integer} SECOND(S)!')
        integer -= 1
        if integer == 0:
            print("HAPPY NEW YEAR!")


countdown(10)
    
def countdown_with_sleep(integer):
    while integer > 0:
        print(f'{integer} SECOND(S)!')
        time.sleep(1)
        integer -= 1

    print("HAPPY NEW YEAR!")
    

countdown_with_sleep(10)