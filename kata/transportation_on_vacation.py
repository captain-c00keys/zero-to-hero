def rental_car_cost(d):
  total = d * 40
  if d < 3:
    return total
  elif d < 7:
    return total - 20
  else:
    return total - 50