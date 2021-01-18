import bpy
import bmesh

# Set in objecte mode
bpy.ops.object.mode_set(mode = 'OBJECT')

# get current mesh
#current_mesh = bpy.context.object.data


# bmesh seems imposible to set vertex color, use a substitution to work like this
#current_mesh = bpy.data.objects['Cube.001'].data
#current_mesh_color = bpy.data.objects['Cube.002'].data

# vert color check
if not current_mesh_color.vertex_colors:
    current_mesh_color.vertex_colors.new()
    
# get vertex color layer this seas to be unuseful when use bmesh and try to set color data by bmesh data
# current_coler_layer = current_mesh.vertex_colors["Col"]
# use a substitution object to cacute the color 
current_coler_layer = current_mesh_color.vertex_colors["Col"]


#--------------------------------------------Bmesh data Get
# create empty bmesh, add current mesh into empty bmesh
current_bm = bmesh.new()
current_bm.from_mesh(current_mesh)
current_bm.faces.ensure_lookup_table()



# TODO: get absolute position
# get location of face (atm it relative to object origin)
# bpy.context.object.matrix_world for world position left muli

i = 0
for face in current_bm.faces:
    
#    #current face center coord
    face_center_coord = face.calc_center_median()
    
    for vert in face.verts:
        # this will loop some repetitive vertex severals times
        
        # get vert index
        current_vert_index = vert.index
        # get vert coord
        current_vert_coord = vert.co
        
        x = face_center_coord.x*0.5+0.5
        y = face_center_coord.y*0.5+0.5
        z = current_vert_coord.z
        
        # Seemingly look like that the vert index is not equale to the color layer index, just use a selfradd varible can work well
        # Unity use y for up direction, left hand axis
        current_coler_layer.data[i].color = (x, z, y, 1.0)
        
        print(current_vert_index)  # DEBUG
        i+=1

# current_bmesh back to mesh
current_bm.to_mesh(current_mesh)
current_bm.free()
#--------------------------------------------


