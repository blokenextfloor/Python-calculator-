def calculate():
    while True:
        try:
            print("\n--- Simple Calculator with Advanced Features ---")
            print("Available Operations:")
            print("1. Basic: +, -, *, /")
            print("2. Advanced: cos, tan (approximations)")
            print("3. Graph: Display y = f(x) as a table")
            
            # Ask for operation type
            operation_type = input("Choose an operation type (basic/advanced/graph): ").strip().lower()

            if operation_type == "basic":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                operation = input("Enter the operation (+, -, *, /): ")

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed!")
                        continue
                    result = num1 / num2
                else:
                    print("Error: Invalid operation selected!")
                    continue

                print(f"Result: {num1} {operation} {num2} = {result}")

            elif operation_type == "advanced":
                print("Advanced Functions (using approximations):")
                print("1. Cosine (cos)")
                print("2. Tangent (tan)")
                func = input("Choose a function (cos/tan): ").strip().lower()
                angle = float(input("Enter the angle in degrees: "))

                # Convert angle to radians manually
                radians = angle * 3.141592653589793 / 180

                if func == "cos":
                    # Approximation of cosine using Taylor series
                    result = 1 - (radians ** 2) / 2 + (radians ** 4) / 24
                    print(f"Cos({angle}°) ≈ {result:.6f}")
                elif func == "tan":
                    # Approximation of tangent using sine/cosine ratio
                    sin_approx = radians - (radians ** 3) / 6 + (radians ** 5) / 120
                    cos_approx = 1 - (radians ** 2) / 2 + (radians ** 4) / 24
                    if cos_approx == 0:
                        print("Error: Tangent is undefined for this angle!")
                        continue
                    result = sin_approx / cos_approx
                    print(f"Tan({angle}°) ≈ {result:.6f}")
                else:
                    print("Error: Invalid function selected!")
                    continue

            elif operation_type == "graph":
                print("Graphing Function: y = f(x) as a table")
                print("Supported functions: sin, cos, tan (approximations)")
                func = input("Enter the function (sin/cos/tan): ").strip().lower()
                start = int(input("Enter the start of the x range: "))
                end = int(input("Enter the end of the x range: "))
                step = int(input("Enter the step size: "))

                print("\n--- Table of Values ---")
                print(f"{'x':>5} | {'y':>10}")
                print("-" * 18)
                for x in range(start, end, step):
                    # Convert x to radians manually
                    radians = x * 3.141592653589793 / 180

                    if func == "sin":
                        # Approximation of sine using Taylor series
                        y = radians - (radians ** 3) / 6 + (radians ** 5) / 120
                    elif func == "cos":
                        # Approximation of cosine using Taylor series
                        y = 1 - (radians ** 2) / 2 + (radians ** 4) / 24
                    elif func == "tan":
                        # Approximation of tangent using sine/cosine ratio
                        sin_approx = radians - (radians ** 3) / 6 + (radians ** 5) / 120
                        cos_approx = 1 - (radians ** 2) / 2 + (radians ** 4) / 24
                        if cos_approx == 0:
                            print(f"{x:>5} | {'Undefined':>10}")
                            continue
                        y = sin_approx / cos_approx
                    else:
                        print("Error: Invalid function selected!")
                        break

                    print(f"{x:>5} | {y:>10.4f}")

            else:
                print("Error: Invalid operation type selected!")
                continue

        except ValueError:
            print("Error: Please enter valid numbers!")
            continue

        # Ask user to exit or continue
        choice = input("\nDo you want to perform another operation? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Exiting the program. Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    calculate()
