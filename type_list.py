# create a list

favorite_colors = ['red', 'black', 'yellow', 'green', 'pink']

# 데이터를 다룬다. manipulate data ..> CRUD
# Create, insert
favorite_colors.append('tan')
print(favorite_colors)
# Read
print(favorite_colors[1])
print(favorite_colors[2:5])
print(favorite_colors[5])
# Delete
favorite_colors.remove('black')

print(favorite_colors)
