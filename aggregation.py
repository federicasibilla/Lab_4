from attraction_rule import run_aggregation
import matplotlib.pyplot as plt
import numpy as np

times=30

y=[]

for i in range(times):
    y.append(run_aggregation())

X =np.repeat(np.arange(0.0,1.0,0.01),times)
Y=[item for sublist in y for item in sublist]


# Plot heatmap
plt.figure()
plt.hist2d(X, Y)
plt.xlabel('$time$')
plt.ylabel('Aggregation')
plt.colorbar()
plt.tight_layout()
plt.show()