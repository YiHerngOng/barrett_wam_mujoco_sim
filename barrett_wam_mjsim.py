#!/usr/bin/env python
#<!--frictional="true" frictionloss=".001"-->
from mujoco_py import load_model_from_path, MjSim, MjViewer, MjSimState
import math
import os
import random
import numpy as np

MODEL_XML = 'wam_7dof_wam_bhand.xml'

def extract_pos():
	wam_base_yaw = random.uniform(-2.6, 2.6)
	wam_shoulder_pitch = random.uniform(-1.985,1.985)
	wam_shoulder_yaw = random.uniform(-2.8, 2.8)
	wam_elbow_pitch = random.uniform(-0.9, 3.14159)
	wam_wrist_yaw = random.uniform(-4.55, 1.25)
	wam_wrist_pitch = random.uniform(-1.5707, 1.5707)
	wam_palm_yaw = random.uniform(-3,3)

	bhand_f1p = random.uniform(0, 3.14159) # spread
	bhand_f1m = random.uniform(0, 2.44346)
	bhand_f1d = random.uniform(0, 0.837758)
	bhand_f2p = random.uniform(0, 3.14159)
	bhand_f2m = random.uniform(0, 2.44346)
	bhand_f2d = random.uniform(0, 0.837758)
	bhand_f3m = random.uniform(0, 2.44346)
	bhand_f3d = random.uniform(0, 0.837758)

	return np.array([wam_base_yaw, wam_shoulder_pitch, wam_shoulder_yaw, wam_elbow_pitch, wam_wrist_yaw, wam_wrist_pitch, wam_palm_yaw, bhand_f1p, bhand_f1m, bhand_f1d, bhand_f2p, bhand_f2m, bhand_f2d, bhand_f3m, bhand_f3d])

# def PD_controller():


model = load_model_from_path(MODEL_XML)
sim = MjSim(model)
viewer = MjViewer(sim)
# state = MjSimState()
t = 0
while True:
    t += 1
    sim.step()
    viewer.render()
    sim.data.ctrl[:] = extract_pos()