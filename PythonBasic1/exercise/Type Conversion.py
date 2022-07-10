#Facebook profile

name = 'Ardit'
age = 27
relationship_status = 'single'

# Now, if we wanted to perhaps change that, let's say my relationship status all of a sudden goes from
# single to it's complicated.

relationship_status = 'it\`s complicated'

print(relationship_status)

# Let's create a program that guesses your age.

birth_year = input('what year where you born ?')
age = 2022 - int(birth_year)
print(f'your age is {age} years old')

