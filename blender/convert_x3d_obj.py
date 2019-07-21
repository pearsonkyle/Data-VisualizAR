# https://docs.blender.org/api/2.79b/info_quickstart.html

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
    