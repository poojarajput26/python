import time

def countdown_timer(hours, minutes, seconds):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    print(f"Countdown started for {hours} hours, {minutes} minutes, and {seconds} seconds!")

    while total_seconds > 0:
        hours_left, remainder = divmod(total_seconds, 3600)
        minutes_left, seconds_left = divmod(remainder, 60)
        timeformat = f'{hours_left:02}:{minutes_left:02}:{seconds_left:02}'
        print(timeformat, end='\r')  # Print countdown in the same line
        time.sleep(1)  # Wait for 1 second
        total_seconds -= 1

    print("Time's up! Task completed.")

def main():
    try:
        hours = int(input("Enter the countdown hours: "))
        minutes = int(input("Enter the countdown minutes: "))
        seconds = int(input("Enter the countdown seconds: "))
        countdown_timer(hours, minutes, seconds)
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
