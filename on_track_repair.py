#   ASSETTO CORSA ON-TRACK REPAIRS
# 
#   This app allows you to fix your car without having to restart from the box,
#   which could be useful on large open-world maps
#
#   -- MediJaster --

import ac, acsys, itertools
from third_party.sim_info import SimInfo, c_float
from random import randint

info = SimInfo()


app_name = "On Track Repair"
width, height = 200 , 170 # Window x,y

def acMain(ac_version):

    # Actual App Object
    global appWindow
    
    appWindow = ac.newApp(app_name)
    ac.setTitle(appWindow, app_name)
    ac.setSize(appWindow, width, height)

    # Variables
    global title_labels, value_labels, car_repair_array
    car_repair_array = (c_float * 5)(0,0,0,0,0)
    
    title_labels_text = ["Front Bumper", "Rear Bumper", "Left Skirt", "Right Skirt"]
    title_labels, value_labels = [], []
    default_string = "0"


    # Title Labels

    increment = 30

    x_pos = 20
    y_pos = 40

    for label in title_labels_text:
        current_label = ac.addLabel(appWindow, label)
        ac.setPosition(current_label, x_pos, y_pos)
        
        y_pos += increment

        title_labels.append(current_label)

    # Number Labels

    x_pos = 180
    y_pos = 40

    value_labels = []

    for label in title_labels_text:
        current_label = ac.addLabel(appWindow, default_string)
        ac.setPosition(current_label, x_pos, y_pos)
        ac.setFontAlignment(current_label, "right")

        y_pos += increment

        value_labels.append(current_label)

    ac.addRenderCallback(appWindow, acUpdate) # -> links this app's window to an OpenGL render function

    return app_name


def acUpdate(deltaT):

    physics_struct = info.physics
    damage_list = physics_struct.carDamage

    for (label, part_damage) in zip(value_labels, damage_list):
        ac.setText(label,str(round(part_damage,2)))

    physics_struct.carDamage = car_repair_array

    info._acpmf_physics[:] = physics_struct
    info._acpmf_physics.flush()