import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []  # List to store all balls
        
        # Populate the contents list based on the input
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, n):
        new_hat = []  # List to store drawn balls
        if n >= len(self.contents):
            # If drawing more balls than available, return all balls
            new_hat = self.contents.copy()
            self.contents.clear()  # Empty the hat
        else:
            # Draw n balls randomly
            for _ in range(n):
                if self.contents:
                    ball = random.choice(self.contents)
                    self.contents.remove(ball)
                    new_hat.append(ball)
        return new_hat

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0  # Count of successful experiments

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)  # Create a deep copy of the hat for each experiment
        drawn_balls = hat_copy.draw(num_balls_drawn)  # Draw balls from the copy
    
        drawn_counts = {}  # Dictionary to count occurrences of each color
    
        # Count the occurrences of each color
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1

        success = True
        # Check if the drawn balls match or exceed the expected number of balls
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break
        
        if success:
            M += 1  # Increment successful experiment count

    # Return probability of success
    return M / num_experiments

# Example usage
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={'red':2, 'green':1}, num_balls_drawn=5, num_experiments=2000)

print(probability)
