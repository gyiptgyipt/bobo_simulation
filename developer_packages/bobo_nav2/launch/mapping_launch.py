<!--
  Copyright 2016 The Cartographer Authors

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
-->

<launch>
  <!-- Arguments -->
  <arg name="model" default="$(env YOYO_MODEL)" doc="model type [robot1, robot2, robot3, robot4]"/>
  <arg name="laser" default="$(env LASER_MODEL)" doc="model type [ltme_1, ltme_2, lti1, lakibeam, bluesea]"/>
  <!-- <arg name="configuration_basename" default="yoyo_map_2d.lua"/> -->
  <arg if="$(eval laser == 'lti1')" name="configuration_basename" value="yoyo_map_70.lua"/>
  <arg unless="$(eval laser == 'lti1')" name="configuration_basename" value="yoyo_map_2d.lua"/>

  <!-- move_base -->
  <include file="$(find yoyo_bringup)/launch/includes/move_base_map.launch">
    <arg name="model" value="$(arg model)" />
  </include>

  <!-- cartographer_node -->
  <node pkg="cartographer_ros" type="cartographer_node" name="cartographer_node" 
        args="-configuration_directory $(find yoyo_bringup)/param
              -configuration_basename $(arg configuration_basename)"
        output="screen">
    <!--remap from="points2" to="/camera/depth/points" / -->
  </node>

  <!-- cartographer_occupancy_grid_node -->
  <node pkg="cartographer_ros" type="cartographer_occupancy_grid_node"
        name="cartographer_occupancy_grid_node" 
        args="-resolution 0.05" />

  <node name="mode_assist" pkg="yoyo_bringup" type="mode_assist.py" output="screen">
    <param name="mode" value="mapping_mode" />
  </node>
  
</launch>