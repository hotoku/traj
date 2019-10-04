import folium

map = folium.Map(location=[35.681382, 139.76608399999998], zoom_start=14)
folium.Marker([35.658581, 139.745433], popup='Tokyo tower', icon=folium.Icon(color='blue')).add_to(map)
map.save("1.html")
