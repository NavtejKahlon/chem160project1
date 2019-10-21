from random import choice,random
npart=500
maxsteps = 10000
side=31  #Should be an odd number
perc=0
memory = 0
density = float(input("Enter a value between 0 and 1: "))
steps = [(1,0),(-1,0),(0,1),(0,-1)]
for ipart in range(npart):
    grid=[[0 for x in range(side)] for y in range(side)]
    # Setting up fixed cells
    for i in range(side):
        for j in range(side):
            if density > random():
                grid[i][j] = 1

    # Start particle at center
    x,y = side//2,side//2
    # perform the random walk until particle departs
    for step in range(maxsteps):
        memory = grid[x][y]
        grid[x][y]=0   #Remove particle from current spot
        # Randomly move particle
        sx,sy = choice(steps)
        x += sx
        y += sy
        if x<0 or y<0 or x==side or y==side:
            perc += 1
            break
        if grid[x][y] == 1:
            x -= sx
            y -= sy
            grid[x][y] = memory
            continue
        grid[x][y]=1   #Put particle in new location

print("probability of Percolation =%5.2f"%( perc/npart))