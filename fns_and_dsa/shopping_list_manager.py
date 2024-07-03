def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("Current shopping list:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("The shopping list is currently empty.")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
