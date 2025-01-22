from datetime import datetime, timedelta
import os
import random

def get_user_year():
    while True:
        try:
            current_year = datetime.now().year
            year = int(input(f"\nEnter a year between 1970 and {current_year}: "))
            if 1970 <= year <= current_year:
                confirmation = input(f"You entered {year}, enter 'y' to confirm: ")
                if confirmation == "y":
                    return year
            else:
                print("Please enter a valid four-digit year...\n")
        except ValueError:
            print("Please enter a valid four-digit year...\n")

def get_user_percentage():
    while True:
        try:
            percent = int(input(f"\nThis number will approximate how full your contribution graph will be, the default value is 80%.\nPress 'Enter' to use the default value or enter a number between 1 and 100: "))
            if 1 <= percent <= 100:
                pass
            else:
                percent = 80
            confirmation = input(f"The graph will be ~{percent}% full, enter 'y' to confirm: ")
            if confirmation == "y":
                return percent / 100
        
        except ValueError:
            percent = 80
            confirmation = input(f"The graph will be ~{percent}% full, enter 'y' to confirm: ")
            if confirmation == "y":
                return percent / 100

def create_commits(year, percent=0.8):
    print(f"\nCreating commits for {year}...\n")

    start_date = datetime(year, 1, 1)
    days_in_year = 366 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 365 # leap year check

    for day in range(days_in_year):
        if random.random() >= percent: # default 80% chance I code on a single day
            continue
        
        commit_date = start_date + timedelta(days=day)
        commit_message = f"Auto commit for {commit_date.date()}"
        commit_command = f"git commit -m \"{commit_message}\" --date=\"{commit_date}\" --no-edit"
        num_commits = random.randint(1, 4)
        for _ in range(num_commits):
            with open("temp.txt", 'a') as file:
                file.write('a')
                os.system("git add temp.txt")
                os.system(commit_command)

    print("\nAll commits have been created!\n")

def push_commits():
    print("\nPushing commits to GitHub...\n")

    os.system("git push origin main")

    print("\nRemoving temp.txt from repo...\n")
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
    os.system("git add .")
    os.system('git commit -m "Removed temp.txt"')
    os.system("git push origin main")
    
    print("\nDone!\n")