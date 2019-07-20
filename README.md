# Data-VisualizAR
Visualize 3D models (.obj) or data using augmented reality on your mobile phone through the web with [AR.js](https://github.com/jeromeetienne/AR.js)

- :iphone: Open this link on your phone [https://tinyurl.com/web-ar-obj](https://pearsonkyle.github.io/Data-VisualizAR/static/github.html)

- :camera: Point camera at picture below 

![](static/patterns/pattern-earth.png)

## Web server
```python 
python web_ar.py
``` 

URL Paths: 
```
/
/model
/video
/models/<name>
```

## Coming Soon
AR & VR visualizations of planetary collisions from SPH simulations 

### [Web-AR](https://github.com/jeromeetienne/AR.js)

![](static/videos/sph_visualization.gif)

### [Web-VR](https://aframe.io/)
![](static/videos/sph_web_vr.gif)

### [Unity](https://unity.com/)
![](static/videos/unity_sph.gif)

## Converting [Paraview](https://www.paraview.org/) Models to [Blender](https://www.blender.org/) (.x3d -> .obj)

1. Open Blender (v2.79)
2. Navigate to script editor (crtl+right arrow)x3
3. Open new script. Press button "+ New"
4. Delete the square model, if present
5. Paste code below 
```python
import bpy
import glob 

file_loc = "C:\\Users\\Kyle\\Documents\\SPH_objects\\"
files = glob.glob(file_loc+"*.x3d")
for i in range(len(files)):

    imported_object = bpy.ops.import_scene.x3d(filepath=files[i])
    obj = bpy.context.selected_objects[0]
    exported_object = bpy.ops.export_scene.obj(filepath=files[i].split('.x3d')[0]+'.obj')

    print('Imported name: ', obj.name)
    bpy.data.objects[obj.name].select = True   
    bpy.ops.object.delete()
    
```
See Reference ![image](static/videos/blender_reference.png)

## Creating an animation from multiple obj files in Blender 