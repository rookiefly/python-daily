import pandas as pd
import numpy as np

print("read data.xlsx...")
r_frame = pd.read_excel("data.xlsx")
print(r_frame)

print("write data2.xlsx...")
w_frame = pd.DataFrame(np.random.random((4, 4)),
                       # index=['exp1', 'exp2', 'exp3', 'exp4'],
                       columns=['jan2015', 'Fab2015', 'Mar2015', 'Apr2005'])
print(w_frame)
w_frame.to_excel("data2.xlsx", index=False)
