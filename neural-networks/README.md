# Neural Networks

## Data pre-preprocessing

These two approaches give the same result for scaling called *Auto* or *std*.

### Scale using `StandardScaler`

```Python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load full csv data:
Target_original = pd.read_csv('Target.csv', sep = ',', header=None)
Input_original = pd.read_csv('Input.csv', sep = ',', header=None)

# Change DataFrame to numpy array:
Target_original = Target_original.to_numpy()
Input_original = Input_original.to_numpy()

# Center and scale with StandardScaler:
scale_Input = StandardScaler()
Input_original = scale_Input.fit_transform(Input_original)

scale_Target = StandardScaler()
Target_original = scale_Target.fit_transform(Target_original)
```

### Scale manually

```Python
import numpy as np
import pandas as pd

# Load full csv data:
Target_original = pd.read_csv('Target.csv', sep = ',', header=None)
Input_original = pd.read_csv('Input.csv', sep = ',', header=None)

# Change DataFrame to numpy array:
Target_original = Target_original.to_numpy()
Input_original = Input_original.to_numpy()

# Center and scale manually:
mean_Input = np.mean(Input_original, axis=0)
std_Input = np.std(Input_original, axis=0)
mean_Target = np.mean(Target_original, axis=0)
std_Target = np.std(Target_original, axis=0)

Input_original = (Input_original - mean_Input)/std_Input
Target_original = (Target_original - mean_Target)/std_Target
```

## Quality of reconstruction

These two approaches of computing the Root Mean Squared Error (RMSE) or Normalized Root Mean Squared Error (NRMSE) give the same result. Below, `X` is the original data and `X_fit` is the model fit.

### RMSE/NRMSE using `mean_squared_error`

```Python
import numpy as np
from math import sqrt
from sklearn.metrics import mean_squared_error

rmse = sqrt(mean_squared_error(X, X_fit))
print(rmse)
nrmse = rmse/sqrt(np.mean(X**2))
print(nrmse)
```

### RMSE/NRMSE manually
```Python
import numpy as np
from math import sqrt

rmse = sqrt(np.mean((X - X_fit)**2))
print(rmse)
nrmse = rmse/sqrt(np.mean(X**2))
print(nrmse)
```
