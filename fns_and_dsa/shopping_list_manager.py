def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ")

        if choice == '1':  # Add item to the list
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add item to the list
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':  # Remove item from the list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item from the list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':  # View current shopping list
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")  # Display each item with its index
            else:
                print("Your shopping list is empty.")

        elif choice == '4':  # Exit the program
            print("Goodbye!")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice. Please try again.")  # Handle invalid inputs

if __name__ == "__main__":
    main()

