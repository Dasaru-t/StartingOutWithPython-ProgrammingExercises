# 14. Kinetic Energy

def main():
  #get values mass & velocity
  mass = float(input("Enter mass of the object(in kilograms): "))
  velocity = float(input("Enter velocity of the object(in meters per second): "))

  #calculate kinetic energy
  ke = kinetic_energy(mass, velocity)

  #display results
  print("kinetic energy :",format(ke,".2f"),"joule")

# The kinetic_energy function accepts mass & velocity
# as arguments and returns kinetic energy
def kinetic_energy(mass, velocity):
  ke = (1/2)*mass*(velocity**2)
  return ke

main()