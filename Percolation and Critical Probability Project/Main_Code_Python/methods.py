from random import seed
from main import Net


def main(p_, L_, seed_):

    net = Net(p = p_, L = L_, seed = seed_ )
    net.clusters_finding()
    net.print_matrix(type='F', draw="C")

if __name__ == "__main__":
    p = ''
    l = ''
    seed = ''
    main(p, l, seed)



