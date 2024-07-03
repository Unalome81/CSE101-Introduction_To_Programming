import A1_implement
import math
def test_matmul(A, B, true_C):
    C_out=A1_implement.matmul(A, B)
    try:
        assert C_out!=true_C, "Test case passed"
        assert C_out==true_C, "Test case failed"
    except AssertionError as msg:
        print(msg)

def test_scale(x, y, z, sx, sy, sz, true_x, true_y, true_z):
    x_out, y_out, z_out, bin=A1_implement.scale(x, y, z, sx, sy, sz)
    try:
        assert not (math.fabs(x_out-true_x)<=0.01 and math.fabs(y_out-true_y)<=0.01 and math.fabs(z_out-true_z)<=0.01), "Test case passed"
        assert math.fabs(x_out-true_x)<=0.01 and math.fabs(y_out-true_y)<=0.01 and math.fabs(z_out-true_z)<=0.01, "Test case failed"
    except AssertionError as msg:
        print(msg)

def test_translate(x, y, z, tx, ty, tz, true_x, true_y, true_z):
    x_out, y_out, z_out, bin=A1_implement.translate(x, y, z, tx, ty, tz)
    try:
        assert not (math.fabs(x_out-true_x)<=0.01 and math.fabs(y_out-true_y)<=0.01 and math.fabs(z_out-true_z)<=0.01), "Test case passed"
        assert math.fabs(x_out-true_x)<=0.01 and math.fabs(y_out-true_y)<=0.01 and math.fabs(z_out-true_z)<=0.01, "Test case failed"
    except AssertionError as msg:
        print(msg)

def test_rotate(x, y, z, axis, phi, true_x, true_y, true_z):
    x_out, y_out, z_out, bin=A1_implement.rotate(x, y, z, axis, phi)
    try:
        assert not (math.fabs(x_out-true_x)<=0.01 and math.fabs(y_out-true_y)<=0.01 and math.fabs(z_out-true_z)<=0.01), "Test case passed"
        assert math.fabs(x_out-true_x)<=0.01 and math.fabs(y_out-true_y)<=0.01 and math.fabs(z_out-true_z)<=0.01, "Test case failed"
    except AssertionError as msg:
        print(msg)

ch=-1
while ch!=9:
    print("Enter 1 to test matmul function using sample inputs: ")
    print("Enter 2 to test scale function using sample inputs: ")
    print("Enter 3 to test translate function using sample inputs: ")
    print("Enter 4 to test rotate function using sample inputs: ")
    print("Enter 5 to test matmul function using user input: ")
    print("Enter 6 to test scale function using user input: ")
    print("Enter 7 to test translate function using user input: ")
    print("Enter 8 to test rotate function using user input: ")
    print("Enter 9 to exit")
    ch=int(input())

    if ch==1:
        def inner_matmul():
            print("For AB=C, inputs are as follows:")
            print("A= ", *A[0], "\n   ", *A[1], "\n   ", *A[2], "\n   ", *A[3])
            print("B= ", B[0], "\n   ", B[1], "\n   ", B[2], "\n   ", B[3])
            print("C= ", C[0], "\n   ", C[1], "\n   ", C[2], "\n   ", C[3])
            test_matmul(A,B,C)

        print("Sample cases for function \"matmul\": ")
        print("\nTest Case 1:")
        A=[[1, 1, 2, 2], [2, 2, 3, 3], [3, 3, 4, 4], [4, 4, 5, 5]]
        B=[1, 2, 3, 4]
        C=[17, 27, 37, 47]
        inner_matmul()
        
        print("\nTest Case 2:")
        A=[[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]
        B=[1, 0, 1, 1]
        C=[8, 11, 14, 17]
        inner_matmul()
        
        print("\nTest Case 3:")
        A=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        B=[1, 2, 3, 4]
        C=[0, 0, 0, 0]
        inner_matmul()
        
        print("\nTest Case 4:")
        A=[[1, -1, 2, -2], [2, -2, -3, 3], [3, -3, 4, -4], [4, -4, -5, 5]]
        B=[24, 31, 41, 19]
        C=[37, -80, 67, -138]
        inner_matmul()
        
        print("\nTest Case 5:")
        A=[[0.1, 12, 2, 23], [3, 34, 0.4, 45], [5, 56, 0.6, 67], [7, 78, 8, 0.89]]
        B=[-1, 4, 5, 1]
        C=[80.9, 180, 289, 345.89]
        inner_matmul()
    
    elif ch==2:
        def inner_scale():
            print("Inputs: ", "\nx=", x ,", y=", y ,", z=", z , "\nsx=", sx , ", sy=", sy , ", sz=", sz, "\ntrue_x=", ox , ", true_y=", oy , ", true_z=", oz)
            test_scale(x, y, z, sx, sy, sz, ox, oy, oz)

        print("Sample cases for function \"scale\": ")
        print("\nTest Case 1:")
        x, y, z, sx, sy, sz, ox, oy, oz = 1, 2, 3, 1, 2, 3, 1, 4, 9
        inner_scale()      
       
        print("\nTest Case 2:")
        x, y, z, sx, sy, sz, ox, oy, oz = 1, 9, 2, 0, 0, 0, 0, 0, 0
        inner_scale()    
       
        print("\nTest Case 3:")
        x, y, z, sx, sy, sz, ox, oy, oz = 2, 7, 3, 1, 1, 1, 2, 7, 3
        inner_scale()    
       
        print("\nTest Case 4:")
        x, y, z, sx, sy, sz, ox, oy, oz = 1.1, 2.2, 3.3, 1.1, 2.2, 3.3, 1.21, 4.84, 10.89
        inner_scale()    
        
        print("\nTest Case 5:")        
        x, y, z, sx, sy, sz, ox, oy, oz = 3.1, 5.2, 9.3, -2, -3, -1, -6.2, -15.6, -9.3
        inner_scale()    
    
    elif ch==3:
        def inner_translate():
            print("Inputs: ", "\nx=", x ,", y=", y ,", z=", z , "\ntx=", tx , ", ty=", ty , ", tz=", tz, "\ntrue_x=", ox , ", true_y=", oy , ", true_z=", oz)
            test_translate(x, y, z, tx, ty, tz, ox, oy, oz)

        print("Sample cases for function \"translate\": ")
        print("\nTest Case 1:")
        x, y, z, tx, ty, tz, ox, oy, oz = 1, 2, 3, 1, 2, 3, 2, 4, 6
        inner_translate()        
       
        print("\nTest Case 2:")
        x, y, z, tx, ty, tz, ox, oy, oz = 1, 2, 3, 1, 1, 1, 2, 3, 4
        inner_translate()        
        
        print("\nTest Case 3:")
        x, y, z, tx, ty, tz, ox, oy, oz = 1, 2, 3, 0, 0, 0, 1, 2, 3
        inner_translate() 
        
        print("\nTest Case 4:")
        x, y, z, tx, ty, tz, ox, oy, oz = 101, 212, 313, 100, 200, 300, 201, 412, 613
        inner_translate() 
       
        print("\nTest Case 5:")
        x, y, z, tx, ty, tz, ox, oy, oz = 1, 1, 1, -0.1, -0.2, -0.3, 0.9, 0.8, 0.7
        inner_translate() 
    
    elif ch==4:
        def inner_rotate():
            print("Inputs: ", "\nx=", x ,", y=", y ,", z=", z , "\naxis=", axis,"\nphi=", phi, "\ntrue_x=", ox , ", true_y=", oy , ", true_z=", oz)
            test_rotate(x, y, z, axis, phi, ox, oy, oz)

        print("Sample cases for function \"rotate\": ")
        print("\nTest Case 1:")
        x, y, z, axis, phi, ox, oy, oz = 1, 2, 3, 'X', 90, 1, -2.99, 2.00
        inner_rotate()
       
        print("\nTest Case 2:")
        x, y, z, axis, phi, ox, oy, oz = 4, 5, 6, 'X', 45, 4, -0.70, 7.78
        inner_rotate()
        
        print("\nTest Case 3:")
        x, y, z, axis, phi, ox, oy, oz = 2.1, 1.3, 1.7, 'Y', 27.5, 2.64, 1.30, 0.53
        inner_rotate()
       
        print("\nTest Case 4:")
        x, y, z, axis, phi, ox, oy, oz = 3, 6, 9, 'Z', 360, 3, 6, 9
        inner_rotate()
        
        print("\nTest Case 5:")
        x, y, z, axis, phi, ox, oy, oz = 45.61, 23.16, 11.22, 'Z', 277, 28.54, -42.44, 11.22
        inner_rotate()
   
    elif ch==5:
        A=[]
        B=[]
        C=[]
        print("Enter the 4 cross 4 input matrix: ")        
        for i in range(4):
            A.append([float(i) for i in input().split()])
        B=[float(i) for i in input("Enter the 4 cross 1 input matrix: ").split()]    
        C=[float(i) for i in input("Enter the 4 cross 1 output matrix: ").split()]   
        test_matmul(A, B, C)
    
    elif ch==6:
        x, y, z= [float (i) for i in input("Enter x , y, z: ").split()]
        sx, sy, sz= [float (i) for i in input("Enter sx, sy, sz: ").split()]
        ox, oy, oz= [float (i) for i in input("Enter the 3 output values: ").split()]
        test_scale(x, y, z, sx, sy, sz, ox, oy, oz)
    
    elif ch==7:
        x, y, z= [float (i) for i in input("Enter x , y, z: ").split()]
        tx, ty, tz= [float (i) for i in input("Enter tx, ty, tz: ").split()]
        ox, oy, oz= [float (i) for i in input("Enter the 3 output values: ").split()]
        test_translate(x, y, z, tx, ty, tz, ox, oy, oz)
    
    elif ch==8:
        x, y, z= [float (i) for i in input("Enter X , Y, Z: ").split()]
        axis=float(input("Enter the axis of rotation: "))  
        phi=float(input("Enter the angle of rotation (in degrees): "))
        ox, oy, oz= [float (i) for i in input("Enter the 3 output values: ").split()]
        test_rotate(x, y, z, axis, phi, ox, oy, oz)
    
    elif ch==9:
        print("Program Terminated")
    
    if ch!=9:
        pause=input("\nEnter any alphanumeric value to continue: ")