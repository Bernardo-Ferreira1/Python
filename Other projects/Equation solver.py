from abc import ABC, abstractmethod  # Import abstract base class (ABC) and abstractmethod to enforce method implementation in subclasses
import re  # Import regular expressions for string manipulation


class Equation(ABC):  # Define an abstract base class for equations
    degree: int  # Expected degree of the equation
    type: str  # Type of the equation (e.g., Linear, Quadratic)
  
    def __init__(self, *args):  # Constructor to initialize equation coefficients
        if (self.degree + 1) != len(args):  # Ensure the number of arguments matches the expected degree + 1
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        if any(not isinstance(arg, (int, float)) for arg in args):  # Ensure all coefficients are numbers
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        if args[0] == 0:  # Highest-degree coefficient must be nonzero
            raise ValueError("Highest degree coefficient must be different from zero")
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}  # Store coefficients in a dictionary

    def __init_subclass__(cls):  # Enforce required attributes in subclasses
        if not hasattr(cls, "degree"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'"
            )
        if not hasattr(cls, "type"):
            raise AttributeError(
                f"Cannot create '{cls.__name__}' class: missing required attribute 'type'"
            )

    def __str__(self):  # Convert the equation to a readable string format
        terms = []
        for n, coefficient in self.coefficients.items():  # Iterate over coefficients
            if not coefficient:  # Skip zero coefficients
                continue
            if n == 0:
                terms.append(f'{coefficient:+}')  # Constant term
            elif n == 1:
                terms.append(f'{coefficient:+}x')  # Linear term
            else:
                terms.append(f"{coefficient:+}x**{n}")  # Higher-degree terms
        equation_string = ' '.join(terms) + ' = 0'  # Format as equation
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))  # Remove unnecessary '+' and '1x' formatting

    @abstractmethod
    def solve(self):  # Abstract method to solve the equation
        pass
        
    @abstractmethod
    def analyze(self):  # Abstract method to analyze the equation properties
        pass


class LinearEquation(Equation):  # Subclass for linear equations (ax + b = 0)
    degree = 1  # Define equation degree
    type = 'Linear Equation'  # Define equation type
    
    def solve(self):  # Solve the linear equation
        a, b = self.coefficients.values()  # Extract coefficients
        x = -b / a  # Solve for x
        return [x]

    def analyze(self):  # Analyze slope and y-intercept
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept': intercept}


class QuadraticEquation(Equation):  # Subclass for quadratic equations (ax^2 + bx + c = 0)
    degree = 2  # Define equation degree
    type = 'Quadratic Equation'  # Define equation type

    def __init__(self, *args):  # Initialize quadratic equation
        super().__init__(*args)  # Call superclass constructor
        a, b, c = self.coefficients.values()  # Extract coefficients
        self.delta = b**2 - 4 * a * c  # Compute discriminant (delta)

    def solve(self):  # Solve the quadratic equation
        if self.delta < 0:  # No real roots if delta is negative
            return []
        a, b, _ = self.coefficients.values()
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)  # Compute first root
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)  # Compute second root
        if self.delta == 0:  # If delta is zero, only one root exists
            return [x1]
        return [x1, x2]

    def analyze(self):  # Analyze vertex and concavity
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)  # Compute x-coordinate of vertex
        y = a * x**2 + b * x + c  # Compute y-coordinate of vertex
        if a > 0:
            concavity = 'upwards'  # Parabola opens upwards
            min_max = 'min'  # Vertex is a minimum
        else:
            concavity = 'downwards'  # Parabola opens downwards
            min_max = 'max'  # Vertex is a maximum
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}


def solver(equation):  # Function to solve and analyze an equation
    if not isinstance(equation, Equation):  # Ensure input is an Equation instance
        raise TypeError("Argument must be an Equation object")

    output_string = f'\n{equation.type:-^24}'  # Format equation type header
    output_string += f'\n\n{equation!s:^24}\n\n'  # Display equation
    output_string += f'{"Solutions":-^24}\n\n'  # Header for solutions
    results = equation.solve()  # Solve equation
    match results:
        case []:
            result_list = ['No real roots']  # Handle no real roots
        case [x]:
            result_list = [f'x = {x:+.3f}']  # Format single root
        case [x1, x2]:
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']  # Format two roots
    for result in result_list:
        output_string += f'{result:^24}\n'
    output_string += f'\n{"Details":-^24}\n\n'  # Header for details
    details = equation.analyze()  # Analyze equation properties
    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [f'slope = {slope:>16.3f}', f'y-intercept = {intercept:>10.3f}']  # Linear equation details
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            coord = f'({x:.3f}, {y:.3f})'  # Format vertex
            details_list = [f'concavity = {concavity:>12}', f'{min_max} = {coord:>18}']  # Quadratic equation details
    for detail in details_list:
        output_string += f'{detail}\n'
    return output_string

lin_eq = LinearEquation(2, 3)  # Example linear equation
quadr_eq = QuadraticEquation(1, 2, 1)  # Example quadratic equation
print(solver(quadr_eq))  # Print quadratic equation solution and analysis