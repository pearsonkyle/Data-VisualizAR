import bpy
import colorsys
from math import sqrt, pi, sin, ceil
from random import TWOPI

# Number of cubes.
count = 16

# Size of grid.
extents = 8.0

# Spacing between cubes.
padding = 0.002

# Size of each cube.
# The height of each cube will be animated, so we'll specify the minimum and maximum scale.
sz = (extents / count) - padding
minsz = sz * 0.25
maxsz = sz * extents
diffsz = maxsz - minsz

# To convert abstract grid position within loop to real-world coordinate.
jprc = 0.0
kprc = 0.0
countf = 1.0 / (count - 1)
diffex = extents * 2

# Position of each cube.
y = 0.0
x = 0.0

# Center of grid.
centerz = 0.0
centery = 0.0
centerx = 0.0

# Distances of cube from center.
# The maximum possible distance is used to normalize the distance.
rise = 0.0
run = 0.0
normdist = 0.0
maxdist = sqrt(2 * extents * extents)

# For animation, track current frame, specify desired number of key frames.
currframe = 0
fcount = 10
invfcount = 1.0 / (fcount - 1)

# If the default frame range is 0, then default to 1 .. 150.
frange = bpy.context.scene.frame_end - bpy.context.scene.frame_start
if frange == 0:
    bpy.context.scene.frame_end = 150
    bpy.context.scene.frame_start = 0
    frange = 150

# Number of keyframes per frame.
fincr = ceil(frange * invfcount)

# For generating the wave.
offset = 0.0
angle = 0.0

# Loop through grid y axis.
for j in range(0, count, 1):
    jprc = j * countf
    y = -extents + jprc * diffex

    # Calculate rise.
    rise = y - centery
    rise *= rise

    # Loop through grid x axis.
    for k in range(0, count, 1):
        kprc = k * countf
        x = -extents + kprc * diffex

        # Calculate run.
        run = x - centerx
        run *= run

        # Find normalized distance using Pythogorean theorem.
        # Remap the normalized distance to a range -PI .. PI
        normdist = sqrt(rise + run) / maxdist
        offset = -TWOPI * normdist + pi

        # Add grid world position to cube local position.
        bpy.ops.mesh.primitive_cube_add(location=(centerx + x, centery + y, centerz), radius=sz)

        # Remember and rename the current object being edited.
        current = bpy.context.object
        current.name = 'Cube ({0:0>2d}, {1:0>2d})'.format(k, j)
        current.data.name = 'Mesh ({0:0>2d}, {1:0>2d})'.format(k, j)

        # Create a material and add it to the current object.
        mat = bpy.data.materials.new(name='Material ({0:0>2d}, {1:0>2d})'.format(k, j))
        mat.diffuse_color = colorsys.hsv_to_rgb(normdist, 0.875, 1.0)
        current.data.materials.append(mat)

        # Track the current key frame.
        currframe = bpy.context.scene.frame_start
        for f in range(0, fcount, 1):

            # Convert the keyframe into an angle.
            fprc = f * invfcount
            angle = TWOPI * fprc

            # Set the scene to the current frame.
            bpy.context.scene.frame_set(currframe)

            # Change the scale.
            # sin returns a value in the range -1 .. 1. abs changes the range to 0 .. 1. 
            # The values are remapped to the desired scale with min + percent * (max - min).
            current.scale[2] = minsz + abs(sin(offset + angle)) * diffsz

            # Insert the key frame for the scale property.
            current.keyframe_insert(data_path='scale', index=2)

            # Advance by the keyframe increment to the next keyframe.
            currframe += fincr