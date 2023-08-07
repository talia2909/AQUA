# Animal Simulator 🐾

## Description
This project introduces a simple Python-based simulator for animals. With the `Animal` class, users can model various properties and behaviors of an animal, such as its name, age, position, and direction.

# What I Learned 📚

Throughout the development of this Animal Simulator project, several key concepts and skills were reinforced:

1. **Object-Oriented Programming (OOP)**: This project served as a practical introduction to OOP principles. I learned how to design and implement classes, create objects, and use methods to interact with those objects.

2. **Attributes and Methods**: I gained a deeper understanding of class attributes and methods, and how they can be used to encapsulate the state and behavior of an object.

3. **Python Basics**: Through coding the simulator, I honed my Python skills, especially in terms of variable management, control structures, and class interactions.

4. **Problem Solving**: Simulating an animal required breaking down complex behaviors into simpler, manageable code chunks. This exercise enhanced my analytical thinking and problem-solving skills.

5. **State Management**: Keeping track of the animal's state (e.g., age, food level) taught me the importance of state management in software development.

6. **Documentation and Code Readability**: Writing a README and organizing the code in a clear and coherent manner highlighted the importance of documentation and making code readable for others (and for my future self).

7. **Project Organization**: Structuring the project and organizing code in a modular way was a crucial lesson, ensuring scalability and maintainability of the codebase.


## Features

- **Attributes**:
  - `alive`: Determines if the animal is alive or not.
  - `width`: Specifies the width of the animal.
  - `height`: Specifies the height of the animal.
  - `food`: Tracks the amount of food the animal has.
  - `name`: The name of the animal.
  - `age`: The age of the animal.
  - `x` and `y`: The animal's position coordinates.
  - `directionH`: The direction the animal is facing (0 for left, 1 for right).

- **Methods**:
  - `__str__`: Returns a formatted string with details about the animal.
  - `get_food`: Returns the current amount of food.
  - `get_age`: Returns the age of the animal.
  - `dec_food`: Decreases the food by 1.
  - `inc_age`: Increases the age by 1.
  - `right`: Moves the animal to the right.
  - `left`: Moves the animal to the left.
  - `get_position`: Returns the current position coordinates of the animal.
  - (and more...)

## Installation

To use the `Animal` class in your project, simply import it:
```python
from Animal import Animal
```

## Usage

Here's a basic example of how to create an animal and interact with its properties:

```python
# Create a new animal named "Lion" aged 5 years
lion = Animal("Lion", 5, 0, 0, 1)

# Get the age of the lion
print(lion.get_age())  # Output: 5

# Move the lion to the right
lion.right()

# Get the current position of the lion
print(lion.get_position())  # Output: (-1, 0)
```
