cars = ['BMW', 'Audi', 'Ferrari']
for car in cars:
    print(car)

# range: from a to b, b not included, range(start, stop, step)
for value in range(1, 5, 2):
    print(value)

squares = [value**2 for value in range(1, 12)]

# Duplicate list
new_cars = cars[:]

# link list
new_cars = cars
