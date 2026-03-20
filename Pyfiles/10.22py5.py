import math

def basic_calculator():
    print("Welcome to use The Basic Arithmetic Calculator!")
    print("We support：+ (addition), - (subtraction), * (multiplication), / (division), ** (exponent), @ (the distance between two points on a XOY plane)")
    print("If exit the program, please press 'quit'.")
    
    while True:
        try:
            first_input = input("\nPlease enter the first number.（or enter 'quit' to exit）: ").strip()
            if first_input.lower() == 'quit':
                print("Thank you,bye!")
                break
            if first_input == '@':
                print("Error:input the right x, y coordinate of Point 1 on XOY plane")
                continue
            operator = input("Please print the operator symbol (+, -, *, /, **, @): ").strip()
            if operator.lower() == 'quit':
                print("Thank you,bye!")
                break
            if operator == '@':
                try:
                    x1 = float(first_input)
                    y1 = float(input("Please input the y coordinate of Point 1 on XOY plane:"))
                    x2 = float(input("Please input the x coordinate of Point 2 on XOY plane:"))
                    y2 = float(input("Please input the y coordinate of Point 2 on XOY plane:"))
                    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
                    print(f"The distance of coordinate({x1}, {y1}) and coordinate({x2}, {y2}) is: {distance:.2f}")
                    
                except ValueError:
                    print("Error:input the right coordinate!")
                continue
            second_input = input("Please input the second number!").strip()
            if second_input.lower() == 'quit':
                print("Thank you,bye!")
                break
            num1 = float(first_input)
            num2 = float(second_input)
            result = None
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: The divisor cannot be zero!")
                    continue
                result = num1 / num2
            elif operator == '**':
                result = num1 ** num2
            else:
                print(f"Error: Unsupported operator '{operator}'")
                continue
            print(f"result: {num1} {operator} {num2} = {result}")            
        except ValueError:
            print("Error:input the right number")
        except KeyboardInterrupt:
            print("\n\nThe program was interrupted by the user.")
            break
        except Exception as e:
            print(f"An unknown error occurred: {e}")

def calculate_distance(x1, y1, x2, y2):
    """Calculate the distance between two points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
if __name__ == "__main__":
    basic_calculator()
