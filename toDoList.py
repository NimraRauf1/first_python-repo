# Simple To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to display the menu options
def display_menu():
    print("\n\n----TO-DO LIST----")
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Function to add a task to the list
def add_task():
    task = input("Enter the task you want to add: ")  # Get user input for the task
    tasks.append(task)  # Add the task to the tasks list
    print(f"Task '{task}' added!")  # Confirm the task has been added

# Function to view all tasks in the list
def view_tasks():
    if not tasks:  # Check if the tasks list is empty
        print("No tasks :)")  # Inform the user that there are no tasks
    else:
        print("\nYour Tasks:")  # Print a header for the task list
        for index, task in enumerate(tasks, start=1):  # Enumerate through tasks with a starting index of 1
            print(f"{index}. {task}")  # Print each task with its corresponding number

# Function to remove a task from the list
def remove_task():
    view_tasks()  # Display current tasks to the user
    try:
        task_index = int(input("Enter the task number you want to remove: "))  # Get user input for the task number
        if 1 <= task_index <= len(tasks):  # Check if the input is a valid task number
            removed_task = tasks.pop(task_index - 1)  # Remove the task from the list (adjusting for zero-based index)
            print(f"Task '{removed_task}' removed!")  # Confirm the task has been removed
        else:
            print("Invalid task number.")  # Inform the user if the task number is invalid
    except ValueError:  # Handle the case where input is not an integer
        print("Please enter a valid number.")

# Main function to run the application
def main():
    while True:  # Start an infinite loop to keep the program running
        display_menu()  # Show the menu options
        choice = input("\nChoose an option: ")  # Get user input for menu choice

        if choice == '1':  # If the user chooses to add a task
            add_task()  # Call the add_task function
        elif choice == '2':  # If the user chooses to view tasks
            view_tasks()  # Call the view_tasks function
        elif choice == '3':  # If the user chooses to remove a task
            remove_task()  # Call the remove_task function
        elif choice == '4':  # If the user chooses to exit
            print("Exiting the To-Do List application. Goodbye!")  # Print exit message
            break  # Exit the loop and end the program
        else:  # If the user enters an invalid option
            print("Invalid choice. Please select a valid option.")  # Inform the user of the invalid choice

# Entry point of the program
if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call the main function to start the application