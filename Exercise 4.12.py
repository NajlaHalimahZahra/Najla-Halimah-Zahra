my_foods =['cheesecake', 'pizza', 'roti bakar', 'dimsum']  
friend_foods = my_foods[:]

my_foods.append('ice cream')
friend_foods.append('pasta')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)