pi=3.14159
def square():
    s=float(input("Side:"))
    print("Perimeter=",4*s," units")
    print("Area=",s*s," square units")
    return

def rectangle():
    l=float(input("Length:"))
    b=float(input("Breadth:"))
    print("Perimeter=",2*(l+b)," units")
    print("Area=",l*b," square units")
    return

def rhombus():
    s=float(input("Side:"))
    d1=float(input("Diagonal l:"))
    d2=float(input("Diagonal 2:"))
    print("Perimeter=",4*s," units")
    print("Area=",d1*d2/2," square units")
    return

def parallelogram():
    l=float(input("Length:"))
    b=float(input("Breadth:"))
    h=float(input("Height:"))
    print("Perimeter=",2*(l+b)," units")
    print("Area=",b*h," square units")
    return

def circle():
    r=float(input("Radius:"))
    print("Perimeter=",2*pi*r," units")
    print("Area=",pi*r*r," square units")
    return

def cube():
    s=float(input("Side:"))
    print("Circular Surface area=",4*s*s,"square units")
    print("Total Surface area=",6*s*s," square units")
    print("Volume=",s*s*s," cubit units")
    return

def cuboid():
    l=float(input("Length:"))
    b=float(input("Breadth:"))
    h=float(input("Height:"))
    print("Circular Surface area",2*(l+b)*h,"square units")
    print("Total Surface area=",2*(l*b + b*h + l*h)," square units")
    print("Volume=",l*b*h," cubit units")
    return

def cone():
    l=float(input("Slant Height:"))
    r=float(input("Radius:"))
    h=float(input("Height:"))
    print("Circular Surface area=",pi*r*l," square units")
    print("Total Surface area=",pi*r*(r+l)," square units")
    print("Volume=",pi*r*r*h/3," cubit units")
    return

def hemisphere():
    r=float(input("Radius:"))
    print("Circular Surface area=",2*pi*r*r," square units")
    print("Total Surface area=",3*pi*r*r," square units")
    print("Volume=",2*pi*r*r*r/3," cubit units")
    return

def sphere():
    r=float(input("Radius:"))
    print("Circular Surface area=",4*pi*r*r," square units")
    print("Total Surface area=",4*pi*r*r," square units")
    print("Volume=",4*pi*r*r*r/3," cubit units")
    return

def s_cylinder():
    r=float(input("Radius:"))
    h=float(input("Height:"))    
    print("Circular Surface area=",2*pi*r*h," square units")
    print("Total Surface area=",2*pi*r*(r+h)," square units")
    print("Volume=",pi*r*r*h," cubit units")
    return

def h_cylinder():
    r1=float(input("Outer Radius:"))
    r2=float(input("Inner Radius:"))
    h=float(input("Height:"))    
    print("Circular Surface area=",2*pi*(r1+r2)*h," square units")
    print("Total Surface area=",(2*pi*(r1+r2)*h)+(2*pi*(r1**2-r2**2))," square units")
    print("Volume=",pi*(r1**2-r2**2)*h," cubit units")
    return

num=int(input("Enter the number of students: "))
for i in range (1,num+1):
    dim=input("Enter the geometric dimension:")
    choice=""
    if(dim=="2D"):
        print("Menu: \n 1)Square \n 2)Rectangle \n 3)Rhombus \n 4)Parallelogram \n 5)Circle \n 6)Exit ")
        choice=input()
        if(choice=="Square"):
            square()
        elif(choice=="Rectangle"):
            rectangle()
        elif(choice=="Rhombus"):
            rhombus()
        elif(choice=="Parallelogram"):
            parallelogram()
        elif(choice=="Circle"):
            circle()
        elif(choice=="Exit"):
            break
        else:
            print("Wrong Input")
    elif(dim=="3D"):
        print("Menu: \n 1)Cube \n 2)Cuboid \n 3)Right Circular Cone \n 4)Hemisphere \n 5)Sphere \n 6)Solid Cylinder \n 7)Hollow Cylinder \n 8)Exit")
        choice=input()
        if(choice=="Cube"):
            cube()
        elif(choice=="Cuboid"):
            cuboid()
        elif(choice=="Right Circular Cone"):
            cone()
        elif(choice=="Hemisphere"):
            hemisphere()
        elif(choice=="Sphere"):
            sphere()
        elif(choice=="Solid Cylinder"):
            s_cylinder()
        elif(choice=="Hollow Cylinder"):
            h_cylinder()
        elif(choice=="Exit"):
            break
        else:
            print("Wrong Input")
    else:
        print("Wrong Input")
