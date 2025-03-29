
def main():
    user_fav_animal = input("What's your favorite animal? ")
    my_favorite_is = user_fav_animal
    print(f"My favorite animal is also \033[1;3m{my_favorite_is}\033[0m!")  

# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()



