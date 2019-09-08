# https://docs.blender.org/api/2.79b/info_quickstart.html
import bpy
import glob 

file_loc = "C:\\Users\\Kyle\\Documents\\Unity Projects\\SPH_Visualization\\Assets\\Python\\Data-VisualizAR\\static\\models\\"
files = glob.glob(file_loc+"*.x3d")

scene = bpy.context.scene
scene.objects.keys()
bpy.context.scene.render.fps = 5
bpy.context.scene.frame_start = 0
bpy.context.scene.frame_end = len(files)

objs = [] 
for i in range(len(files)):
    imported_object = bpy.ops.import_scene.x3d(filepath=files[i])
    obj = bpy.context.selected_objects[0]
    obj.hide = True
    modifier=obj.modifiers.new('Decimate 0.5','DECIMATE')
    modifier.ratio=0.5
    modifier.use_collapse_triangulate=True
    objs.append( obj)

def hide_true(objs,idx):
    for i in range(len(objs)):
        if i == idx:
            objs[i].hide = False
            objs[i].keyframe_insert(data_path="hide")
        else:
            objs[i].hide = True
            objs[i].keyframe_insert(data_path="hide")

for i in range(len(files)):
    scene.frame_set(i)    
    hide_true(objs,i)

for k in range(len(bpy.data.objects)-1,0,-1):
    if 'Face' not in bpy.data.objects[k].name:
        bpy.data.objects[k].select = True
    else: 
        bpy.data.objects[k].select = False 

bpy.ops.object.delete()