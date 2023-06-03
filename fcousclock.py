import time

def focus_timer(minutes):
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        print("Remaining time: ", i//60, ":", "{:02d}".format(i%60), end="\r")
        time.sleep(1)
    print("Focus session finished!")
