# https://docs.blender.org/api/2.79b/info_quickstart.html
import bpy
import glob 

file_loc = "C:\\Users\\Kyle\\Documents\\Unity Projects\\SPH_Visualization\\Assets\\Python\\Data-VisualizAR\\static\\models\\"
files = glob.glob(file_loc+"*.x3d")

scene = bpy.context.scene
scene.objects.keys()

objs = [] 
for i in range(len(files)):
    imported_object = bpy.ops.import_scene.x3d(filepath=files[i])
    obj = bpy.context.selected_objects[0]
    obj.hide = True
    obj.hide_render = True
    objs.append( obj)

# clean up un-necessary assets 
#for k in bpy.data.objects.keys():
#    bpy.data.objects[k].select = True   
#    bpy.ops.object.delete()

def hide_true(objs,idx):
    for i in range(len(objs)):
        if i == idx:
            objs[i].hide = False
            objs[i].keyframe_insert(data_path="hide")
            objs[i].keyframe_insert(data_path="hide_render")

        else:
            objs[i].hide = True
            objs[i].keyframe_insert(data_path="hide")
            objs[i].keyframe_insert(data_path="hide_render")

for i in range(len(files)):
    scene.frame_set(i*7.5)    
    hide_true(objs,i)

#exported_object = bpy.ops.export_scene.obj(filepath='SPH.obj')
