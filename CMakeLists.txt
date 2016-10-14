cmake_minimum_required(VERSION 2.8.3)
project(agv2_control)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  roslib
  rosbag
  std_msgs
  urdf
)

find_package(Boost REQUIRED COMPONENTS thread)

catkin_package(
  CATKIN_DEPENDS roscpp roslib std_msgs urdf
  DEPENDS
)

#~ add_executable(htcbot_control_move src/control_move.cpp)
#~ add_executable(htcbot_move_pattern src/move_pattern.cpp)

#~ target_link_libraries(htcbot_control_move
  #~ ${catkin_LIBRARIES}
#~ )

#~ target_link_libraries(htcbot_move_pattern
  #~ ${catkin_LIBRARIES}
#~ )

install(DIRECTORY config
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
