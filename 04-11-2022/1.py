import numpy as np
import pandas as pd
import matplotlib.pyplot

matplotlib.pyplot.plot(np.array([n for n in range(1, 11)]),
                       np.array([n**2 for n in range(1, 11)]))
matplotlib.pyplot.show()