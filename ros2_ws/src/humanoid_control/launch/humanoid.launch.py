from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='humanoid_control',
            executable='vision_node',
            name='vision_node',
            output='screen'
        ),

        Node(
            package='humanoid_control',
            executable='tracker_node',
            name='tracker_node',
            output='screen'
        ),

        Node(
            package='humanoid_control',
            executable='serial_bridge',
            name='serial_bridge',
            output='screen'
        ),

    ])
