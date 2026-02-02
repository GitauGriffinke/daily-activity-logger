# Daily activity logger
# My first python project

from datetime import datetime
import os

def log_entry():
    """Log a new daily activity entry"""
    print("===Daily ACTIVITY LOGGER===")
    print("Welcome! lets log your day")
    print() #prints a blank line



# Get today's date
today = datetime.now().strftime("%Y-%m-%d")
print(f"Today's date: {today}")
print()

#Ask the user QUESTIONS
print("What did you Accomplish today?")
activity = input("→ ")

print("\nHow are you feeling?(1-10, where 10 is amazing)")
mood = input("→ ")

print("\nAny notes or reflections?")
notes = input("→ ")

if not os.path.exists('entries'):
    os.makedirs('entries')


#save to file
filename = f"entries/{today}.txt"

#open file in 'append' mode and write to it
with open(filename, 'a' , encoding = 'utf-8') as file:
    file.write(f"\n{'='*40}\n")
    file.write(f"Entry logged at:{datetime.now().strftime('%H:%M:%S')}\n")
    file.write(f"{'='*40}\n")
    file.write(f"Mood:{mood}/10\n")
    file.write(f"Notes:{notes}\n")
print("\n Entry saved successfully!")
print(f"saved to: {filename}")


def view_entries():
    """view all past entries"""
    print("\n=== YOUR PAST ENTRIES ===\n")

    if not os.path.exists('entries'):
        print("No entries yet! Create your first entry.")
        return
    
    entries = os.listdir('entries')

    if len(entries) == 0:
        print("NO entries yet! Create your first entry")
        return
    
    for entry_file in sorted(entries):
        print(f"\n {entry_file}")
        with open(f"entries/{entry_file}", 'r' , encoding = 'utf-8') as file:
          print(file.read())

def main():
    """Main menu""" 
    while True:
        print("\n" + '='*40)
        print("DAILY ACTIVITY LOGGER - MAIN MENU")
        print("="*40)
        print("1. log today's activity")
        print("2. view past entries")
        print("3. Exit")
        print() 

        choice = input("choose an option (1-3):" )

        if choice == '1':
            log_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            print("\n Goodbye! keep logging your journey!")   
            break  

        else:
            print("\n Invalid choice. please enter 1, 2, or 3")  

if __name__ == "__main__":
    main()           

    
