# Use the official ROS 2 Humble base image from Docker Hub
FROM ros:humble

# Set environment variables
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    DEBIAN_FRONTEND=noninteractive

# Install additional dependencies
RUN apt-get update && \
    apt-get install -y \
    python3-colcon-common-extensions \
    python3-pip tmux tmuxinator \
    build-essential \
    git vim ros-humble-desktop-full \
    ros-humble-gazebo-ros2-control ros-humble-gazebo-ros2-control-demos \
    ros-humble-ros2-control ros-humble-ros2-control-test-assets \
    ros-humble-ros2-controllers ros-humble-ros2-controllers-test-nodes \
    && rm -rf /var/lib/apt/lists/*

# Create a ROS 2 workspace directory
RUN mkdir -p /ros_ws/src

# Set the working directory to the ROS 2 workspace
WORKDIR /ros2_ws

# Build the workspace (uncomment if you have packages to build)
RUN . /opt/ros/humble/setup.sh && colcon build

# Create a ROS 2 workspace directory
RUN mkdir -p /test_ws/src

# Set the working directory to the ROS 2 workspace
WORKDIR /test_ws

# Build the workspace (uncomment if you have packages to build)
RUN . /opt/ros/humble/setup.sh && colcon build

# Source ROS 2 setup script
RUN echo 'source /opt/ros/humble/setup.bash' >> ~/.bashrc
RUN echo '#export BOBO_MODEL=robot1' >> ~/.bashrc
RUN echo '#export BOBO_MODEL=robot2' >> ~/.bashrc
RUN echo 'export BOBO_MODEL=sim_robot2' >> ~/.bashrc
RUN echo 'alias bb="colcon build --symlink-install && source install/setup.bash"' >> ~/.bashrc
RUN echo 'alias delete_workspace="rm -rf build install log;"' >> ~/.bashrc
RUN echo 'export ROS_DOMAIN_ID=99' >> ~/.bashrc

# Optional: Install Python packages if needed
RUN pip install --no-cache-dir \
    numpy \
    scipy

# Copy local ROS 2 packages into the workspace (if any)
COPY ../bobo* /ros2_ws/src/

# Source ROS 2 setup script
RUN echo 'source /ros2_ws/install/setup.bash' >> ~/.bashrc
RUN echo 'source /test_ws/install/setup.bash' >> ~/.bashrc

# Set entrypoint to the ROS 2 bash shell
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash"]
