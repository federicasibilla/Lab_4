from viksek_model import*
import random as rn

# takes indices of particles in the attraction zone
# returns (x,y) direction towards which to move
def direction_to(coordinates,attraction_zone):

    x=[]
    y=[]
    for index in attraction_zone:
        x.append(coordinates[index,0])
        y.append(coordinates[index,1])

    return (sum(x)/len(x),sum(y)/len(y))

# ------------------------------- RUNS FROM HERE -------------------------------

def run_aggregation_10_eta():


   # keeping it tidy
    simdir = os.path.join(os.getcwd(), "simulation")
    particledir = os.path.join(simdir, "particles")
    plotdir = os.path.join(simdir, "plots")

    if not os.path.exists(simdir):
        os.mkdir(simdir)
    if not os.path.exists(particledir):
        os.mkdir(os.path.join(simdir, "particles"))
    if not os.path.exists(plotdir):
        os.mkdir(os.path.join(simdir, "plots"))

    

    N = 100           # num of particles
    eta = 0.1       # noise in [0,1], add noise uniform in [-eta*pi, eta*pi]
    r = 0.1          # radius
    delta_t = 0.01   # time step

    # Generate random particle coordinates
    # particles[i,0] = x
    # particles[i,1] = y
    particles = np.random.uniform(0, 1, size=(N, 2))
    # initialize random angles
    thetas = np.zeros((N, 1))
    for i, theta in enumerate(thetas):
        thetas[i, 0] = rand_angle()
    os.chdir(particledir)

    T = 1.0 #was 2.0

    aggregations=[]
    for eta in np.arange(0.0,1.1,0.1):
            # Maximum time
        t = 0.0

        
        aggregations_t=[]
        print("Creating particle files", end='', flush=True)
        # Currently run until time ends
        while t < T:

            print(end='.', flush=True)
            # save coordinates & corresponding thetas to a text file
            output = np.concatenate((particles, thetas), axis=1)
            np.savetxt("%.2f.txt" % t, output)

            avg_dist=[]
            for i, (x, y) in enumerate(particles):

                # get neighbor indices for current particle
                neighbors = get_neighbors(particles, r, x, y)[0]
                attraction_zone=get_neighbors(particles, r,x,y)[1]

                # get average theta angle
                avg = get_average(thetas, neighbors)

                # get noise angle
                n_angle = rand_angle()
                noise = eta * n_angle

                # get new theta
                thetas[i] = avg + noise

                # get average position of particles in attraction zone
                avg_pos=direction_to(particles,attraction_zone)

                # get noise 
                rnx=rn.random()
                rny=rn.random()
                n_pos = np.asarray([rnx,rny])
                noise_pos = eta * n_pos+avg_pos
                pos_unit = noise_pos/(np.sqrt(noise_pos[0]**2+noise_pos[1]**2))

                # adding noise allignment and aggregation contributions
                final_move=angle_2_vector(thetas[i])+pos_unit
                final_move_unit=final_move/(np.sqrt(final_move[0]**2+final_move[1]**2))

                # move to new position with respect to alignment zone
                particles[i,:] += delta_t * (final_move_unit)

                # assure correct boundaries (xmax, ymax) = (1,1)
                if particles[i, 0] < 0:
                    particles[i, 0] = 1 + particles[i, 0]

                if particles[i, 0] > 1:
                    particles[i, 0] = particles[i, 0] - 1

                if particles[i, 1] < 0:
                    particles[i, 1] = 1 + particles[i, 1]

                if particles[i, 1] > 1:
                    particles[i, 1] = particles[i, 1] - 1

                # meausre of aggregation
                dist=[]
                for index in neighbors:
                    dist.append(euclidean_distance(particles[index][0], particles[index][1], x, y))

                avg_dist.append(sum(dist)/len(dist))

            aggregations_t.append(sum(avg_dist)/len(avg_dist))

            # new time step
            t += delta_t
            
        print()
        aggregations.append(aggregations_t[-1])

    return aggregations

  

#initialize matrix to store vectors with final polarization for different etas for m simulations
m=25
matrix=np.zeros((m,11))

for l in range(m):
    matrix[l]=run_aggregation_10_eta()

print(matrix)