from setuptools import setup
from glob import glob

package_name = 'humanoid_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),

        ('share/' + package_name,
         ['package.xml']),

        ('share/' + package_name + '/launch',
         glob('launch/*.py')),

        ('share/' + package_name + '/config',
         glob('config/*.yaml')),

        ('share/' + package_name + '/models',
         glob('models/*')),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='Charan',
    maintainer_email='charan@example.com',

    description='Humanoid Robot Using Edge AI for Real-Time Human Detection and Tracking',

    license='MIT',

    entry_points={
        'console_scripts': [
            'vision_node = humanoid_control.vision_node:main',
            'tracker_node = humanoid_control.tracker_node:main',
            'serial_bridge = humanoid_control.serial_bridge:main',
        ],
    },
)
