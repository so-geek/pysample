# %%
import numpy as np
import matplotlib.pyplot as plt

test = "test now "

# %%
print(test)

# %%

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

# %%
y = np.linspace(0, 20, 100)
plt.plot(y, np.cos(y))
plt.show()
