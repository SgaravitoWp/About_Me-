import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

class Net:
    def __init__(self, p, L, seed):

        self.p = p
        self.l = L
        self.seed = seed
        self.__matrix = self.create_matrix()
        self.__final_matrix = self.__matrix.copy()
        self.clustersNum = 2
        

    def set_seed(self):
        np.random.seed(self.seed)

    def create_matrix(self):
        
        if self.seed is not None:
            self.set_seed()

        start_matrix = np.ones(self.l+2, dtype=int)*-1

        for i in range(0,self.l):

            random_sample = np.random.binomial(1,self.p, self.l)
            left_zero = np.insert(random_sample,0, np.array([-1]))
            right_zero = np.append(left_zero,np.array([-1]))
            start_matrix = np.append(start_matrix,right_zero)
            
        prev_random_matrix = np.append(start_matrix, np.ones(self.l+2,dtype=int)*-1)
        random_matrix = np.reshape(prev_random_matrix, (self.l+2,-1))
        
        return random_matrix
    

    def clusters_mark(self, i, j):
                   
            self.__final_matrix[i,j] = self.clustersNum
            if self.__final_matrix[i+1, j] == 1:
                self.clusters_mark(i+1, j)
            else:
                pass
            if self.__final_matrix[i-1, j] == 1:
                self.clusters_mark(i-1,j)
            else:
                pass
            if self.__final_matrix[i, j+1] == 1:
                self.clusters_mark(i,j+1)
            else:
                pass
            if self.__final_matrix[i, j-1] == 1:
                self.clusters_mark(i,j-1)
            else:
                pass
        
    def clusters_finding(self):
        for i in range(self.l +2):
            for j in range(self.l +2):
                if self.__final_matrix[i,j] != 1:
                    continue
                else:
                    self.clusters_mark(i, j)
                    self.clustersNum += 1         

    def cut_matrix(self, type):
        if type == 'I':
            return self.__matrix[1:self.l+1,1:self.l+1]
        if type == 'F':
            return self.__final_matrix[1:self.l+1,1:self.l+1]

    def print_matrix(self, type, draw):
        if draw == "M":
            print(self.cut_matrix(type))
        if draw == "C":
            plt.figure(figsize=(5,5))
            plt.pcolor(self.cut_matrix(type))
            plt.axis('off')
            plt.show()
        
