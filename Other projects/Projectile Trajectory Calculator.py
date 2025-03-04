import math  # Import the math library for mathematical calculations

# Define global constants
GRAVITATIONAL_ACCELERATION = 9.81  # Gravitational acceleration (m/s²)
PROJECTILE = "∙"  # Symbol representing the projectile in the matrix
x_axis_tick = "T"  # Symbol representing the X-axis in the matrix
y_axis_tick = "⊣"  # Symbol representing the Y-axis in the matrix

# Class representing a projectile in motion
class Projectile:
    __slots__ = ('__speed', '__height', '__angle')  # Optimizes memory by limiting attributes

    def __init__(self, speed, height, angle):
        """Initializes a projectile with speed, height, and angle."""
        self.__speed = speed  # Initial speed
        self.__height = height  # Initial height
        self.__angle = math.radians(angle)  # Converts angle to radians

    def __str__(self):
        """Returns a string representation of the projectile."""
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        """Calculates the total horizontal displacement of the projectile."""
        horizontal_component = self.__speed * math.cos(self.__angle)  # Horizontal velocity component
        vertical_component = self.__speed * math.sin(self.__angle)  # Vertical velocity component
        squared_component = vertical_component ** 2  # Squared vertical component
        gh_component = 2 * GRAVITATIONAL_ACCELERATION * self.__height  # Potential energy converted to kinetic energy
        sqrt_component = math.sqrt(squared_component + gh_component)  # Square root of the internal term
        
        # Formula for calculating projectile horizontal displacement
        return horizontal_component * (vertical_component + sqrt_component) / GRAVITATIONAL_ACCELERATION

    def __calculate_y_coordinate(self, x):
        """Calculates the Y coordinate for a given X based on the motion equation."""
        height_component = self.__height  # Initial height
        angle_component = math.tan(self.__angle) * x  # Angle-based term
        acceleration_component = GRAVITATIONAL_ACCELERATION * x ** 2 / (
                2 * self.__speed ** 2 * math.cos(self.__angle) ** 2)  # Gravity acceleration term

        y_coordinate = height_component + angle_component - acceleration_component  # Trajectory equation
        return y_coordinate

    def calculate_all_coordinates(self):
        """Calculates all (x, y) coordinates of the projectile along its trajectory."""
        return [
            (x, self.__calculate_y_coordinate(x))
            for x in range(math.ceil(self.__calculate_displacement()))  # Iterates up to the total displacement
        ]

    # Getter methods for private attributes
    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        return round(math.degrees(self.__angle))  # Returns the angle in degrees (rounded)

    @property
    def speed(self):
        return self.__speed

    # Setter methods for private attributes
    @height.setter
    def height(self, n):
        self.__height = n

    @angle.setter
    def angle(self, n):
        self.__angle = math.radians(n)  # Converts degrees to radians before storing

    @speed.setter
    def speed(self, s):
       self.__speed = s

    def __repr__(self):
        """Official representation of the object for debugging."""
        return f'{self.__class__}({self.speed}, {self.height}, {self.angle})'

# Class responsible for drawing the projectile's trajectory graph
class Graph:
    __slots__ = ('__coordinates')  # Reduces memory usage

    def __init__(self, coord):
        """Initializes the graph with a list of (x, y) coordinates."""
        self.__coordinates = coord

    def __repr__(self):
        """Object representation for debugging."""
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        """Creates a formatted table with the projectile's coordinates."""
        table = '\n  x      y\n'  # Table header
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'  # Right-aligned formatting for better visualization

        return table

    def create_trajectory(self):
        """Creates a graphical representation of the projectile's trajectory."""
        # Round the coordinates to integers
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        # Determine the limits of the graph
        x_max = max(rounded_coords, key=lambda i: i[0])[0]  # Maximum X value
        y_max = max(rounded_coords, key=lambda j: j[1])[1]  # Maximum Y value

        # Create an empty matrix filled with spaces
        matrix_list = [[" " for _ in range(x_max + 1)] for _ in range(y_max + 1)]

        # Place the trajectory points in the matrix
        for x, y in rounded_coords:
            matrix_list[-1 - y][x] = PROJECTILE  # "-1 - y" inverts the Y-axis so (0,0) is at the bottom left

        # Convert the list matrix into a list of strings
        matrix = ["".join(line) for line in matrix_list]

        # Add the Y-axis markers at the start of each row
        matrix_axes = [y_axis_tick + row for row in matrix]

        # Add the X-axis row at the bottom of the graph
        matrix_axes.append(" " + x_axis_tick * (len(matrix[0])))

        # Combine all lines into a formatted string
        graph = "\n" + "\n".join(matrix_axes) + "\n"

        return graph

# Helper function to create a projectile, compute its trajectory, and print the results
def projectile_helper(speed, height, angle):
    projectile = Projectile(speed, height, angle)  # Create a Projectile object
    coordinates = projectile.calculate_all_coordinates()  # Calculate trajectory coordinates
    graph = Graph(coordinates)  # Create a graph with these coordinates

    # Print projectile details
    print(projectile)
    # Print coordinate table
    print(graph.create_coordinates_table())   
    # Print trajectory graph
    print(graph.create_trajectory())    

# Test the function with a projectile of 10 m/s speed, 3 m height, and 60° angle
projectile_helper(10, 3, 60)
