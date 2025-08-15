mass = input("enter a mass in kilograms to calculate the energy\ninput: ")
while not mass.isnumeric(): mass = input("input valid number\ninput: ")

print(f"the energy of{int(mass)} is {int(mass)*(200000000 **2)}")
