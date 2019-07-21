import bpy
import glob 

file_loc = "C:\\Users\\Kyle\\Documents\\Unity Projects\\SPH_Visualization\\Assets\\Python\\Data-VisualizAR\\static\\models\\"
files = glob.glob(file_loc+"*.x3d")
print(files)

objs = [] 

imported_object = bpy.ops.import_scene.x3d(filepath=files[0])
obj = bpy.context.selected_objects[0]
objs.append( obj) 

#bpy.data.objects[obj.name].select = True   
#bpy.ops.object.delete()
