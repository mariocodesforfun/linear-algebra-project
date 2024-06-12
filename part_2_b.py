import numpy as np
from numpy.typing import NDArray
from constants import INITIAL_POPULATION, MIGRATION_MATRIX

def combine_populations(initial_population: NDArray[np.float64]) -> NDArray[np.float64]:
    """Combine Manhattan population and the sum of other boroughs' populations."""
    population_other_boroughs = np.sum(initial_population[1:])
    return np.array([initial_population[0], population_other_boroughs])

def calculate_population_distribution(matrix: NDArray[np.float64], initial_population: NDArray[np.float64], start_year: int, end_year: int) -> dict[str, NDArray[np.float64]]:
    """Calculate the population distribution for each year from start_year to end_year."""
    population_distribution = {str(start_year): initial_population}
    for year in range(start_year + 1, end_year + 1):
        population_distribution[str(year)] = matrix @ population_distribution[str(year - 1)]
    return population_distribution

def print_population_distribution(distribution: dict[str, NDArray[np.float64]]) -> None:
    """Print the population distribution for each year."""
    for year, population in distribution.items():
        print(f"Population in {year}: Manhattan: {population[0]:.6f} million, Other Boroughs: {population[1]:.6f} million")

# Define the migration matrix M
M: NDArray[np.float64] = MIGRATION_MATRIX

# Initial population distribution in 2022
initial_population: NDArray[np.float64] = INITIAL_POPULATION

# Combine Manhattan population and other boroughs population
population_2022: NDArray[np.float64] = combine_populations(initial_population)

# Calculate the population distribution for each year from 2025 to 2032
population_distribution: dict[str, NDArray[np.float64]] = calculate_population_distribution(M, population_2022, 2023, 2032)

# Print the population distribution for each year
print_population_distribution(population_distribution)
