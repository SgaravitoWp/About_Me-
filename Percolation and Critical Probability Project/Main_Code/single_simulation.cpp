#include "percolation_problem.h"

int main(int argc, char **argv)
{
  const long SIZE = std::atol(argv[1]);
  const double FILL_PROBABILITY = std::atof(argv[2]);

  //Se repite este número de veces para calcular 1 vez.
  const int REPS_PER_1_CALCULATION = std::atoi(argv[3]);

  //Este es el número de veces que se calcula la probabilidad.
  const int GROUPS_OF_CALCULATIONS = std::atoi(argv[4]);

  int seed = std::atoi(argv[5]);

  compute_mean_and_standard_deviation_for_percolating_probability(SIZE, FILL_PROBABILITY, REPS_PER_1_CALCULATION, GROUPS_OF_CALCULATIONS, seed);  

  return 0;
}
