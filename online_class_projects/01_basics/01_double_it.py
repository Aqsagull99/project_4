def main():
    # Ask the user for a number
    curr_value = int(input("Enter a number: "))

    # Double the number until it reaches or exceeds 100
    while curr_value < 100:
        curr_value *= 2  # Double the value
        print(curr_value, end=" ")  # Print result in the same line


# Required to call the main function
if __name__ == '__main__':
    main()
