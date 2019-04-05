#!/usr/bin/python3.5
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines

# Examples
# ./vc-gui.py -n 40 -d 0.1
# ./vc-gui.py -n 10 -d 0.5


def get_cmdline_args():
    # returns a parser required to parse the command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--density", type=float)
    parser.add_argument("-n", "--number", type=int)
    return parser.parse_args()



# This file is for the gui part of the vertex cover example.

# The following are what we are going to be doing
# 1. Generate the set of random 'N' vertices
# 2. Next we randomly generate the edges
# 3. Next the magic is done by Manju's code
# 4. So now we get the approximate VertexCover .. basically the set of point to be colored differently
# 5. Now we plot them all

if __name__ == "__main__":
    args = get_cmdline_args()
    # Generate the random vertice's co-ords
    n_vertices = args.number
    # This produces 2 columns and n rows ndarray
    vertices = np.random.rand(n_vertices,2)

    # Now the random edges
    density = args.density
    # basically produce integer pairs.. The elements are actually the indices of the vertices
    # There might be repeats.. but we don't care
    # edges = np.random.randint(0,n_vertices, (int(n_vertices**2 * density),2))

    edges = list(map(lambda x : [x//n_vertices, x%n_vertices],
                    np.random.choice(n_vertices**2, int(n_vertices**2 * density), False)))


    # Now the random subset of vertices
    vc_size = 1 + int((n_vertices-1) * (1- (density**1.2)))
    vc = np.random.choice(n_vertices, vc_size, False) # False to avoid replacement

    # Now the plotting

    # 1. all the points
    # 2. all the edges
    # 3. vc points

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(vertices[:,0], vertices[:,1])

    # for plotting the edges
    edge_line_gen = lambda x : lines.Line2D([vertices[x[0]][0],vertices[x[1]][0]], 
                                        [vertices[x[0]][1],vertices[x[1]][1]],
                                        linewidth=1,
                                        linestyle=':')
    edge_lines = [edge_line_gen(edges[i]) for i in range(len(edges))]

    for line in edge_lines:
        ax.add_line(line)

    # for plotting the vertices in vc
    ax.scatter(vertices[vc,0],vertices[vc,1])

    input()
