import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(14,10))
ax = plt.subplot(1,1,1)
earth = Basemap(projection='mill')
earth.drawcoastlines(color='0.50', linewidth=0.25)
earth.fillcontinents(color='0.93', lake_color=(0.757, 0.824, 0.824))
earth.drawstates(color='0.50', linewidth=0.1)
earth.drawcountries(color='0.50', linewidth=0.25)
earth.drawmapboundary(fill_color=(0.757, 0.824, 0.824))

plt.title("map")
plt.show()