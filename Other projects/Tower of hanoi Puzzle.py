def move(n, source, auxiliary, target):
    if n > 0:
        # move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)
        
        # display starting configuration
        print(rods, '\n')


NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
    # move the nth disk from source to target
    target.append(source.pop())
        
    # display our progress
    print(A, B, C, '\n')
        
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)

"""
-----------------Resolução sem usar recursividade---------------------------------------------

NUMBER_OF_DISKS = 3  # Number of disks in the Tower of Hanoi problem
number_of_moves = 2**NUMBER_OF_DISKS - 1  # Total number of moves required to solve the puzzle
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),  # Source rod initialized with disks in descending order
    'B': [],  # Auxiliary rod starts empty
    'C': []   # Target rod starts empty
}

def make_allowed_move(rod1, rod2):
    
    #Perform an allowed move between two rods.
    
   # Parameters:
      #  rod1 (str): The first rod involved in the move.
     #   rod2 (str): The second rod involved in the move.
    
    forward = False  # Flag to determine the direction of the move

    # Determine if moving a disk from rod1 to rod2 is allowed
    if not rods[rod2]:  # If rod2 is empty, the move is allowed
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:  # Smaller disk on top of larger is allowed
        forward = True

    # Execute the move in the allowed direction
    if forward:
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        rods[rod2].append(rods[rod1].pop())  # Move the top disk from rod1 to rod2
    else:
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        rods[rod1].append(rods[rod2].pop())  # Move the top disk from rod2 to rod1

    # Display the current state of the rods after the move
    print(rods, '\n')

def move(n, source, auxiliary, target):
    
    #Simulate the Tower of Hanoi solution using iterative moves between rods.
    
   # Parameters:
     #   n (int): The number of disks.
    #    source (str): The source rod.
     #   auxiliary (str): The auxiliary rod.
      #  target (str): The target rod.
  
    # Display the initial configuration of the rods
    print(rods, '\n')

    # Loop through all required moves
    for i in range(number_of_moves):
        remainder = (i + 1) % 3  # Determine the move sequence based on the iteration number

        # Handle moves based on the sequence and whether n is even or odd
        if remainder == 1:  # First type of move
            if n % 2 != 0:  # If n is odd
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            else:  # If n is even
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        elif remainder == 2:  # Second type of move
            if n % 2 != 0:  # If n is odd
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            else:  # If n is even
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        elif remainder == 0:  # Third type of move
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)
"""