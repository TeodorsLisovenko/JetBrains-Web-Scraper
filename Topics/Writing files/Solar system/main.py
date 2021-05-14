# create the planets.txt

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus",  "Neptune"]

planets_file = open('planets.txt', 'w', encoding='utf-8')

# write the names on separate lines
for planet in planets:
    planets_file.write(planet + '\n')

planets_file.close()
