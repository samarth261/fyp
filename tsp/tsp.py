#!/usr/bin/python3.5


# we are going to generate the co-ordinates of the given number of cities
# and then return a distance matrix for the same

def rand_city(count, x_max, y_max):
    # count is the number of cities
    # max_x and max_y are the maximum allowed ranges for the cities
    
    import random as r
    import numpy as np

    # this will store the list of cities
    cities = [None,None]
    dist = []
    cities[0] = np.random.randint(x_max,size = count)
    cities[1] = np.random.randint(y_max,size = count)
    cities = np.transpose(np.array(cities))

    # now we calculate the distance matrix
    from math import sqrt as sqrt
    def dist_fx(a,b):
        return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    for i in range(len(cities)):
        dist.append([])
        for j in range(len(cities)):
            dist[i].append([])
            dist[i][j] = dist_fx(cities[i],cities[j])

    return cities, np.array(dist)

def hopfield_tsp(cities, distances):
    import numpy as np

    num_cities = len(cities)
    network = np.random.rand(num_cities, num_cities)

    # row constraint
    row_term = 0
    for row in network:
        row_on_row = np.matrix(row.reshape(-1,1)) * np.matrix(row.reshape(1,-1))

        # swap_0_and_1 is np.array and so is mask
        swap_0_and_1 = np.vectorize(lambda x : 0 if x == 1 else 1)
        mask = swap_0_and_1(np.identity(num_cities))

        # now we remove the diagonal of the matrix
        row_on_row = row_on_row * mask

        row_term += np.sum(row_on_row)


    # column constraint
    column_term = 0
    for col in network.transpose():
        col_on_col = np.matrix(col.reshape(-1,1)) * np.matrix(col.reshape(1,-1))

        # swap_0_and_1 is np.array and so is mask
        swap_0_and_1 = np.vectorize(lambda x : 0 if x == 1 else 1)
        mask = swap_0_and_1(np.identity(num_cities))

        # now we remove the diagonal of the matrix
        col_on_col = col_on_col * mask

        column_term += np.sum(col_on_col)

    # the n_cities term
    n_cities_term = sum(network) - num_cities
    n_cities_term **= 2
    
    # the distance constraint
    total_distance = 0


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    N_CITY = 10
    MAX_X = 10
    MAX_Y = 10
    city, dist = rand_city(N_CITY, MAX_X, MAX_Y)
    print(city)
    for row in dist:
        print (row)

    #_thread.start_new_thread(plot_cities, (city,))
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(city[:2,0], city[:2,1])
    ax.scatter(city[:,0], city[:,1])

    hopfield_tsp(city)

    input()
