# -*- coding: utf-8 -*-
from traits.api import HasTraits, Button, Instance
from traitsui.api import View, Item, VGroup
from tvtk.pyface.scene_editor import SceneEditor 
from mayavi.tools.mlab_scene_model import MlabSceneModel
from mayavi.core.ui.mayavi_scene import MayaviScene
from mayavi import mlab

class DemoApp(HasTraits):
    plotbutton = Button(u"绘图")
    # mayavi场景
    scene = Instance(MlabSceneModel, ()) 
    
    view = View(
        VGroup(
            # 设置mayavi的编辑器
            Item(name='scene',  
                editor=SceneEditor(scene_class=MayaviScene), 
                resizable=True,
                height=250,
                width=400
            ),
            'plotbutton',
            show_labels=False
        ),
        title=u"在TraitsUI中嵌入Mayavi"
    )
      
    def _plotbutton_fired(self):
        self.plot()
     
    def plot(self):
        mlab.test_mesh() 
    
app = DemoApp()
app.configure_traits()   