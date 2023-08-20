

## Quickstart

###### Create map object

```python
import folium
m = folium.Map(location=[45.5236, -122.6750])
```

###### Options

```python
from rich import inspect

inspect(folium.Map, help=True)

class Map(
  location=None,          
  width='100%',           
  height='100%',          
  left='0%',              
  top='0%',               
  position='relative',    
  tiles='OpenStreetMap',  
  attr=None,              
  min_zoom=0,             
  max_zoom=18,            
  zoom_start=10,          
  min_lat=-90,            
  max_lat=90,             
  min_lon=-180,           
  max_lon=180,            
  max_bounds=False,       
  crs='EPSG3857',         
  control_scale=False,    
  prefer_canvas=False,    
  no_touch=False,         
  disable_3d=False,       
  png_enabled=False,      
  zoom_control=True,      
  **kwargs                
)
```

##### Add Data

```python
#Add a single marker
folium.Marker(location=[df.Latitude.mean(), df.Longitude.mean()]).add_to(map)
```



## Examples

#### folium with Mapbox

> ###### View
>
> ```python
> def get_context_data(self, **kwargs):
>   api_key='pk.....' # mapbox api key
>   tiles='dark-v10'
>   tilesize_pixels = "256" 
>   map_tiles = f"https://api.mapbox.com/styles/v1/mapbox/{tiles}/tiles/{tilesize_pixels}/{{z}}/{{x}}/{{y}}@2x?access_token={api_key}"
>   m = folium.Map(
>     width=800,
>     height=600,
>     zoom_start=6.15,
>     tiles=map_tiles,
>     attr="Mapbox",
>   )
>   url = ("https://raw.githubusercontent.com/python-visualization/folium/main/examples/data")
>   antarctic_ice_edge = f"{url}/antarctic_ice_edge.json"
>   antarctic_ice_shelf_topo = f"{url}/antarctic_ice_shelf_topo.json"
>   folium.GeoJson(antarctic_ice_edge, name="geojson").add_to(m)
>   folium.TopoJson(json.loads(requests.get(antarctic_ice_shelf_topo).text),"objects.antarctic_ice_shelf",name="topojson",).add_to(m)
>   m.get_root().render()
>   map_head: str = m.get_root().header.render()
>   map_body: str = m.get_root().html.render()
>   map_script: str = m.get_root().script.render()
> 
>   context = super(JobDetailView, self).get_context_data(**kwargs)
>   context['map_head'] = map_head
>   context['map_body'] = map_body
>   context['map_script'] = map_script
>   context['map_title'] = 'folium map'
>   return context
> ```
>
> ###### template
>
> ```html
> <!DOCTYPE html>
> <html>
>   <head>
>   	{{ map_head|safe }}
>   </head>
>   <body>
>     <h1>Using components</h1>
>       {{map_title}}
>       {{map_body|safe}}
>     <script>
>       {{ map_script|safe }}
>     </script>
>   </body>
> </html>
> ```



---

### Links

- [Folium 0.14.0 documentation](https://python-visualization.github.io/folium/index.html#)
- [Map Visualization with Folium](https://medium.com/datasciencearth/map-visualization-with-folium-d1403771717) : Medium article with several examples
- [Folium Mapping: Displaying Markers on a Map](https://medium.com/towards-data-science/folium-mapping-displaying-markers-on-a-map-6bd56f3e3420): Add markers with popups
- [How to integrate a map in a Django app using Folium](https://carlosmv.hashnode.dev/how-to-integrate-a-map-in-a-django-app-using-folium).

