import math

degree = 45

rad = degree * math.pi/180
print(rad)
print(math.radians(45))

small_pizza = 0.22
big_pizza = 0.27
family_pizza =0.38
small_pizza_price = 11.50
big_pizza_prize = 15.60
family_pizza_prize = 22

small_pizza_field = math.pi * small_pizza**2
big_pizza_field = math.pi * big_pizza**2
family_pizza_field = math.pi * family_pizza**2

print(f'cena za metr kwadratowy pizzy:{small_pizza_price/small_pizza_field}')