from viksek_model import*
import shutil 

N = 100           # num of particlex
r = 0.1          # radius
delta_t = 0.01   # time step

# Maximum time

T = 1.0 #was 2.0

def run_for_10_etas():

    # Generate random particle coordinates
    # particles[i,0] = x
    # particles[i,1] = y
    particles = np.random.uniform(0, 1, size=(N, 2))

    # initialize random angles
    thetas = np.zeros((N, 1))
    for i, theta in enumerate(thetas):
        thetas[i, 0] = rand_angle()

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

    os.chdir(particledir)

    for eta in np.arange(0.0,1.1,0.1):

        t = 0.0

        print("Creating particle files", end='', flush=True)
        # Currently run until time ends
        while t < T:
            print(end='.', flush=True)
            # save coordinates & corresponding thetas to a text file
            output = np.concatenate((particles, thetas), axis=1)
            np.savetxt("%.2f.txt" % t, output)
            for i, (x, y) in enumerate(particles):
                # get neighbor indices for current particle
                neighbors = get_neighbors(particles, r, x, y)[0]
                # get average theta angle
                avg = get_average(thetas, neighbors)
                # get noise angle
                n_angle = rand_angle()
                noise = eta * n_angle
                # get new theta
                thetas[i] = avg + noise
                # move to new position 
                particles[i,:] += delta_t * angle_2_vector(thetas[i])
                # assure correct boundaries (xmax, ymax) = (1,1)
                if particles[i, 0] < 0:
                    particles[i, 0] = 1 + particles[i, 0]
                if particles[i, 0] > 1:
                    particles[i, 0] = particles[i, 0] - 1
                if particles[i, 1] < 0:
                    particles[i, 1] = 1 + particles[i, 1]
                if particles[i, 1] > 1:
                    particles[i, 1] = particles[i, 1] - 1
            # new time step
                t+= delta_t

            
            
            
            
        final_out = np.concatenate((particles, thetas), axis=1)
        np.savetxt("%.2f.txt" % eta, final_out)

    print()

    # initialize vector to store measures of polarization each eta value
    pol_of_eta=np.zeros(11)

    # read from the files and measue polarization at each eta value and store
    txt_files = [i for i in sorted(os.listdir(particledir)) if i.endswith(".txt")]
    for fname,h in zip(txt_files,range(11)):
        f = os.path.join(particledir, fname) # the actual file
        # read in data
        mat = np.loadtxt(f)
        thetas = mat[:,2]
        polarization=1/len(thetas)*np.sqrt(sum(np.sin(thetas))**2+sum(np.cos(thetas))**2)
        pol_of_eta[h]=polarization
    print()

    return pol_of_eta


