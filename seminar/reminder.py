import os
from datetime import datetime
import time

# A list to store the reminders
reminders = []

# Function to display the menu
def display_menu():
    print("\nWelcome to the Reminder System! 🕰️")
    print("1. Set a Reminder")
    print("2. View All Reminders")
    print("3. Mark Reminder as Done")
    print("4. Exit")

# Function to set a reminder
def set_reminder():
    try:
        reminder_text = input("Enter your reminder: ")
        reminder_date = input("Enter the reminder date (YYYY-MM-DD): ")
        reminder_time = input("Enter the reminder time (HH:MM): ")

        # Convert the date and time to a datetime object
        reminder_datetime = f"{reminder_date} {reminder_time}"
        reminder_datetime = datetime.strptime(reminder_datetime, "%Y-%m-%d %H:%M")

        reminder = {
            "text": reminder_text,
            "datetime": reminder_datetime,
            "done": False
        }
        reminders.append(reminder)
        print(f"Reminder set for {reminder_datetime.strftime('%Y-%m-%d %H:%M')}.")

    except ValueError:
        print("Invalid date or time format! Please enter in the correct format.")

# Function to view all reminders
def view_reminders():
    if not reminders:
        print("No reminders set yet.")
    else:
        print("\nYour Reminders:")
        for idx, reminder in enumerate(reminders, 1):
            status = "Done" if reminder["done"] else "Pending"
            print(f"{idx}. {reminder['text']} at {reminder['datetime'].strftime('%Y-%m-%d %H:%M')} - {status}")

# Function to mark a reminder as done
def mark_reminder_done():
    view_reminders()
    if reminders:
        try:
            reminder_num = int(input("Enter the reminder number to mark as done: "))
            if 1 <= reminder_num <= len(reminders):
                reminders[reminder_num - 1]["done"] = True
                print("Reminder marked as done.")
            else:
                print("Invalid reminder number.")
        except ValueError:
            print("Please enter a valid number.")

# Function to check reminders at intervals (for demonstration purposes)
def check_reminders():
    while True:
        current_time = datetime.now()
        for reminder in reminders:
            if not reminder["done"] and reminder["datetime"] <= current_time:
                print(f"Reminder: {reminder['text']} - Time: {reminder['datetime'].strftime('%Y-%m-%d %H:%M')}")
                reminder["done"] = True  # Mark the reminder as done
        time.sleep(60)  # Check every minute

# Main function to run the reminder system
def reminder_system():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            set_reminder()
        elif choice == '2':
            view_reminders()
        elif choice == '3':
            mark_reminder_done()
        elif choice == '4':
            print("Thank you for using the Reminder System! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the reminder system in a separate thread for demonstration
import threading
reminder_thread = threading.Thread(target=check_reminders, daemon=True)
reminder_thread.start()

# Run the main program
reminder_system()
