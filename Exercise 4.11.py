pizzas = ['pepperoni', 'cheese', 'meat lover', ]
pizza_milik_teman = pizzas[:]

pizzas.append('veggie')
pizza_milik_teman.append('hawaiian')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
    
print("\nMy friend's favorite pizzas are:")
for pizza in pizza_milik_teman:
    print(pizza)