import time

# create a function that will do a count down operation for a given number of seconds

def countdown(seconds):
    # loop through the number of seconds
    for i in range(seconds):
        # print the number of seconds left
        print(seconds - i)
        # wait one second
        time.sleep(1)
        return seconds - i