import numpy as np
import csv

import Distributions

# constants
l1 = 1.2              # LAMBDA = AVERAGE NUMBER OF OFFSPRING (PARAMETER FOR POISSON DISTRIBUTION)
s0 = 5                # INITIAL NUMBER OF PARENTS IN GENERATION 0
K = 20                # THE NUMBER OF GENERATIONS EQUALS 20
S = 10              # AMOUNT OF SEEDS TESTED
fileName = 'Output_Galton_Watson.txt'
avg = [0 for x in range(S)]

class Personnel:
    
    def __phi(self, y):
        offspring = 0
        for i2 in range(y): offspring += Distributions.Poisson_distribution(l1)      # GENERATE FOR EACH INDIVIDUAL IN THE POPULATION A NUMBER OF OFFSPRING
        return offspring    

    def procedure(self):
         with open(fileName, 'w', newline='') as csvfile:                            
             c = csv.writer(csvfile, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
             for i0 in range(S):
                np.random.seed(i0)                                   # set seed to i0
                y = s0                                               # set number of initial people (state 0)
                for i1 in range(K):                                  # visit K states
                     print("Generation ", i1, "  Offspring", y, "\n") # print offspring y to console       
                     #c.writerow([i0, i1, y])                        # print offspring y to file
                     y = self.__phi(y)                               # determine offsprings of y at state i1
                     avg[i0] += y;
                avg[i0] /= K
                c.writerow([i0, avg[i0]])                            # print AVG offsprings to file
                       
           
def main():
    MyActivityPtr = Personnel()
    MyActivityPtr.procedure()
    
if __name__ == '__main__':
    main()             