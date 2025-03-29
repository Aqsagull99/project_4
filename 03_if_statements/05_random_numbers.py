
import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    
    """Prints 10 random numbers between 1 and 100."""
    for _ in range(N_NUMBERS):  
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")  #end=" " means "add a space after printing instead of moving to a new line
    

if __name__ == '__main__':
    main()



