#### .bashrc
```
#export BOBO_MODEL=robot1
#export BOBO_MODEL=robot2
export BOBO_MODEL=sim_robot2

alias bb='colcon build --symlink-install && source install/setup.bash'
alias delete_workspace='rm -rf build install log; echo "Done"'

export ROS_DOMAIN_ID=99
```

#### how to build
```
 docker build -t romrobotics/humble:bobo .
```
