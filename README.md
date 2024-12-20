# plot-boolean-state
pcmesh3.ipynb This is an example notebook to plot boolean state values using matplotlib.axes.Axes.pcolormesh

Use JupyterLab notebook or stand-alone Python to plot a time-series of boolean values. This is similar to signals displayed on an oscilloscope or logic analyzer. This is useful to visualize boolean state variables and events.  This example plots 16 channels of fake data.  

Matplotlib pcolormesh library is used to plot a numpy array of boolean values. pcolormesh is sometimes used to plot mathematical functions in a "heat map" format. Plotting boolean data is simplified verion of that format. Only 2 colors are used.

![Figure 1](https://github.com/user-attachments/assets/8c9db483-4aa7-46b3-9bb4-fb1b872a917d)
![Figure 2](https://github.com/user-attachments/assets/f629c6a6-e093-4808-9714-c459506e44f8)

Next steps (not done):
- Text names for channels (yticks)
- xtick labels get crowded when there are many points in the series. Setup major/minor xticks. Label the major xticks. Optionally mark the minor xticks
- grid lines also get crowded when there are many points in the series.
- Specify color per channel. Change plot array to int type and use the value to select a color.
- Rewrite as a function/method.
- Use parameters/instances to modify preferences

### Alternate plotting method
states3.ipynb file

New and improved method: Use multiple subplots and then filled lines. This is easier to understand and it supports multiple colors. It's easier to manage thousands of time values. Multiple subplots works well for 10 or less variables.
![state_plot](https://github.com/user-attachments/assets/2e5fda84-da06-40e5-a942-482530ad68f9)
