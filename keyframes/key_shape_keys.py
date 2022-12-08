import bpy
from mathutils import Vector
import pickle
import os.path as osp


obj = bpy.context.active_object

prefix = '/Users/lipei/mount/mine/home/peizhuo/projects/cloth/code/mine/results/massive081/007/000/sequence/'

mesh_sequence_pickle = pickle.load(open(osp.join(prefix, 'mesh_sequence.pkl'), 'rb'))


frames = range(len(mesh_sequence_pickle))

for i_frame in range(len(mesh_sequence_pickle)):
    block = obj.shape_key_add(name=str(i_frame), from_mix=False)  # returns a key_blocks member
    block.value = 1.0
    block.mute = True
    for (vert, co) in zip(block.data, mesh_sequence_pickle[i_frame]['vertices']):
        vert.co = co

    # keyframe off on frame zero
    block.mute = True
    block.keyframe_insert(data_path='mute', frame=0, index=-1)

    block.mute = False
    block.keyframe_insert(data_path='mute', frame=i_frame + 1, index=-1)

    block.mute = True
    block.keyframe_insert(data_path='mute', frame=i_frame + 2, index=-1)
