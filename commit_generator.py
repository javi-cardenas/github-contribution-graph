from datetime import datetime, timedelta
import os
import random
import subprocess

def main():
    """Main function to get user input, create commits, and push them."""
    year = get_user_year()
    percent = get_user_percentage()
    create_commits(year, percent)
    push_commits()


def get_user_year() -> int:
    """Prompt the user to enter a valid year."""
    current_year = datetime.now().year
    while True:
        try:
            year = int(input(f"\nEnter a year between 1970 and {current_year}: "))
            if 1970 <= year <= current_year:
                if confirm(f"You entered {year}. Confirm (y/n): "):
                    return year
            else:
                print("⚠️ Please enter a valid four-digit year...\n")
        except ValueError:
            print("⚠️ Invalid input! Enter a valid four-digit year...\n")


def get_user_percentage() -> float:
    """Prompt the user to enter a percentage for commit frequency."""
    default_percent = 80
    while True:
        try:
            user_input = input(f"\nEnter a number between 1 and 100 to set commit frequency, or press 'Enter' to use the default {default_percent}%: ")
            percent = int(user_input) if user_input else default_percent
            if 1 <= percent <= 100:
                if confirm(f"The graph will be ~{percent}% full. Confirm (y/n): "):
                    return percent / 100
            else:
                print("⚠️ Enter a number between 1 and 100...\n")
        except ValueError:
            print("⚠️ Invalid input! Please enter a number between 1 and 100...\n")


def confirm(prompt: str) -> bool:
    """Utility function to get user confirmation."""
    return input(prompt).strip().lower() == "y"


def create_commits(year: int, percent: float = 0.8) -> None:
    """Generate commits based on user input for the given year."""
    print(f"\n📅 Creating commits for {year}...\n")

    start_date = datetime(year, 1, 1)
    days_in_year = (datetime(year + 1, 1, 1) - start_date).days  # Correct leap year calculation

    for day in range(days_in_year):
        if random.random() >= percent:  # Default 80% chance of coding
            continue
        
        commit_date = start_date + timedelta(days=day)
        num_commits = random.randint(1, 4)  # Random number of commits per day
        
        for _ in range(num_commits):
            with open("temp.txt", 'a') as file:
                file.write('a')

            run_command("git add temp.txt")
            commit_message = f"Auto commit for {commit_date.date()}"
            run_command(f'git commit -m "{commit_message}" --date="{commit_date}" --no-edit')

    print("\n✅ All commits have been created!\n")


def push_commits() -> None:
    """Push commits to GitHub and clean up temp files."""
    print("\n🚀 Pushing commits to GitHub...\n")

    run_command("git push origin main")

    print("\n🗑️ Removing temp.txt from repo...\n")
    if os.path.exists("temp.txt"):
        os.remove("temp.txt")
    run_command("git add .")
    run_command('git commit -m "Removed temp.txt"')
    run_command("git push origin main")

    print("\n✅ Done!\n")


def run_command(command: str) -> None:
    """Run a shell command using subprocess."""
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Error running command: {command}\n{e.stderr.decode()}")


if __name__ == "__main__":
    main()
