#4_1 from Lab Book
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

work = np.array([20, 15, 10 ,3])
GPA = np.array([10, 9, 6, 2])

model = LinearRegression()
model.fit(GPA.reshape(-1, 1), work)

b = model.intercept_
a = model.coef_

plt.close('all')
plt.plot(GPA,work,'o')
plt.xlabel('GPA')
plt.ylabel('work')

y = a * GPA + b
plt.plot(GPA, y)
plt.grid(True)

gpa = 5
wrk = a * gpa + b
plt.plot(gpa, wrk, 'dr')
print('Work for GPA = 5 is', np.round(wrk[0], decimals = 2), 'hours')