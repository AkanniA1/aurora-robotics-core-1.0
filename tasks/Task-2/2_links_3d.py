# two_link_3d_sliders.py
# The beggining of all python projects, which is the inclusion of libraries into the projects
#Numpy for array , pyplot for graph, Slider for Sliders I think And Axes3D in 3Dn on  as written on line 7
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D)

# --------- link lengths (units) ----------
L1 = 1.5 # This is initialising Length 1
L2 = 1.0 # This is initialising Length 1

def Rz(t):# defining a function
    c, s = np.cos(t), np.sin(t)  # C = np.cos t and s = npsin t
    return np.array([[c,-s,0],# Numpy in action to create arrat with c,s earlier defines
                     [s, c,0],
                     [0, 0,1]])

def Ry(t): # defining another function
    # Same explanation as last.
    c, s = np.cos(t), np.sin(t)
    return np.array([[ c,0, s],
                     [ 0,1, 0],
                     [-s,0, c]])
# Making a function for 3D... Initialling and assigning R0, R1, p0,p1,p2
def fk_3d(q_yaw, q_sh, q_el):
    """Return 3D points (base, joint, ee) for a 2-link arm with
       base-yaw (about z), then shoulder pitch (about y), then elbow pitch (about y)."""
    R0 = Rz(q_yaw)
    R1 = R0 @ Ry(q_sh)
    p0 = np.zeros(3)
    p1 = R1 @ np.array([L1, 0, 0])
    p2 = p1 + (R1 @ Ry(q_el)) @ np.array([L2, 0, 0])
    return p0, p1, p2

# --------- figure/axes ----------
# We are about to plot the graph using Axes 3D or maybe not
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("3D 2-Link Arm (yaw, shoulder, elbow)")
ax.set_box_aspect((1,1,1))
lim = L1 + L2 + 0.3 # defining Lim using L1 and L2
ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)# two_link_3d_sliders.py
# The beggining of all python projects, which is the inclusion of libraries into the projects
#Numpy for array , pyplot for graph, Slider for Sliders I think And Axes3D in 3Dn on  as written on line 7
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D)

# --------- link lengths (units) ----------
L1 = 1.5 # This is initialising Length 1
L2 = 1.0 # This is initialising Length 1

def Rz(t):# defining a function
    c, s = np.cos(t), np.sin(t)  # C = np.cos t and s = npsin t
    return np.array([[c,-s,0],# Numpy in action to create arrat with c,s earlier defines
                     [s, c,0],
                     [0, 0,1]])

def Ry(t): # defining another function
    # Same explanation as last.
    c, s = np.cos(t), np.sin(t)
    return np.array([[ c,0, s],
                     [ 0,1, 0],
                     [-s,0, c]])
# Making a function for 3D... Initialling and assigning R0, R1, p0,p1,p2
def fk_3d(q_yaw, q_sh, q_el):
    """Return 3D points (base, joint, ee) for a 2-link arm with
       base-yaw (about z), then shoulder pitch (about y), then elbow pitch (about y)."""
    R0 = Rz(q_yaw)
    R1 = R0 @ Ry(q_sh)
    p0 = np.zeros(3)
    p1 = R1 @ np.array([L1, 0, 0])
    p2 = p1 + (R1 @ Ry(q_el)) @ np.array([L2, 0, 0])
    return p0, p1, p2

# --------- figure/axes ----------
# We are about to plot the graph using Axes 3D or maybe not
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')
ax.set_title("3D 2-Link Arm (yaw, shoulder, elbow)")
ax.set_box_aspect((1,1,1))
lim = L1 + L2 + 0.3 # defining Lim using L1 and L2
ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_zlim(-lim, lim)
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')

# initial angles (deg -> rad)
yaw0, sh0, el0 = 30.0, 20.0, 40.0# initialising the initia values
yaw = np.deg2rad(yaw0); sh = np.deg2rad(sh0); el = np.deg2rad(el0) # Converting degree to radian using an inbuilt function

# plot initial arm
b, j, e = fk_3d(yaw, sh, el) # getting initial position for the parts of the arm
(line,) = ax.plot([b[0], j[0], e[0]],
                  [b[1], j[1], e[1]],
                  [b[2], j[2], e[2]],
                  marker='o', linewidth=3)
txt = ax.text2D(0.02, 0.98, "", transform=ax.transAxes, va="top")# Plotting using the 3D plot

# sliders
ax_yaw = plt.axes([0.15, 0.06, 0.7, 0.02])# Plot ax_ yaw
ax_sh  = plt.axes([0.15, 0.03, 0.7, 0.02])# Plot ax_sh
ax_el  = plt.axes([0.15, 0.00, 0.7, 0.02])# Plot ax_el
# All plots above are in 2D using the Matplotlib. pyplot as plt , Sometimes py in some youtube videos

s_yaw = Slider(ax_yaw, 'yaw (°)', -180, 180, valinit=yaw0)# I dont know explanation for this sha... But I know s_yaw is
# been defined with respect to ax_yaw
s_sh  = Slider(ax_sh,  'shoulder (°)', -179, 179, valinit=sh0)# same with s_sh with respect to ax_sh
s_el  = Slider(ax_el,  'elbow (°)',   -179, 179, valinit=el0)# as well as s_el with ax_el
# Just noticed s in front is for easy identification since it uses sliders, while ax uses axes 3D

def update(_):# defining another function,et me just put it all here
#q1, q2, q0, convert degree to radians for s_yaw but has to be a value that is why.val is  there
    q0 = np.deg2rad(s_yaw.val) #
    q1 = np.deg2rad(s_sh.val)
    q2 = np.deg2rad(s_el.val)
    b, j, e = fk_3d(q0, q1, q2) # using the newly got value to build a 3D Function
    line.set_data_3d([b[0], j[0], e[0]],
                     [b[1], j[1], e[1]],
                     [b[2], j[2], e[2]])# creating an array from the values gotten earlier
    txt.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}, z={e[2]:.3f}\n"
                 f"yaw={s_yaw.val:.1f}°, sh={s_sh.val:.1f}°, el={s_el.val:.1f}°")# Dont really get this line, but
# we limiting the decimal points...
    fig.canvas.draw_idle()# calling a function?

for s in (s_yaw, s_sh, s_el):# Classic Loop in the function
    s.on_changed(update)#stating function name
update(None)# no update
plt.show()# to show the plot that has been earlier plit in line
# Robotics in python is actually nice cos it is pushing my python a whole step further, I have to brush up my python
ax.set_xlabel('X'); ax.set_ylabel('Y'); ax.set_zlabel('Z')

# initial angles (deg -> rad)
yaw0, sh0, el0 = 30.0, 20.0, 40.0# initialising the initia values
yaw = np.deg2rad(yaw0); sh = np.deg2rad(sh0); el = np.deg2rad(el0) # Converting degree to radian using an inbuilt function

# plot initial arm
b, j, e = fk_3d(yaw, sh, el) # getting initial position for the parts of the arm
(line,) = ax.plot([b[0], j[0], e[0]],
                  [b[1], j[1], e[1]],
                  [b[2], j[2], e[2]],
                  marker='o', linewidth=3)
txt = ax.text2D(0.02, 0.98, "", transform=ax.transAxes, va="top")# Plotting using the 3D plot

# sliders
ax_yaw = plt.axes([0.15, 0.06, 0.7, 0.02])# Plot ax_ yaw
ax_sh  = plt.axes([0.15, 0.03, 0.7, 0.02])# Plot ax_sh
ax_el  = plt.axes([0.15, 0.00, 0.7, 0.02])# Plot ax_el
# All plots above are in 2D using the Matplotlib. pyplot as plt , Sometimes py in some youtube videos

s_yaw = Slider(ax_yaw, 'yaw (°)', -180, 180, valinit=yaw0)# I dont know explanation for this sha... But I know s_yaw is
# been defined with respect to ax_yaw
s_sh  = Slider(ax_sh,  'shoulder (°)', -179, 179, valinit=sh0)# same with s_sh with respect to ax_sh
s_el  = Slider(ax_el,  'elbow (°)',   -179, 179, valinit=el0)# as well as s_el with ax_el
# Just noticed s in front is for easy identification since it uses sliders, while ax uses axes 3D

def update(_):# defining another function,et me just put it all here
#q1, q2, q0, convert degree to radians for s_yaw but has to be a value that is why.val is  there
    q0 = np.deg2rad(s_yaw.val) #
    q1 = np.deg2rad(s_sh.val)
    q2 = np.deg2rad(s_el.val)
    b, j, e = fk_3d(q0, q1, q2) # using the newly got value to build a 3D Function
    line.set_data_3d([b[0], j[0], e[0]],
                     [b[1], j[1], e[1]],
                     [b[2], j[2], e[2]])# creating an array from the values gotten earlier
    txt.set_text(f"EE: x={e[0]:.3f}, y={e[1]:.3f}, z={e[2]:.3f}\n"
                 f"yaw={s_yaw.val:.1f}°, sh={s_sh.val:.1f}°, el={s_el.val:.1f}°")# Dont really get this line, but
# we limiting the decimal points...
    fig.canvas.draw_idle()# calling a function?

for s in (s_yaw, s_sh, s_el):# Classic Loop in the function
    s.on_changed(update)#stating function name
update(None)# no update
plt.show()# to show the plot that has been earlier plit in line
# Robotics in python is actually nice cos it is pushing my python a whole step further, I have to brush up my python