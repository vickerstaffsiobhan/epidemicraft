# -*- coding: utf-8 -*-
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt


# make array of all susceptible population
population = np.zeros( (100, 100) )

# random disease outbreak somewhere in the population
outbreak = [0,0]
population[outbreak[0],outbreak[1]] = 1

plt.figure(figsize=(6,4),dpi=150)   



plt.imshow(population, cmap='viridis', interpolation='nearest',vmin=0,vmax=2)


from matplotlib.colors import LinearSegmentedColormap
colors=[(0.80,0.80,0.80),(0.64,0.19,0.13),(0.21,0.23,0.24)]
cm = LinearSegmentedColormap.from_list("my_colors", colors, N=3)

# model parameters: beta, gamma
beta = 0.3
gamma = 0.05
 # make array of all susceptible population
population = np.zeros( (100, 100) )
    
    # random disease outbreak somewhere in the population
outbreak = [0,0]
population[outbreak[0],outbreak[1]] = 1
    # at each time point: 
    # infected cell can infect its neighbours
  
for time in range(100):
       
        # find infected points
        infectedIndex = np.where(population==1)
        for i in range(len(infectedIndex[0])):
            # get x, y coordinates for each point
            x = infectedIndex[0][i]
            y = infectedIndex[1][i]
            # infect each neighbour with probability beta
            # infect all 8 neighbours (this is a bit finicky, is there a better way?):
            for xNeighbour in range(x-1,x+2):
                for yNeighbour in range(y-1,y+2):
                    if (xNeighbour,yNeighbour) != (x,y):
                        # make sure I don't fall off an edge
                        if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                            if population[xNeighbour,yNeighbour]==0:
                                population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
            
            # recover 
            population[x,y] =1+np.random.choice(range(2),1,p=[1-gamma,gamma])[0]
        sirmap = {0:0, 1:0, 2:0}
        for row in population:
            for cell in row: 
                sirmap[cell] += 1
      
        # plot heatmap of population
        plt.figure(figsize=(6,4),dpi=150)   
        # filename=path+"spatial_SIR"+str(time+1)+".png"
        plt.imshow(population, cmap=cm, interpolation='nearest',vmin=0,vmax=2)
        # plt.show()
        # plt.savefig(filename,type="png") 


