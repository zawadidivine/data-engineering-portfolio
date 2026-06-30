my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    print("\nCurrent list:", my_list)
    print("1. Add a number")
    print("2. Delete a number")
    print("3. Skip this turn (continue)")
    print("4. Exit (break)")

    choice = input("Enter your choice: ")

    if choice == "1":
        number = int(input("Enter a number to add: "))
        my_list.append(number)
        print(number, "has been added.")

    elif choice == "2":
        number = int(input("Enter a number to delete: "))

        if number in my_list:
            index = my_list.index(number)
            del my_list[index]
            print(number, "has been deleted.")
        else:
            print("Number not found.")

    elif choice == "3":
        print("Skipping this turn...")
        continue

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
