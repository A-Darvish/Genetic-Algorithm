import random
import matplotlib.pyplot as plt

class Game:
    def __init__(self, levels):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps

        self.levels = levels
        self.current_level_index = -1
        self.current_level_len = 0
        self.with_win_score = None
    
    def load_next_level(self):
        self.current_level_index += 1
        self.current_level_len = len(self.levels[self.current_level_index])


    def initial_population(self, population_size):
        population = []
        for _ in range(population_size):
            chromosome = [random.randint(0, 2) for _ in range(self.current_level_len)]
            for i in range(self.current_level_len - 1):   #this checks that while you're in the air u can't jump or duck.
                if chromosome[i] == 1:
                     chromosome[i+1] = 0
            population.append(chromosome)
        return population
    
    def fitness(self, chromosome):
        current_level = self.levels[self.current_level_index]
        steps = 0
        max_steps = 0
        score = 0
        for i in range(self.current_level_len):
            current_step = current_level[i]
            if chromosome[i] == 1:
                score -= 0.5 # useless jump
            if chromosome[i] == 2:
                score -= 0.3 # useless duck
            if ((i == self.current_level_len - 1) and chromosome[i] == 1):
                score += 1 # finishing with a jump
            if current_step == '_':
                steps += 1
            elif  current_step == 'M':
                if i > 0 and chromosome[i-1] != 1:
                    score += 2 # eating mushroom
                steps += 1
            elif (current_step == 'G' and i > 0 and chromosome[i - 1] == 1):
                steps += 1
            elif (current_step == 'G' and i > 1 and chromosome[i - 2] == 1):
                steps += 1
                score += 2 # killing a Goompa
            elif (current_step == 'L' and chromosome[i - 1] == 2):
                steps += 1
            else:
                max_steps = max(steps, max_steps)
                steps = 0
        max_steps = max(steps, max_steps)
        if self.with_win_score:
            if max_steps == self.current_level_len:
                score += 5 # for winning the game
        score += max_steps
        return score
    
    def calculate_cumulative_fitness(self, population):
        fitness_values = [self.fitness(chromosome) for chromosome in population]
        cumulative_fitness = [sum(fitness_values[:i+1]) for i in range(len(fitness_values))]
        return cumulative_fitness

    def roulette_wheel_selection(self, population, cumulative_fitness):
        selection_point = random.uniform(0, cumulative_fitness[-1])
        for chromosome, fitness_value in zip(population, cumulative_fitness):
            if fitness_value >= selection_point:
                return chromosome

    def selection(self, population, sel_type = 1):
        if sel_type == 1: # only based on fitness
            tournament = random.sample(population, (len(population)//2) + 1)
            tournament.sort(key=self.fitness)
            return tournament[-2 :]
        else:
            selected_parents = []
            for _ in range(2):
                selected_parents.append(self.roulette_wheel_selection(population, self.calculate_cumulative_fitness(population)))
            return selected_parents
    
    def crossover(self, parent1, parent2, k_point):
        point1 = random.randint(1, len(parent1) - 1)
        if k_point == 1:
            child1 = parent1[:point1] + parent2[point1:]
            child2 = parent2[:point1] + parent1[point1:]    
        else:
            point2 = random.randint(0, len(parent1) - 1)
            start = min(point1, point2)
            end = max(point1, point2)
            child1 = parent1[:start] + parent2[start:end] + parent1[end:]
            child2 = parent2[:start] + parent1[start:end] + parent2[end:]
        return child1, child2
    
    def mutation(self, chromosome, mutation_rate):
        for i in range(len(chromosome)):
            if random.random() < mutation_rate:
                while True:
                    new_gene = random.randint(0, 2)
                    if chromosome[i] != new_gene:
                        if i>0 and chromosome[i-1]==1 and new_gene == 1:
                            continue
                        else:
                            chromosome[i] = new_gene
                            break
        return chromosome
    
    def evolutionary_algorithm(self, population_size, with_win_score, sel_type, k_point, mutation_rate, generations):
        self.with_win_score = with_win_score
        population = self.initial_population(population_size)
        min_fit = []
        avg_fit = []
        max_fit = []
        min_fit.append(0)
        avg_fit.append(0)
        max_fit.append(0)
        for _ in range(generations):
            new_population = []
            for _ in range(population_size // 4):
                parent1, parent2 = self.selection(population, sel_type)
                child1, child2 = self.crossover(parent1, parent2, k_point)
                child1 = self.mutation(child1, mutation_rate)
                child2 = self.mutation(child2, mutation_rate)
                new_population.extend([child1, child2])

            remain = population_size - len(new_population)
            population.sort(key=self.fitness)
            new_population.extend(population[-remain :]) # keeping the best parents
            population = new_population
            min_fit.append(min(self.fitness(chromosome) for chromosome in population))
            max_fit.append(max(self.fitness(chromosome) for chromosome in population))
            
            total_fitness = sum(self.fitness(chromosome) for chromosome in population)
            average_fitness = total_fitness / len(population)
            avg_fit.append(average_fitness)

        best_chromosome = max(population, key=self.fitness)
        best_fitness = self.fitness(best_chromosome)
        
        plt.plot(max_fit, color='red', marker='.')
        plt.plot(avg_fit, color='green', marker='.')
        plt.plot(min_fit, color='blue', marker='.')
        plt.xlabel("generation")
        plt.ylabel("fitness")
        plt.legend(["max_fit", "avg_fit", "min_fit"])
        plt.title('first method')
        
        plt.show()
        return best_chromosome, best_fitness
        
    

g = Game(["____G_G_MMM___L__L_G_____G___M_L__G__L_GM____L____"])
g.load_next_level()

population_size = 200 
with_win_score = True
sel_type = 1 # 1: selection based on only fitness /  2: selection based on roulette wheel
k_point = 1 # crossover points
mutation_rate = 0.1 # probablity of mutation
generations = 10

print(g.evolutionary_algorithm(population_size, with_win_score, sel_type, k_point, mutation_rate, generations))

