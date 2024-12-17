
# **Genetic Algorithm for Game Optimization**

This project implements a **Genetic Algorithm** to optimize player actions in a game-like environment. The algorithm evolves sequences of actions to maximize the player's performance across game levels using principles of natural selection.

---

## **Project Overview**

The Genetic Algorithm is applied to solve an optimization problem where the goal is to navigate a game level efficiently. The process involves generating a population of action sequences, evaluating their fitness, applying selection, crossover, and mutation operations, and iterating over multiple generations to improve solutions.

---

## **Key Features**

- **Game Environment**:  
   - Levels are represented as strings containing obstacles (`G`, `M`, `L`) and empty spaces (`_`).  
   - Actions include **jump**, **duck**, or **move forward**.  

- **Genetic Algorithm Components**:  
   - **Population Initialization**: Random sequences of actions.  
   - **Fitness Evaluation**: Rewards progress and penalizes unnecessary actions.  
   - **Selection**: Tournament-based or Roulette Wheel selection.  
   - **Crossover**: Single or two-point crossover for generating offspring.  
   - **Mutation**: Random mutation with a specified rate to introduce diversity.  
   - **Elitism**: Preserves the best solutions across generations.  

- **Visualization**:  
   - Plots the fitness progression (max, average, and minimum) across generations.  

---

## **How to Run**

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/A-Darvish/Genetic-Algorithm.git
   cd Genetic-Algorithm
   ```

2. **Run the Script**:  
   Execute the `game.py` file:  
   ```bash
   python game.py
   ```

3. **Adjust Parameters**:  
   You can modify the following parameters in the script:  
   ```python
   population_size = 200        # Number of chromosomes in each generation
   with_win_score = True        # Reward for finishing the level
   sel_type = 1                 # Selection type: 1 (tournament), 2 (roulette wheel)
   k_point = 1                  # Number of crossover points
   mutation_rate = 0.1          # Probability of mutation
   generations = 10             # Number of generations to evolve
   ```

---

## **Results**

- The best sequence of actions to complete the level is printed in the terminal.  
- A fitness plot showing the **maximum**, **average**, and **minimum** fitness across generations is generated.  

---

## **Dependencies**

- Python 3.x  
- Required Libraries:  
   ```bash
   pip install matplotlib
   ```

---

## **Example Output**

- Best action sequence and its fitness score:
   ```
   ([Best Chromosome], Best Fitness Score)
   ```
- Fitness progression plot across generations.

---

## **Future Improvements**

- Expand levels to include more complex challenges.  
- Introduce additional actions and obstacles.  
- Test with other evolutionary algorithms (e.g., Particle Swarm Optimization).  

---
