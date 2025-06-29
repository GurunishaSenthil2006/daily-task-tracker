tasks = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added.")
    elif choice == '2':
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    elif choice == '3':
        num = int(input("Enter task number to delete: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"❌ Removed: {removed}")
        else:
            print("Invalid task number.")
    elif choice == '4':
        break
    else:
        print("Invalid option.")
