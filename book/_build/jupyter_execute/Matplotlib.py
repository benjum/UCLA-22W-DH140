#!/usr/bin/env python
# coding: utf-8

# # Matplotlib

# https://matplotlib.org/
# 
# * "Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python."
# * "Matplotlib makes easy things easy and hard things possible."
# 
# * Matplotlib was built on the NumPy and SciPy frameworks and initially made to enable interactive Matlab-like plotting via gnuplot from iPython
# 
# * Gained early traction with support from the Space Telescope Institute and JPL
# 
# * Easily one of the go-to libraries for academic publishing needs
#   * Create publication-ready graphics in a range of formats
#   * Powerful options to customize all aspects of a figure
#   
# * Matplotlib underlies the plotting capabilities of other libraries such as Pandas, Seaborn, and plotnine

# ![image.png](attachment:image.png)
# Anatomy of a Figure, https://matplotlib.org/3.1.1/gallery/showcase/anatomy.html

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


plt.plot([1,2,3,4])


# In[ ]:


plt.plot([1,2,3,4]);


# In[ ]:


plt.plot([1,2,3,4])
plt.show()


# In[ ]:


plt.plot([1,2,3,4],[2,4,6,8]);


# In[ ]:


plt.plot([1,2,3,4],[2,4,6,8],color='green',marker='o',linestyle='');


# In[ ]:


x = np.linspace(0.5, 3.5, 10)
y = np.cos(x)


# In[ ]:


plt.plot(x,y)
plt.show()


# In[ ]:


plt.plot(x,y,'bo')
plt.show()


# In[ ]:


plt.plot(x,y,'bo')
plt.ylabel('cos(x)')
plt.show()


# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

# In[ ]:


x2 = np.linspace(0.5, 3.5, 10)
y2 = np.cos(2*np.pi/3*(x-0.5))


# In[ ]:


plt.plot(x,y,'bo')
plt.plot(x2,y2,'ks')
plt.ylabel('cos(x)')
plt.show()


# In[ ]:


plt.plot(x,y,'b')
plt.plot(x2,y2,'k')
plt.ylabel('cos(x)')
plt.show()


# In[ ]:


plt.plot(x,y,'b')
plt.plot(x2,y2,'k')
plt.ylabel('y')
plt.xlabel('x')
plt.show()


# In[ ]:


plt.plot(x,y,'b')
plt.plot(x2,y2,'k')
plt.ylabel('y',fontsize=16)
plt.xlabel('x',fontsize=16)
plt.title('cosines',fontsize=16)
plt.show()


# In[ ]:


plt.plot(x,y,'b')
plt.plot(x2,y2,'k')
plt.ylabel('y',fontsize=16)
plt.xlabel('x',fontsize=16)
plt.title('cosines',fontsize=16)
plt.savefig('cosines.png')


# In[ ]:


x = np.linspace(0, 2*np.pi, 100)
y1 = 3 + np.cos(x)
y2 = 1 + 0.5*np.cos(1+x/0.75)

plt.plot(x, y1, color='green', linestyle='-', linewidth=1)
plt.plot(x, y2, color='blue', linestyle='-', linewidth=1)

plt.ylim(0,4.5)
plt.yticks([0, 1, 2, 3, 4], fontsize=14)

plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)

plt.title('sinusoids', fontsize=16)

plt.text(3,0,'addedtext')

plt.annotate('Spine', xy=(6.28, 1.5), xytext=(5.5, 1.0),
            weight='bold', color='blue',
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color='blue'))

plt.show();


# In[ ]:


x = np.linspace(0, 2*np.pi, 100)
y1 = 3 + np.cos(x)
y2 = 1 + 0.5*np.cos(1+x/0.75)

# Make these lines dashed
plt.plot(x, y1, color='green', linestyle='-', linewidth=1)
plt.plot(x, y2, color='blue', linestyle='-', linewidth=1)

plt.ylim(0,4.5)
# Make the x axis range from 0 to 2pi

plt.yticks([0, 1, 2, 3, 4], fontsize=14)
# Make the xticks at (0, pi, 2pi)

plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)

# Change this title to be "Anatomy of a figure"
plt.title('sinusoids', fontsize=16)

# Shift the following text to be below the title, make it more descriptive, color it blue 
plt.text(3,0,'addedtext')

# Use this annotation command to make another annotation pointing to the green line
plt.annotate('Spine', xy=(6.28, 1.5), xytext=(5.5, 1.0),
            weight='bold', color='blue',
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color='blue'))

plt.show();


# In[ ]:


get_ipython().run_line_magic('load', '"assets/helpers/anatomy_figure.py"')


# # pyplot vs figure and axes

# In[ ]:


x = np.linspace(0, 2*np.pi, 100)
y1 = 3 + np.cos(x)
y2 = 1 + 0.5*np.cos(1+x/0.75)


# In[ ]:


plt.plot(x,y1,x,y2)
plt.show()


# In[ ]:


fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x,y1,x,y2)

plt.show()
#fig.show()


# In[ ]:


fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1, 1, 1)

ax.plot(x,y1,x,y2)

plt.show()


# In[ ]:


fig,ax = plt.subplots(1,1,figsize=(8,8))

ax.plot(x,y1,x,y2)

plt.show()


# In[ ]:


fig,ax = plt.subplots(2,1,figsize=(8,8))

ax[0].plot(x,y1)
ax[1].plot(x,y2)

plt.show()


# Let's convert the above *Anatomy* figure (included right below) to use figure and axes

# In[ ]:


x = np.linspace(0, 2*np.pi, 100)
y1 = 3 + np.cos(x)
y2 = 1 + 0.5*np.cos(1+x/0.75)

# Make these lines dashed
plt.plot(x, y1, color='green', linestyle='--', linewidth=1)
plt.plot(x, y2, color='blue', linestyle='--', linewidth=1)

plt.ylim(0,4.5)
# Make the x axis range from 0 to 2pi
plt.xlim(0,2*np.pi)

plt.yticks([0, 1, 2, 3, 4], fontsize=14)
# Make the xticks at (0, pi, 2pi)
plt.xticks([0,np.pi,2*np.pi])

plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)

# Change this title to be "Anatomy of a figure"
plt.title('Anatomy of a figure', fontsize=16)

# Shift the following text to be below the title, make it more descriptive, color it blue 
plt.text(3,4.3,'Title',color='blue')

# Use this annotation command to make another annotation pointing to the green line
plt.annotate('Spine', xy=(6.28, 1.5), xytext=(5.5, 1.0),
            weight='bold', color='blue',
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color='blue'))
plt.annotate('Green line', xy=(0.8, 3.8), xytext=(1.5, 3.4),
            weight='bold', color='blue',
            arrowprops=dict(arrowstyle='->',
                            connectionstyle="arc3",
                            color='blue'))

plt.show();


# In[ ]:


get_ipython().run_line_magic('load', '"assets/helpers/anatomy_figure_axes.py"')


# # Creating different types of plots

# In[ ]:


x = np.linspace(0.5, 3.5, 10)
y = np.cos(x)


# In[ ]:


plt.scatter(x,y)
plt.show()


# In[ ]:


plt.bar(x,y)
plt.show()


# In[ ]:


plt.bar(x,y,width=0.2)
plt.show()


# In[ ]:


plt.barh(x,y,height=0.2)
plt.show()


# In[ ]:


x = np.linspace(0, 4*np.pi, 100)
y = np.linspace(-2, 2, 100)
Xgrid, Ygrid = np.meshgrid(x,y)

f = np.exp(-Ygrid**2) * np.cos(Xgrid)

plt.contourf(f)

plt.show()


# In[ ]:


x = np.linspace(0, 4*np.pi, 100)
y = np.linspace(-2, 2, 100)
Xgrid, Ygrid = np.meshgrid(x,y)

f = np.exp(-Ygrid**2) * np.cos(Xgrid)

plt.contourf(Xgrid, Ygrid, f)

plt.show()


# In[ ]:


x = np.linspace(0, 4*np.pi, 100)
y = np.linspace(-2, 2, 100)
Xgrid, Ygrid = np.meshgrid(x,y)

f = np.exp(-Ygrid**2) * np.cos(Xgrid)

plt.contourf(Xgrid, Ygrid, f)
ax = plt.gca()
ax.set_xticks([0,2*np.pi,4*np.pi])
ax.set_xticklabels(['0','$2\pi$','$4\pi$'])

plt.show()


# In[ ]:


np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(6, 6))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()


# In[ ]:


np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(6, 6))

# for hist, use the parameters "width" and "bins" to experiment with different hist plots
axs[0, 0].hist(data[0])

# give this scatter plot y range of (-3.5,3.5), x range of (-4,4), and make the points green
axs[1, 0].scatter(data[0], data[1])

# make the lines dotted
axs[0, 1].plot(data[0], data[1])

axs[1, 1].hist2d(data[0], data[1])

plt.show()


# In[ ]:


get_ipython().run_line_magic('load', '"assets/helpers/quad_figure.py"')


# In[ ]:


# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)

plt.show()


# ## Change the below cell to make a 3D plot of the data used for the contour plot above

# In[ ]:


# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)

plt.show()


# In[ ]:


get_ipython().run_line_magic('load', '"assets/helpers/3d-figure.py"')

