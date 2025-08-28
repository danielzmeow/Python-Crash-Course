# Python can access the last item in list through "-1", last second through "-2", and so on.
# You can use pop to remove any item in list and then use its value
motorcycles = ['ducati', 'yamaha', 'honda']

del motorcycles[1]
print(motorcycles)

motorcycles.insert(0, 'suzuki')
print(motorcycles)

poped_motorcycle = motorcycles.pop(0)
print(poped_motorcycle)
print(motorcycles)

# remove allows user to remove item by its value
motorcycles.remove('ducati')

# .sort for permanent, sorted for temporary
cars = ['BMW', 'Audi', 'Ferrari']
cars.sort()
sorted(cars)
print(len(cars))