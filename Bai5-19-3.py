import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = x**2
y2 = np.sqrt(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

ax1.plot(x, y1, label='y = x^2', color='blue')
ax1.set_title('Đồ thị y = x^2')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid()

ax2.plot(x, y2, label='y = sqrt(x)', color='orange')
ax2.set_title('Đồ thị y = sqrt(x)')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()
ax2.grid()

plt.tight_layout()
plt.show()

