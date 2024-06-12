import numpy as np
from numpy.typing import NDArray
from constants import MIGRATION_MATRIX, INITIAL_POPULATION

# Define the migration matrix M
M: NDArray[np.float64] = MIGRATION_MATRIX

# Initial population distribution in 2023
initial_population: NDArray[np.float64] = INITIAL_POPULATION

# Sum the populations of the other four boroughs
population_other_boroughs: float = np.sum(initial_population[1:])

# Combine Manhattan population and other boroughs population
population_current: NDArray[np.float64] = np.array([initial_population[0], population_other_boroughs])

def calculate_long_term_population(M: NDArray[np.float64], population_current: NDArray[np.float64],
                                   capacity: float = 3.0, threshold: float = 1e-6) -> tuple[NDArray[np.float64], int]:
    """Calculate the long-term population distribution and stabilization year."""
    year = 2023
    while True:
        population_next = M @ population_current
        # Check if the population stabilizes (difference is below a small threshold)
        if np.allclose(population_next, population_current, atol=threshold):
            break
        population_current = population_next
        year += 1
        # Check if Manhattan's population reaches its capacity
        if population_current[0] >= capacity:
            return population_current, year
    return population_current, year

# Calculate the long-term population distribution
long_term_population, stabilization_year = calculate_long_term_population(M, population_current)

# Print the long-term population distribution and the stabilization year
print(f"Long-term Population Distribution: Manhattan: {long_term_population[0]:.6f} million, Other Boroughs: {long_term_population[1]:.6f} million")
print(f"The population distribution stabilizes around the year {stabilization_year}")

# Check if Manhattan reaches its capacity and when
if long_term_population[0] >= 3.0:
    print(f"Manhattan's population reaches its capacity of 3 million around the year {stabilization_year}")
else:
    print("Manhattan's population does not reach its capacity of 3 million.")
