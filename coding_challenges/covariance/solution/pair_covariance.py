# developing the covariance matrix here,
# to help motivate the pca lecture

import pandas as pd
import numpy as np

# 3 observations
A = [[25, 30], [29, 40], [39, 78]]

data = pd.DataFrame(A)

# subtract means (on a column-basis)
means = np.mean(data)
delt = data - means

covar = np.dot(delt.T, delt)
covar
