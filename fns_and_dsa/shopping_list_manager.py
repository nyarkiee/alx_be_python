def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"'{item}' added to the shopping list.")


def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")


def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Current Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)

        elif choice == "2":
            item = input("Enter the item to remove: ")
            remove_item(shopping_list, item)

        elif choice == "3":
            view_list(shopping_list)

        elif choice == "4":
            print("Exiting Shopping List Manager.")
            break

        else:
            print("Invalid choice. Please enter 1–4.")


if __name__ == "__main__":
    main()
