import os

# List directory contents  / file hayi ke dar directory hastand
def list_directory_contents():
    files = os.listdir('.')
    for file in files:
        print(file)

# Change directory / taghire directory
def change_directory(path):
    try:
        os.chdir(path)
        print("Current directory:", os.getcwd())
    except FileNotFoundError:
        print("Directory not found!")

# Create a directory / sakhte directory jadid
def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print("Directory created:", directory_name)
    except FileExistsError:
        print("Directory already exists!")

# Remove a file / hazfe file
def remove_file(filename):
    try:
        os.remove(filename)
        print("File removed:", filename)
    except FileNotFoundError:
        print("File not found! Try adding type to the end of the name.")

# Print working directory / directory fe'li
def print_current_directory():
    print("Current directory:", os.getcwd())

# Read a file / khandane mohtaviate file
def edit_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found! Try adding type to the end of the name.")


# Main menu loop
while True:
    print("\nMenu:")
    print("1. List directory contents")
    print("2. Change directory")
    print("3. Create a directory")
    print("4. Remove a file")
    print("5. Print Current directory")
    print("6. Read a file")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        list_directory_contents()
    elif choice == '2':
        path = input("Enter the directory path: ")
        change_directory(path)
    elif choice == '3':
        directory_name = input("Enter the directory name: ")
        create_directory(directory_name)
    elif choice == '4':
        filename = input("Enter the filename to remove: ")
        remove_file(filename)
    elif choice == '5':
        print_current_directory()
    elif choice == '6':
        filename = input("Enter the filename to edit: ")
        edit_file(filename)
    elif choice == '7':
        print("Goodbye! :)")
        break
    else:
        print("Invalid choice. Please try again.")
