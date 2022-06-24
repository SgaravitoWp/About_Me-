from main import Net


def main(p_, L_, seed_):

    net = Net(p = p_, L = L_, seed = seed_ )
    net.print_matrix(type = "F", draw = "C")
    print(net.per_cluster())

if __name__ == "__main__":
    p = 1
    l = 10
    seed = 5
    main(p, l, seed)



