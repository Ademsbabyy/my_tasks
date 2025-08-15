# List Manipulation
# 1. Create a list of five cities
cities = ["Lagos","Ibadan","Ogun","Alabata","Abeokuta"]

# 2. Replace the third city with a new one (entered by user).
cities[2] = input("Enter a city: ")


# 3. Remove the last city
cities.pop()


# 4. Add a new city to the beginning of the list

cities.insert(0,"Maitamma")

# 5. Print the updated list

print(cities)