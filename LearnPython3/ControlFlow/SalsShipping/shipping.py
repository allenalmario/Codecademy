weight = 41.5

# ground shipping
if weight <= 2:
  print("Cost: " + str(1.50 * weight + 20))
elif weight <= 6:
  print("Cost: " + str(3 * weight + 20))
elif weight <= 10:
  print("Cost: " + str(4 * weight + 20))
elif weight > 10:
  print("Cost: " + str(4.75 * weight + 20))

premium_shipping = 125
print(premium_shipping)

# drone shipping
if weight <= 2:
  print("Cost: " + str(4.50 * weight))
elif weight <= 6:
  print("Cost: " + str(9 * weight))
elif weight <= 10:
  print("Cost: " + str(12 * weight))
elif weight > 10:
  print("Cost: " + str(14.25 * weight))