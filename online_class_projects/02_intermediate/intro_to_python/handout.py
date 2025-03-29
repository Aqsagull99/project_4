#Milestone #1: Mars Weight

# Mars gravity is 37.8% of Earth's gravity
MARS_GRAVITY = 0.378

# Get user input for Earth weight
earth_weight = float(input("Enter a weight on Earth: "))

# Calculate weight on Mars
mars_weight = round(earth_weight * MARS_GRAVITY, 2)

# Display the result
print(f"The equivalent on Mars: {mars_weight}")




#Milestone #2: All Planets

# Gravity conversion factors for each planet
planet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

# Get user input
earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

# Check if the planet is valid and calculate weight
if planet in planet_gravity:
    equivalent_weight = round(earth_weight * planet_gravity[planet], 2)
    print(f"The equivalent weight on {planet}: {equivalent_weight}")
else:
    print("Invalid planet name. Please enter a correct planet.")