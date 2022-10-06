import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')

#Graph setup
ax.set_title("Boppin Graph")

ax.set_xlabel("Width of Boppin")
ax.set_ylabel("Magnitude of Boppin")
ax.set_zlabel("Amount of 'g's ")

#Plot points from text file
with open("Boppinpoints.txt", "r") as f:
    line = f.readline()
    y,x,z = line.split(',')
    y = float(y)
    x = float(x)        
    z = float(z)
    ax.scatter(x,y,z)
    for line in f:
        y,x,z = line.split(',')
        y = float(y)
        x = float(x)        
        z = float(z)
        ax.scatter(x,y,z)



#Create new user points 
newpoint = input("Do you want to create a new point? (Y/N)")

while newpoint == "Y" :
    newy = int(input("What would you like the Y axis to be?"))
    newx = int(input("What would you like the X axis to be?"))
    newz = int(input("What would you like the Z axis to be?"))
    ax.scatter(newx, newy, newz)

    with open("Boppinpoints.txt", "a") as f:
        f.write(str(newy) + "," + str(newx) + "," + str(newz) + "\n")

    newpoint = input("Do you want to create a new point? (Y/N)")



plt.show()