#!/usr/bin/python3.5

# basically used to generate tsp problems that are nice.

def rand_city(count):
    # count is the number of cities
    # max_x and max_y are the maximum allowed ranges for the cities
    
    import numpy as np

    # this will store the list of cities
    cities = [None,None]
    dist = []
    # cities[0] = np.random.random(x_max,size = count)
    # cities[1] = np.random.random(y_max,size = count)

    cities[0] = np.random.random_sample(size = count)
    cities[1] = np.random.random_sample(size = count)
    cities = np.transpose(np.array(cities))
    # now the cities.shape is (count, 2)

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


def new_fname(city_count):
    fname = str(city_count)
    cnt = int(open("prob_num.txt").read())
    fname += "_" + str(cnt)
    cnt += 1
    open("prob_num.txt","w").write(str(cnt))
    return fname


def my_export(cities):
    # basically pickle 'cities' and store in file
    import pickle
    fname = new_fname(len(cities))
    pickle.dump(cities, open(fname,"wb"))


def get_cmdline_args():
    # returns a parser required to parse the command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--ncity", type=int, default=10, help="The number of cities in the graph")

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import _thread

    args = get_cmline_args()
    N_CITY = args.ncity
    plt.ion()
    cities_plot = plt.figure()
    ax = cities_plot.add_subplot(111)
    while True:
        city, dist = rand_city(N_CITY)
        print(city)
        for row in dist:
            print (row)

        #_thread.start_new_thread(plot_cities, (city,))
        ax.scatter(city[:,0], city[:,1])
        ii = input()
        if ii == 'e':
            # now we export the city positions
            my_export(city)
        ax.clear()
