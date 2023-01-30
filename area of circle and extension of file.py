#Area of circle
r = float(input("Radius of circle:"))
area = (22/7)*r**2
print("Area of circle is",area)


#Extension of a file
a = input("Input the Filename:")
ext = a.split(".")
print("The extension of file is:" + repr(ext[-1]))
