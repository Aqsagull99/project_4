#Problem #1: List Practice

def main():
    # Create a list called fruit_list
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list
    fruit_list.append('mango')

    # Print the updated list
    print("Updated list:", fruit_list)

if __name__ == "__main__":
    main()




#Problem #2: Index Game

def access_element(lst, index):
    """Returns the element at the specified index or an error message if out of range."""
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    return "Index out of range!"

def modify_element(lst, index, new_value):
    """Replaces the element at the specified index with a new value."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Modified list: {lst}"
    return "Index out of range!"

def slice_list(lst, start, end):
    """Returns a sliced list from start index to end index."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return f"Sliced list: {lst[start:end]}"
    return "Invalid range!"

def index_game():
    """Interactive game for practicing list indexing."""
    sample_list = [10, 20, 30, 40, 50, "apple", "banana"]

    while True:
        print("\nOptions: 1) Access 2) Modify 3) Slice 4) Exit")
        choice = input("Choose an operation (1/2/3/4): ")

        if choice == "1":  # Access
            index = int(input("Enter an index: "))
            print(access_element(sample_list, index))

        elif choice == "2":  # Modify
            index = int(input("Enter an index: "))
            new_value = input("Enter a new value: ")
            print(modify_element(sample_list, index, new_value))

        elif choice == "3":  # Slice
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(sample_list, start, end))

        elif choice == "4":  # Exit
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    index_game()   