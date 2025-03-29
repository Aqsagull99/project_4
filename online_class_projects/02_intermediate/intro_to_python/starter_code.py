# Gravity constants for planets
GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    # Get weight from the user
    earth_weight = float(input("Enter a weight on Earth: "))

    # Get planet name from the user
    planet = input("Enter a planet: ")

    # Check if the planet is valid
    if planet in GRAVITY_FACTORS:
        planetary_weight = round(earth_weight * GRAVITY_FACTORS[planet], 2)
        print(f"The equivalent weight on {planet}: {planetary_weight}")
    else:
        print("Invalid planet name. Please enter a correct planet.")

if __name__ == "__main__":
    main()


