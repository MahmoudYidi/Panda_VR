#!/usr/bin/env python

# /***************************************************************************

# **************************************************************************/

import rospy
from future.utils import viewitems # for python2&3 efficient compatibility

from franka_interface import ArmInterface, GripperInterface
from sensor_msgs.msg import Joy
#from franka_dataflow.getch import getch
once = 1

def doing(myvar):
   print(myvar)
   global once
   
   if once == 1:
      once = 0
   
   if myvar[0] == 1:
      c = 'w' 
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))

     
   elif myvar[1] ==1:
      c = '2'
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))


   elif myvar[2] ==1:
      c = '1'
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))

      
   elif myvar[3] ==1:
      c = 'q'
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))


   elif myvar[4] ==1:
      c = '6'
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))


   elif myvar[5] ==1:
      c = 'y'
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))

      
   elif myvar[6] ==1:
      c = 't'
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))

   elif myvar[7] ==1:
      c = '5'
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))


   elif myvar[8] ==1:
      c = '8'
      cmd = bindings[c]
      print(myvar[0])
      if c == '8' or c == 'i' or c == '9':
        cmd[0](cmd[1])
        
        print("command: %s" % (cmd[2],))
      else:
            #expand binding to something like "set_j(right, 'j0', 0.1)"
        cmd[0](*cmd[1])
        print("command: %s" % (cmd[2],))
  
   else:
     c = ''
   

   
def Callback(data):
    myvar = data.axes
    doing(myvar)


def set_j(limb, joint_name, delta):
        joint_command = limb.joint_angles()
        joint_command[joint_name] += delta
        limb.set_joint_positions(joint_command)

def set_g(action):
        if has_gripper:
            if action == "close":
                gripper.close()
            elif action == "open":
                gripper.open()
            elif action == "calibrate":
                gripper.calibrate()

rospy.init_node('rq3_proxy')
limb = ArmInterface()
gripper = GripperInterface(ns = limb.get_robot_params().get_base_namespace())
has_gripper = gripper.exists

joints = limb.joint_names()

bindings = {
        '1': (set_j, [limb, joints[0], 0.01], joints[0]+" increase"),
        'q': (set_j, [limb, joints[0], -0.01], joints[0]+" decrease"),
        '2': (set_j, [limb, joints[1], 0.01], joints[1]+" increase"),
        'w': (set_j, [limb, joints[1], -0.01], joints[1]+" decrease"),
        '3': (set_j, [limb, joints[2], 0.01], joints[2]+" increase"),
        'e': (set_j, [limb, joints[2], -0.01], joints[2]+" decrease"),
        '4': (set_j, [limb, joints[3], 0.01], joints[3]+" increase"),
        'r': (set_j, [limb, joints[3], -0.01], joints[3]+" decrease"),
        '5': (set_j, [limb, joints[4], 0.01], joints[4]+" increase"),
        't': (set_j, [limb, joints[4], -0.01], joints[4]+" decrease"),
        '6': (set_j, [limb, joints[5], 0.01], joints[5]+" increase"),
        'y': (set_j, [limb, joints[5], -0.01], joints[5]+" decrease"),
        '7': (set_j, [limb, joints[6], 0.01], joints[6]+" increase"),
        'u': (set_j, [limb, joints[6], -0.01], joints[6]+" decrease")
     }

if has_gripper:
        bindings.update({
        '8': (set_g, "close", "close gripper"),
        'i': (set_g, "open", "open gripper"),
        '9': (set_g, "calibrate", "calibrate gripper")
        })


while not rospy.is_shutdown():
    rospy.Subscriber("/Arm/Joy", Joy, Callback)
    rospy.sleep(1)
