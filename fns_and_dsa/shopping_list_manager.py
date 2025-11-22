def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Required list

    while True:
        display_menu()  # Required call
        try:
            choice = int(input("Enter your choice: "))  # Must be a number
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(item + " has been added.")
            else:
                print("Item cannot be empty.")

        elif choice == 2:
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(item + " has been removed.")
            else:
                print(item + " not found in the list.")

        elif choice == 3:
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(str(i) + ". " + item)

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
