# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'colA': [10, 20, 30],
                   'colB': [100, 200, 300]})

print(df)

-- second line

plt.scatter(x=df['colA'],y=df['colB'])
plt.title('Scatter Plot')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.savefig('Scatter Plot')


