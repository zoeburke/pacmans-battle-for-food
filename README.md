# Pacman Game

This is a simple Pacman game implemented using Python and Pygame. The game includes a Pacman character, an enemy, and food items that Pacman and the enemy chase.

## Project Structure

```
123718179_assignment_1/
│
├── pacman.py
├── enemy.py
├── food.py
├── main.py
└── README.md
```

- `pacman.py`: Contains the `Pacman` class with methods for drawing, moving, and relocating Pacman.
- `enemy.py`: Contains the `Enemy` class with methods for drawing, moving, and relocating the enemy.
- `food.py`: Contains the `Food` class with methods for drawing and relocating the food.
- `main.py`: The main file that runs the game, handles user input, and checks for collisions.

## Setup Instructions

1. **Install Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Pygame**: Install the Pygame library using pip:
   ```bash
   pip install pygame
   ```

3. **Clone the Repository**: Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/123718179_assignment_1.git
   ```

4. **Navigate to the Project Directory**:
   ```bash
   cd 123718179_assignment_1
   ```

## Running the Game

To run the game, execute the `main.py` file:
```bash
python main.py
```

## Game Controls

- **Arrow Keys**: Use the arrow keys to move Pacman in the desired direction.
- **Quit**: Close the game window to quit the game.

## How the Game Works

- Pacman moves based on user input.
- The enemy chases the food.
- If Pacman collides with the food, both Pacman and the food are relocated to random positions.
- If the enemy collides with the food, both the enemy and the food are relocated to random positions.
- If the enemy collides with Pacman, both the enemy and Pacman are relocated to random positions.
