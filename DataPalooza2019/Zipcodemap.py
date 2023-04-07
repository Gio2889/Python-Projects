import shapefile
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import os

cwd=os.getcwd()
sf = shapefile.Reader("tl_2017_us_zcta510")  # or whatever filename

shape_recs = sf.shapeRecords()

fig = plt.figure()
ax = fig.add_subplot(111)

for rec in shape_recs:
    points = rec.shape.points
    d = rec.record  # record MetaData
    zip_code = d[1]
    c = 'b'  # matplotlib blue

    # You can also use a Named, Hex, Greyscale percent, or RGB value
    # c = 'blue'
    # c = '#0033CC'
    # c = '.75'
    # c = (0.0, 0.0, 1.0)

    if zip_code == "68521":  # Coloring in 1 zipcode
        c = 'r'
    patch = patches.Polygon(points,True,label=d[1],color=c)
    ax.add_patch(patch)

ax.autoscale()
plt.axis('off')
plt.savefig("my_map.png")

# %%
