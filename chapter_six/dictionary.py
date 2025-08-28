alien_0 = {'color': 'green', 'points': 5, 'speed': 'medium'}
# Dictionary contains pairs of value keys: color <-> green, points <-> 5, speed <-> medium

# Add new value
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
    
print(f"New position: {alien_0['x_position']}")

# Delete some value
del alien_0['points']
print(alien_0)

# Use .get() to AVOID KeyError
print(alien_0.get('points', "No point available"))