cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

cakes = ['chocolate', 'vanilla', 'strawberry']

for cake in cakes:
    if cake == 'chocolate' or cake == 'vanilla':
        print("sold out")
    else:
        print(cake.title())