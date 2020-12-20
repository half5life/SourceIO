import math

from SourceIO.source1.vmt.shader_base import ShaderBase, Nodes


class Cable(ShaderBase):
    SHADER = 'cable'

    @property
    def basetexture(self):
        texture_path = self._vavle_material.get_param('$basetexture', None)
        if texture_path is not None:
            return self.load_texture_or_default(texture_path, (0.3, 0, 0.3, 1.0))
        return None

    @property
    def bumpmap(self):
        texture_path = self._vavle_material.get_param('$bumpmap', None)
        if texture_path is not None:
            image = self.load_texture_or_default(texture_path, (0.5, 0.5, 1.0, 1.0))
            image.colorspace_settings.is_data = True
            image.colorspace_settings.name = 'Non-Color'
            return image
        return None

    def create_nodes(self, material_name: str):
        if super().create_nodes(material_name) in ['UNKNOWN', 'LOADED']:
            return

        material_output = self.create_node(Nodes.ShaderNodeOutputMaterial)
        shader = self.create_node(Nodes.ShaderNodeBsdfPrincipled)
        self.connect_nodes(shader.outputs['BSDF'], material_output.inputs['Surface'])

        basetexture = self.basetexture
        if basetexture:
            basetexture_node = self.create_node(Nodes.ShaderNodeTexImage, '$basetexture')
            basetexture_node.image = basetexture

            tex_coord_node = self.create_node(Nodes.ShaderNodeTexCoord)
            tex_mapping_node = self.create_node(Nodes.ShaderNodeMapping)
            tex_mapping_node.inputs['Rotation'].default_value = (0, 0, math.radians(90))
            tex_mapping_node.inputs['Scale'].default_value = (25, 1, 1)

            self.connect_nodes(tex_coord_node.outputs['UV'], tex_mapping_node.inputs['Vector'])
            self.connect_nodes(tex_mapping_node.outputs['Vector'], basetexture_node.inputs['Vector'])
            self.connect_nodes(basetexture_node.outputs['Color'], shader.inputs['Base Color'])