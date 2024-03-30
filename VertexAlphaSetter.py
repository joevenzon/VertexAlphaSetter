bl_info = {
    "name": "Vertex Alpha Setter",
    "author": "Matías Avilés Pollak",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Tools",
    "description": "Paints Alpha Vertex in a specific tone",
    "doc_url": "https://github.com/Desayuno64/VertexAlphaSetter",
    "category": "Vertex Paint",
}

import bpy
import bmesh

def set_vertex_alpha(alpha):
    import bpy
    assert bpy.context.mode == 'PAINT_VERTEX'
    mesh = bpy.context.object.data
    ca = mesh.color_attributes.active_color
    if ca.domain == 'POINT':
        for vi, v in enumerate(mesh.vertices):
            if v.select:
                ca.data[vi].color[3] = alpha
    elif ca.domain == 'CORNER':
        for li, l in enumerate(mesh.loops):
            if mesh.vertices[l.vertex_index].select:
                ca.data[li].color[3] = alpha

class SetVertexAlphaOperator(bpy.types.Operator):
    """Set the alpha value of selected vertices"""
    bl_idname = "object.set_vertex_alpha"
    bl_label = "Set Vertex Alpha"

    def execute(self, context):
        set_vertex_alpha(context.scene.alpha_value)
        return {'FINISHED'}

class VIEW3D_PT_VertexAlphaSetter(bpy.types.Panel):
    bl_label = "Vertex Alpha Setter"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"
    
    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, 'alpha_value')
        layout.operator("object.set_vertex_alpha")

def register():
    bpy.utils.register_class(SetVertexAlphaOperator)
    bpy.utils.register_class(VIEW3D_PT_VertexAlphaSetter)
    bpy.types.Scene.alpha_value = bpy.props.FloatProperty(name="Alpha Value", default=0.5)

def unregister():
    bpy.utils.unregister_class(SetVertexAlphaOperator)
    bpy.utils.unregister_class(VIEW3D_PT_VertexAlphaSetter)
    del bpy.types.Scene.alpha_value

if __name__ == "__main__":
    register()
