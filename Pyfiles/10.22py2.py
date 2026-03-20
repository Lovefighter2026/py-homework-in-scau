base = float(input('Please input the base of the right triangle: '))
height = float(input('Please input the height of the right triangle: '))

if base <= 0 or height <= 0:
    print("Error: Base and height must be positive numbers!")
else:
    hypotenuse = (base ** 2 + height ** 2) ** 0.5
    
    print(Right Triangle Side Lengths:)
    print(base:)
    print(height:)
print(hypotenuse；)
