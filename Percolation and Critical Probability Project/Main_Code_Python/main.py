
import numpy as np
import matplotlib.pyplot as plt
import sys 


class Net:

    def __init__(self, p, L, seed):

        self.p = p
        self.l = L
        self.seed = seed
        self.__matrix = self.__create_matrix()
        self.__final_matrix = self.__matrix.copy()
        self.clustersNum = 2
        self.__clusters_finding()
        
    '''Metodos Privados'''

    def __set_seed(self):
        np.random.seed(self.seed)

    def __create_matrix(self):
        
        if self.seed is not None:
            self.__set_seed()

        start_matrix = np.ones(self.l+2, dtype=int)*-1

        for i in range(0,self.l):

            random_sample = np.random.binomial(1,self.p, self.l)
            left_zero = np.insert(random_sample,0, np.array([-1]))
            right_zero = np.append(left_zero,np.array([-1]))
            start_matrix = np.append(start_matrix,right_zero)
            
        prev_random_matrix = np.append(start_matrix, np.ones(self.l+2,dtype=int)*-1)
        random_matrix = np.reshape(prev_random_matrix, (self.l+2,-1))
        
        return random_matrix
    

    def __clusters_mark(self, i, j):
                   
            self.__final_matrix[i,j] = self.clustersNum
            if self.__final_matrix[i+1, j] == 1:
                self.__clusters_mark(i+1, j)
            else:
                pass
            if self.__final_matrix[i-1, j] == 1:
                self.__clusters_mark(i-1,j)
            else:
                pass
            if self.__final_matrix[i, j+1] == 1:
                self.__clusters_mark(i,j+1)
            else:
                pass
            if self.__final_matrix[i, j-1] == 1:
                self.__clusters_mark(i,j-1)
            else:
                pass
        
    def __clusters_finding(self):
        for i in range(self.l +2):
            for j in range(self.l +2):
                if self.__final_matrix[i,j] != 1:
                    continue
                else:
                    self.__clusters_mark(i, j)
                    self.clustersNum += 1         

    def __cut_matrix(self, type):
        if type == 'I':
            return self.__matrix[1:self.l+1,1:self.l+1]
        if type == 'F':
            return self.__final_matrix[1:self.l+1,1:self.l+1]

    def __vertical_per_cluster(self):
        
        row_sup = set(self.__cut_matrix("F")[0])
        row_inf = set(self.__cut_matrix("F")[self.l - 1])
        global_cluster = list((row_sup & row_inf) - {0})
        global_cluster = len(global_cluster)

        return global_cluster
    
    def __horizontal_per_cluster(self):
        
        column_sup = set(np.transpose(self.__cut_matrix("F")[0:self.l,0]))
        column_inf = set(np.transpose(self.__cut_matrix("F")[0:self.l,self.l - 1]))
        global_cluster = list((column_sup & column_inf) - {0})
        global_cluster = len(global_cluster)

        return global_cluster

    '''Metodos accesibles'''

    def clusters_count(self):
        return np.max(self.__final_matrix) -1

    def per_cluster(self):
        if self.__horizontal_per_cluster() + self.__vertical_per_cluster() == 0:
            boolean = False
        else:
            boolean = True
        return boolean

    def print_matrix(self, type, draw):
        if draw == "M":
            print(self.__cut_matrix(type))
        if draw == "C":
            plt.figure(figsize=(5,5))
            plt.pcolor(self.__cut_matrix(type))
            plt.axis('off')
            plt.show()
        
