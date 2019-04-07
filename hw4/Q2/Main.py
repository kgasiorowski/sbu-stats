import scipy.stats as st
from math import sqrt

target = .95
counter = 1

while True:

    mean = 69.5
    sd = 3.0

    val1 = 70.48
    val2 = 68.52

    temp1 = st.norm.cdf((val1 - mean)/(sd/sqrt(counter)))
    temp2 = st.norm.cdf((val2 - mean)/(sd/sqrt(counter)))

    final = round(temp1 - temp2, 5)

    print(counter, " : ", final)

    if final == target or final == 1 or final == -1:
        break

    counter += 1
