### prerequirement

install

```
sudo apt-get install ros-indigo-ros-control ros-indigo-ros-controllers
```

### Control the rod

1. roslaunch agv2_control agv2_control.launch

2. publish topics
  - /agv2/ros_front_joint_position_controller/command
  - /agv2/ros_rear_joint_position_controller/command
    - the type is std_msg/Float64
    - the value means the lifted distance (in meter)
