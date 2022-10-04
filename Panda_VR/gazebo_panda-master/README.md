# Gazebo Panda

## Dependencies

- [franka_panda_description](https://github.com/justagist/franka_panda_description)

## Interface Details

- Hardware interface: hardware_interface/EffortJointInterface
- Transmission interface: transmission_interface/SimpleTransmission
- Controllers:
  - gazebo_panda/effort_joint_position_controller: effort_controllers/JointGroupPositionController
  - gazebo_panda/effort_joint_torque_controller: effort_controllers/JointGroupEffortController
  - gazebo_panda/panda_gripper_controller: effort_controllers/JointGroupPositionController
