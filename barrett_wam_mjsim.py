#!/usr/bin/env python
#<!--frictional="true" frictionloss=".001"-->
from mujoco_py import load_model_from_path, MjSim, MjViewer, MjSimState
import math
import os
import random
import numpy as np
import time
MODEL_XML = '/home/graspinglab/barrett_wam_mujoco_sim/wam_7dof_wam_bhand.xml'

def extract_pos():
	wam_base_yaw = 0
	wam_shoulder_pitch = 0
	wam_shoulder_yaw = 0
	wam_elbow_pitch = 0
	wam_wrist_yaw = 0
	wam_wrist_pitch = 0
	wam_palm_yaw = 0

	bhand_f1p = 0 # spread
	bhand_f1m = 0
	bhand_f1d = 0
	bhand_f2p = 0
	bhand_f2m = 0
	bhand_f2d = 0
	bhand_f3m = 0
	bhand_f3d = 0


	return np.array([wam_base_yaw, wam_shoulder_pitch, wam_shoulder_yaw, wam_elbow_pitch, wam_wrist_yaw, wam_wrist_pitch, wam_palm_yaw, bhand_f1p, bhand_f1m, bhand_f1d, bhand_f2p, bhand_f2m, bhand_f2d, bhand_f3m, bhand_f3d])


def extract_pos1():
	wam_base_yaw = 1.5777
	wam_shoulder_pitch = 1.1511
	wam_shoulder_yaw = 0
	wam_elbow_pitch = 0.94315678
	wam_wrist_yaw = -3.1276419
	wam_wrist_pitch = 0.5235
	wam_palm_yaw = 1.5587

	bhand_f1p = 0 # spread
	bhand_f1m = 0
	bhand_f1d = 0
	bhand_f2p = 0
	bhand_f2m = 0
	bhand_f2d = 0
	bhand_f3m = 0
	bhand_f3d = 0


	return np.array([wam_base_yaw, wam_shoulder_pitch, wam_shoulder_yaw, wam_elbow_pitch, wam_wrist_yaw, wam_wrist_pitch, wam_palm_yaw, bhand_f1p, bhand_f1m, bhand_f1d, bhand_f2p, bhand_f2m, bhand_f2d, bhand_f3m, bhand_f3d])

# def PD_controller():


model = load_model_from_path(MODEL_XML)
# sim = MjSim(model)
# viewer = MjViewer(sim)
# state = MjSimState()
t = 0
# while True:
#     t += 1
#     sim.step()
#     viewer.render()
#     # sim.data.ctrl[:] = extract_pos()
#     # time.sleep(10)
#     sim.data.ctrl[:] = extract_pos1()
f = open("test1.csv", "r")
traj = f.readlines()
for i in traj:
	print(i.split(',')) 
