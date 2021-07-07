altitude = int(input("Enter the altitude of the plane: "))

if altitude <= 1000:
  print("safe to land")
elif altitude >1000 and altitude <=50:
  print("Bring down to 1000 ft")
elif altitude > 5000:
  print("Turn Around")
