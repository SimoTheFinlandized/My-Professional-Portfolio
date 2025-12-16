import datetime
import json
import os
import re
import math
from collections import defaultdict
from getpass import getpass
import csv

class PDA:
    def __init__(self):
        self.address_book = {}
        self.todo_list = []
        self.diary = defaultdict(list)
        self.calendar_events = defaultdict(list)
        self.password = None
        self.load_data()

    def display_menu(self):
        print("\n=== PDA Main Menu ===")
        print("1. Address Book")
        print("2. Calculator")
        print("3. Clock")
        print("4. Calendar")
        print("5. Diary")
        print("6. To-Do List")
        print("7. Exit")

    def address_book_menu(self):
        while True:
            print("\n=== Address Book ===")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contacts")
            print("4. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                name = input("Enter name: ")
                phone = input("Enter phone: ")
                if self.validate_phone(phone):
                    self.address_book[name] = phone
                    print("Contact added!")
                else:
                    print("Invalid phone number format. Use XXX-XXX-XXXX.")
            elif choice == '2':
                print("\nContacts:")
                for name, phone in self.address_book.items():
                    print(f"{name}: {phone}")
            elif choice == '3':
                query = input("Enter search term (name or phone): ")
                results = {k: v for k, v in self.address_book.items() if query.lower() in k.lower() or query in v}
                if results:
                    print("\nSearch Results:")
                    for name, phone in results.items():
                        print(f"{name}: {phone}")
                else:
                    print("No matches found.")
            elif choice == '4':
                break

    def calculator(self):
        print("\n=== Calculator ===")
        print("1. Basic Calculator")
        print("2. Scientific Calculator")
        choice = input("Select an option: ")

        if choice == '1':
            try:
                expression = input("Enter expression: ")
                result = eval(expression)
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '2':
            try:
                expression = input("Enter scientific expression (use math functions): ")
                result = eval(expression, {"__builtins__": None}, {"math": math})
                print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")

    def clock(self):
        print("\n=== Clock ===")
        print(f"Current Time: {datetime.datetime.now().strftime('%H:%M:%S')}")

    def calendar_menu(self):
        while True:
            print("\n=== Calendar ===")
            print("1. View Today")
            print("2. Add Event")
            print("3. View Events")
            print("4. Set Reminder")
            print("5. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                print(f"Today: {datetime.datetime.now().strftime('%Y-%m-%d')}")
            elif choice == '2':
                date = input("Enter date (YYYY-MM-DD): ")
                if self.validate_date(date):
                    event = input("Enter event description: ")
                    self.calendar_events[date].append(event)
                    print("Event added!")
                else:
                    print("Invalid date format. Use YYYY-MM-DD.")
            elif choice == '3':
                date = input("Enter date to view (YYYY-MM-DD): ")
                if date in self.calendar_events:
                    print(f"\nEvents for {date}:")
                    for i, event in enumerate(self.calendar_events[date], 1):
                        print(f"{i}. {event}")
                else:
                    print("No events found for this date.")
            elif choice == '4':
                date = input("Enter reminder date (YYYY-MM-DD): ")
                if self.validate_date(date):
                    reminder = input("Enter reminder: ")
                    self.calendar_events[date].append(f"REMINDER: {reminder}")
                    print("Reminder set!")
                else:
                    print("Invalid date format. Use YYYY-MM-DD.")
            elif choice == '5':
                break

    def diary_menu(self):
        if not self.password:
            self.password = getpass("Set a password for your diary: ")
            print("Password set!")

        password = getpass("Enter diary password: ")
        if password != self.password:
            print("Incorrect password!")
            return

        while True:
            print("\n=== Diary ===")
            print("1. Add Entry")
            print("2. View Entries")
            print("3. Search Entries")
            print("4. Add Tag")
            print("5. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                date = input("Enter date (YYYY-MM-DD): ")
                if self.validate_date(date):
                    entry = input("Write your diary entry: ")
                    self.diary[date].append({"entry": entry, "tags": []})
                    print("Entry added!")
                else:
                    print("Invalid date format. Use YYYY-MM-DD.")
            elif choice == '2':
                date = input("Enter date to view (YYYY-MM-DD): ")
                if date in self.diary:
                    print(f"\nEntries for {date}:")
                    for i, entry in enumerate(self.diary[date], 1):
                        print(f"{i}. {entry['entry']}")
                        if entry['tags']:
                            print(f"   Tags: {', '.join(entry['tags'])}")
                else:
                    print("No entries found for this date.")
            elif choice == '3':
                query = input("Enter search term: ")
                results = {k: v for k, v in self.diary.items() if any(query.lower() in e['entry'].lower() for e in v)}
                if results:
                    print("\nSearch Results:")
                    for date, entries in results.items():
                        print(f"{date}:")
                        for entry in entries:
                            print(f" - {entry['entry']}")
                else:
                    print("No matches found.")
            elif choice == '4':
                date = input("Enter date of entry (YYYY-MM-DD): ")
                if date in self.diary:
                    entry_num = int(input("Enter entry number: "))
                    if 0 < entry_num <= len(self.diary[date]):
                        tag = input("Enter tag: ")
                        self.diary[date][entry_num-1]['tags'].append(tag)
                        print("Tag added!")
                    else:
                        print("Invalid entry number.")
                else:
                    print("No entries found for this date.")
            elif choice == '5':
                break

    def todo_menu(self):
        while True:
            print("\n=== To-Do List ===")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task Complete")
            print("4. Set Task Priority")
            print("5. Back to Main Menu")
            choice = input("Select an option: ")

            if choice == '1':
                task = input("Enter task: ")
                self.todo_list.append({"task": task, "completed": False, "priority": "medium"})
                print("Task added!")
            elif choice == '2':
                print("\nTasks:")
                for i, task in enumerate(self.todo_list, 1):
                    status = "✓" if task["completed"] else " "
                    print(f"{i}. [{status}] [{task['priority'].upper()}] {task['task']}")
            elif choice == '3':
                task_num = int(input("Enter task number to mark complete: "))
                if 0 < task_num <= len(self.todo_list):
                    self.todo_list[task_num-1]["completed"] = True
                    print("Task marked complete!")
                else:
                    print("Invalid task number.")
            elif choice == '4':
                task_num = int(input("Enter task number to set priority: "))
                if 0 < task_num <= len(self.todo_list):
                    priority = input("Enter priority (high/medium/low): ").lower()
                    if priority in ["high", "medium", "low"]:
                        self.todo_list[task_num-1]["priority"] = priority
                        print("Priority set!")
                    else:
                        print("Invalid priority. Use high/medium/low.")
                else:
                    print("Invalid task number.")
            elif choice == '5':
                break

    def export_data(self):
        print("\n=== Export Data ===")
        print("1. Export Address Book")
        print("2. Export To-Do List")
        print("3. Export Diary")
        choice = input("Select an option: ")

        if choice == '1':
            with open('address_book.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Phone'])
                for name, phone in self.address_book.items():
                    writer.writerow([name, phone])
            print("Address book exported to address_book.csv")
        elif choice == '2':
            with open('todo_list.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Task', 'Completed', 'Priority'])
                for task in self.todo_list:
                    writer.writerow([task['task'], task['completed'], task['priority']])
            print("To-do list exported to todo_list.csv")
        elif choice == '3':
            with open('diary.json', 'w') as f:
                json.dump(dict(self.diary), f, indent=2)
            print("Diary exported to diary.json")

    def import_data(self):
        print("\n=== Import Data ===")
        print("1. Import Address Book")
        print("2. Import To-Do List")
        print("3. Import Diary")
        choice = input("Select an option: ")

        if choice == '1':
            try:
                with open('address_book.csv', newline='') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip header
                    for row in reader:
                        self.address_book[row[0]] = row[1]
                print("Address book imported!")
            except FileNotFoundError:
                print("address_book.csv not found.")
        elif choice == '2':
            try:
                with open('todo_list.csv', newline='') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip header
                    for row in reader:
                        self.todo_list.append({
                            "task": row[0],
                            "completed": row[1].lower() == 'true',
                            "priority": row[2]
                        })
                print("To-do list imported!")
            except FileNotFoundError:
                print("todo_list.csv not found.")
        elif choice == '3':
            try:
                with open('diary.json') as f:
                    self.diary = defaultdict(list, json.load(f))
                print("Diary imported!")
            except FileNotFoundError:
                print("diary.json not found.")

    def save_data(self):
        data = {
            'address_book': self.address_book,
            'todo_list': self.todo_list,
            'diary': dict(self.diary),
            'calendar_events': dict(self.calendar_events),
            'password': self.password
        }
        with open('pda_data.json', 'w') as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists('pda_data.json'):
            with open('pda_data.json', 'r') as f:
                data = json.load(f)
                self.address_book = data.get('address_book', {})
                self.todo_list = data.get('todo_list', [])
                self.diary = defaultdict(list, data.get('diary', {}))
                self.calendar_events = defaultdict(list, data.get('calendar_events', {}))
                self.password = data.get('password')

    def validate_phone(self, phone):
        return re.match(r'^\d{3}-\d{3}-\d{4}

    def validate_date(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")

            if choice == '1':
                self.address_book_menu()
            elif choice == '2':
                self.calculator()
            elif choice == '3':
                self.clock()
            elif choice == '4':
                self.calendar_menu()
            elif choice == '5':
                self.diary_menu()
            elif choice == '6':
                self.todo_menu()
            elif choice == '7':
                self.save_data()
                print("Goodbye!")
                break
            elif choice == '8':
                self.export_data()
            elif choice == '9':
                self.import_data()

if __name__ == "__main__":
    pda = PDA()
    pda.run()
    

