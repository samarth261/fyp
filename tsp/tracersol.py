import matplotlib.pyplot as plt
import matplotlib.lines as lines
import sys
import pickle

trc = pickle.load(open(sys.argv[1],"rb"))


plt.ion()
city_ = plt.figure()
ax = city_.add_subplot(111)



city = trc.cities
ax.scatter(city[:,0], city[:,1])


edge_line_gen = lambda x,y : lines.Line2D([city[x][0], city[y][0]], 
                                                [city[x][1], city[y][1]],
                                                linewidth=1,
                                                linestyle=':')
tsp = trc.soln
edge_lines = [edge_line_gen(list(tsp[:,i]).index(1), list(tsp[:,(i+1)%len(city)]).index(1)) for i in range(len(city))]
                
for line in edge_lines:
    ax.add_line(line)

input()

