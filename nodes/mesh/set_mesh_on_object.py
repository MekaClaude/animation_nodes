import bpy, bmesh
from ... base_types.node import AnimationNode

class SetMeshOnObject(bpy.types.Node, AnimationNode):
    bl_idname = "mn_SetMeshOnObject"
    bl_label = "Set Mesh on Object"

    inputNames = { "Object" : "object",
                   "Mesh" : "bm" }

    outputNames = { "Object" : "object" }

    def create(self):
        socket = self.inputs.new("mn_ObjectSocket", "Object")
        socket.showName = False
        socket.objectCreationType = "MESH"
        self.inputs.new("mn_MeshSocket", "Mesh")
        self.outputs.new("mn_ObjectSocket", "Object")

    def execute(self, object, bm):
        if object is None: return object
        if object.type == "MESH":
            if object.mode != "OBJECT":
                bpy.ops.object.mode_set(mode = "OBJECT")
            if object.mode == "OBJECT":
                bm.to_mesh(object.data)
        return object