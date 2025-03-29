# Constants for planetary gravity relative to Earth
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
    # Prompt user for Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt user for planet name
    planet = input("Enter a planet: ")

    # Get the gravity factor, assuming the user enters a valid planet
    if planet in GRAVITY_FACTORS:
        planetary_weight = round(earth_weight * GRAVITY_FACTORS[planet], 2)
        print(f"The equivalent weight on {planet}: {planetary_weight}")
    else:
        print("Invalid planet name. Please enter a correct planet.")

if __name__ == "__main__":
    main()
