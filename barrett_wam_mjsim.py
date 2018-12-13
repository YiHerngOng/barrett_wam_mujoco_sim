#!/usr/bin/env python
#<!--frictional="true" frictionloss=".001"-->
from mujoco_py import load_model_from_path, MjSim, MjViewer
import math
import os

MODEL_XML = 'wam_7dof_wam_bhand.xml'
# MODEL_XML = '/home/yiherngong/barrett/bhand.xml'

# model = MjModel(MODEL_XML)

# model._compute_subtree()
model = load_model_from_path(MODEL_XML)
sim = MjSim(model)
viewer = MjViewer(sim)
t = 0
while True:
    # sim.data.ctrl[0] = math.cos(t / 10.) * 0.01
    # sim.data.ctrl[1] = math.sin(t / 10.) * 0.01
    t += 1
    sim.step()
    viewer.render()
    # if t>1000:
   	# 	break

    # if t > 100 and os.getenv('TESTING') is not None: