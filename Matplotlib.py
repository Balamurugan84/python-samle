# graph

import matplotlib.pyplot as plt
import numpy as np

plt.title("Line graph")
xpoints = np.array([0, 6])
ypoints = np.array([0, 300])
plt.plot(xpoints, ypoints)
plt.show()

#  marker

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = '*')
plt.show()


# label

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110])
y = np.array([240, 250, 260, 270, 280, 290, 300])
plt.plot(x, y)
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()

# grid

import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110])
y = np.array([240, 250, 260, 270, 280, 290, 300])

plt.title("Sports Watch Data")
plt.xlabel("x-label")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid()
plt.show()

# subplot

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])
plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])
plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.show()

# pie

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
plt.pie(y)
plt.show()

