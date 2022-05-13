# sets.py
# This program demonstrates various set operations.

baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

# Display members of the baseball set.
print('The following students are on the baseball team:')
for name in baseball:
  print(name)

# Display members of the basketball set.
print()
print('The following students are on the basketball team:')
for name in basketball:
  print(name)

# Demonstrate intersection
print()
print('The following students play both baseball and basketball:')
for name in baseball.intersection(basketball):
  print(name)

# Demonstrate union
print()
print('The following students play either baseball or basketball:')
for name in baseball.union(basketball):
  print(name)