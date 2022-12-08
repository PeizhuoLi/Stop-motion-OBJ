import bpy
from mathutils import Vector
import pickle
import os.path as osp

def insert_keyframe(fcurves, frame, values):
    for fcu, val in zip(fcurves, values):
        fcu.keyframe_points.insert(frame, val, options={'FAST'})

obj = bpy.context.active_object
mesh = obj.data
action = bpy.data.actions.new("MeshAnimation")

mesh.animation_data_create()
mesh.animation_data.action = action

prefix = '/Users/lipei/mount/mine/home/peizhuo/projects/cloth/code/mine/results/massive081/007/000/sequence/'

mesh_sequence_pickle = pickle.load(open(osp.join(prefix, 'mesh_sequence.pkl'), 'rb'))

data_path = "vertices[%d].co"
vec_z = Vector((0.0, 0.0, 1.0))

frames = range(len(mesh_sequence_pickle))

for v in mesh.vertices:
    fcurves = [action.fcurves.new(data_path % v.index, index=i) for i in range(3)]
    co_rest = v.co

    for t in frames:
        verts = mesh_sequence_pickle[t]['vertices']
        # co_kf = Vector((verts[v.index, 0], verts[v.index, 1], verts[v.index, 2]))
        co_kf = verts[v.index]
        insert_keyframe(fcurves, t, co_kf)
