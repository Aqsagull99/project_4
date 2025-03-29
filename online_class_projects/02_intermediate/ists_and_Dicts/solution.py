# index game
def access_element(lst, index):
    """Returns the element at the specified index or an error message if out of range."""
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    """Modifies the element at a given index or returns an error message if out of range."""
    try:
        lst[index] = new_value
        return f"Updated list: {lst}"
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    """Returns a sliced list from start index to end index."""
    return f"Sliced list: {lst[start:end]}"  # No need for try-except here

def index_game():
    """Interactive index game."""
    lst = [1, 2, 3, 4, 5]  # Example list
    print("Current list:", lst)

    print("\nOptions: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))

    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))

    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))

    else:
        print("Invalid operation.")

if __name__ == "__main__":
    index_game()



#List Practice Solution

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