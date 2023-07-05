Here is how you can compute the Accuracy Ratio (AR) using Python and pandas, given that you have the P[S=s], P[D|S=s] and P[N|S=s] in pandas Series. Note that the provided formula for AR involves two parts which we will calculate separately and then combine. 

```python
import pandas as pd

# Assuming the following are your input pandas Series
P_S_s = pd.Series([...])  # insert your values for P[S=s]
P_D_S_s = pd.Series([...])  # insert your values for P[D|S=s]
P_N_S_s = pd.Series([...])  # insert your values for P[N|S=s]

# First, we calculate p as per your earlier question
p = sum(P_D_S_s * P_S_s)

# Begin calculating the parts of the AR equation
first_part = 0
second_part = 0
k = len(P_S_s)  # assuming the length of all Series is the same

for s in range(1, k+1):
    sum_t = sum([P_D_S_s[t-1]*P_S_s[t-1] for t in range(1, s)])
    first_part += (1 - P_D_S_s[s-1]) * P_S_s[s-1] * sum_t

    second_part += P_D_S_s[s-1] * (1 - P_D_S_s[s-1]) * (P_S_s[s-1]**2)

# Calculate the AR as per the provided equation
AR = (1/(p*(1-p))) * (2 * first_part + second_part) - 1

print(f"AR: {AR}")
```

Please note that in Python, indexing starts from 0, hence the `s-1` and `t-1` indices in the script. Also, remember to replace `[...]` with your actual data.
