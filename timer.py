import time 

seconds = int(input("Enter the time in seconds: "))

while seconds > 0:
    min, secs = divmod(seconds, 60)
    timer = f"{min:02}:{secs:02}"
    print(timer, end="\r")
    time.sleep(1)
    seconds -= 1

print("\n Time's Up")