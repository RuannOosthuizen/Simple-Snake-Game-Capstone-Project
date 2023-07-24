# Snake Game

This is a simple Snake Game implemented in Python using the Turtle graphics library. The game allows you to control a snake that moves around the screen to eat food and grow longer. The objective is to eat as much food as possible without colliding with the walls or the snake's own tail.

## How to Play

1. Run the Python script `snake_game.py`.
2. Use the arrow keys (Up, Down, Left, and Right) to control the movement of the snake.
3. Guide the snake to eat the food (indicated by a small square) that appears on the screen.
4. Each time the snake eats food, it will grow longer, and your score will increase.
5. The game ends if the snake collides with the walls or its own tail.
6. Close the game window by clicking on it after the game is over.

## Prerequisites

- Python 3.x
- The following Python libraries are required:
  - turtle
  - time

## Installation

1. Clone or download the repository.
2. Make sure you have Python 3.x installed on your system.
3. Install the required libraries using pip:

```bash
pip install turtle
```

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the `snake_game.py` file is located.
3. Run the script:

```bash
python snake_game.py
```

## Game Controls

- Use the arrow keys to control the snake's direction:
  - Up Arrow: Move the snake upwards
  - Down Arrow: Move the snake downwards
  - Left Arrow: Move the snake to the left
  - Right Arrow: Move the snake to the right

## Rules

- The snake moves automatically in the direction it is facing.
- The game ends if the snake collides with the boundaries (walls) of the screen.
- The game also ends if the snake collides with its own tail.
- Eating the food increases the score and the snake's length.
- The longer the snake gets, the more challenging it becomes to avoid collisions.

## Acknowledgments

The implementation of this Snake Game is based on a project developed as part of a Python programming course.

Enjoy playing the Snake Game! 🐍🍎



# Snake Class for Python Snake Game

This Python code defines a `Snake` class that is used to represent and control the snake in a simple Snake Game using the Turtle graphics library. The Snake class allows the snake to move around the screen, grow longer as it eats food, and change its direction based on user input.

## How to Use the Snake Class

1. Make sure you have the Turtle library installed. If you don't have it, you can install it using:

   ```bash
   pip install PythonTurtle
   ```

2. Create an instance of the `Snake` class to control the snake in your Snake Game. For example:

   ```python
   from turtle import Screen
   from snake import Snake

   # Set up the screen and other game elements
   screen = Screen()
   # ... (other code to set up the screen)

   # Create the Snake object
   snake = Snake()

   # Set up the key listeners to control the snake's direction
   screen.listen()
   screen.onkey(snake.up, "Up")
   screen.onkey(snake.down, "Down")
   screen.onkey(snake.left, "Left")
   screen.onkey(snake.right, "Right")

   # Start the game loop
   game_is_on = True
   while game_is_on:
       # Move the snake and other game elements
       # ... (other code to handle game logic)

   # Close the game window when the game is over
   screen.exitonclick()
   ```

## Constants

- `STARTING_POSITIONS`: A list of tuples representing the initial positions of the segments of the snake.
- `MOVE_DISTANCE`: An integer representing the distance in pixels that the snake moves in each step.

## Snake Class Methods

- `__init__(self)`: The constructor method that initializes the `Snake` object. It creates the snake's segments, sets the head, and assigns the initial direction.
- `create_snake(self)`: Creates the initial segments of the snake based on the `STARTING_POSITIONS` constant.
- `add_segment(self, position)`: Adds a new segment to the snake at the specified position.
- `extend(self)`: Extends the snake by adding a new segment at the end when it eats food.
- `move(self)`: Moves the snake forward in the current direction. The segments follow the previous segment's position, causing the entire snake to move.
- `up(self)`, `down(self)`, `left(self)`, `right(self)`: Methods to control the snake's direction. These methods update the snake's heading based on user input, but certain directions are restricted to prevent the snake from moving back onto itself.

## Acknowledgments

The implementation of this `Snake` class is based on a project developed as part of a Python programming course.



# Scoreboard Class for Python Snake Game

This Python code defines a `Scoreboard` class used to manage and display the score in a simple Snake Game using the Turtle graphics library. The `Scoreboard` class is responsible for updating and showing the current score, as well as displaying a "GAME OVER" message when the game ends.

## How to Use the Scoreboard Class

1. Make sure you have the Turtle library installed. If you don't have it, you can install it using:

   ```bash
   pip install PythonTurtle
   ```

2. Create an instance of the `Scoreboard` class to keep track of the score in your Snake Game. For example:

   ```python
   from turtle import Screen
   from scoreboard import Scoreboard

   # Set up the screen and other game elements
   screen = Screen()
   # ... (other code to set up the screen)

   # Create the Scoreboard object
   scoreboard = Scoreboard()

   # In the game loop, update the score when the snake eats food
   # ... (other code to handle game logic, including calling the following line when the snake eats food)
   scoreboard.increase_score()

   # When the game is over, display the "GAME OVER" message
   # ... (other code to handle game over conditions)
   scoreboard.game_over()

   # Close the game window when the game is over
   screen.exitonclick()
   ```

## Constants

- `ALIGNMENT`: A string constant representing the alignment of the score and "GAME OVER" text. It is set to "center" to center the text on the screen.
- `FONT`: A tuple constant representing the font style for displaying the score and "GAME OVER" text. It uses the Courier font with a size of 24 and normal weight.

## Scoreboard Class Methods

- `__init__(self)`: The constructor method that initializes the `Scoreboard` object. It sets up the initial score, color, position, and font for displaying the score.
- `update_scoreboard(self)`: Writes the current score on the screen using the specified alignment and font.
- `increase_score(self)`: Increases the score by 1 and updates the displayed score on the screen by calling `update_scoreboard()` after clearing the previous score.
- `game_over(self)`: Displays the "GAME OVER" message at the center of the screen when the game is over.

## Acknowledgments

The implementation of this `Scoreboard` class is based on a project developed as part of a Python programming course.



# Food Class for Python Snake Game

This Python code defines a `Food` class used to represent the food that the snake can eat in a simple Snake Game using the Turtle graphics library. The `Food` class is a subclass of the `Turtle` class and is responsible for displaying and refreshing the food at random positions on the screen.

## How to Use the Food Class

1. Make sure you have the Turtle library installed. If you don't have it, you can install it using:

   ```bash
   pip install PythonTurtle
   ```

2. Create an instance of the `Food` class to represent the food in your Snake Game. For example:

   ```python
   from turtle import Screen
   from food import Food

   # Set up the screen and other game elements
   screen = Screen()
   # ... (other code to set up the screen)

   # Create the Food object
   food = Food()

   # When the snake eats the food, refresh the position of the food
   # ... (other code to handle the snake eating food, including calling the following line)
   food.refresh()

   # Close the game window when the game is over
   screen.exitonclick()
   ```

## Food Class Methods

- `__init__(self)`: The constructor method that initializes the `Food` object. It sets up the appearance (shape, color, size) and speed of the food and calls the `refresh()` method to set its initial position.
- `refresh(self)`: Randomly sets a new position for the food on the screen. The new position is within the boundaries specified by `(-280, -280)` for the lower-left corner and `(280, 280)` for the upper-right corner of the screen.

## Acknowledgments

The implementation of this `Food` class is based on a project developed as part of a Python programming course.

Enjoy having the food appear at random positions for your Snake Game! 🍎🍏