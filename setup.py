from os import listdir
from os.path import join, isfile
from setuptools import setup, Extension
from catkin_pkg.python_setup import generate_distutils_setup, parse_package


def list_src(dir_name):
    return [
        join(dir_name, fn)
        for fn in listdir(dir_name)
        if isfile(join(dir_name, fn)) and (fn.endswith('.c') or fn.endswith('.cpp'))
    ]

includes = ['rosbag/include', 'roslz4/include']

rosbag_src = join('rosbag', 'src')
rosbag = Extension(
    'rosbag._rosbag',
    include_dirs=includes,
    #libraries=['lz4'],
    library_dirs=['/usr/lib/x86_64-linux-gnu/'],
    sources=list_src(rosbag_src)
)


roslz4_src = join('roslz4', 'src')
roslz4 = Extension(
    'roslz4._roslz4',
    include_dirs=includes,
    libraries=['lz4'],
    library_dirs=['/usr/lib/x86_64-linux-gnu/'],
    sources=list_src(roslz4_src)
)


d = generate_distutils_setup(
    'rosbag',
    packages=['rosbag'],
    package_dir={'rosbag': rosbag_src},
    scripts=['rosbag/scripts/rosbag'],
    requires=['genmsg', 'genpy', 'roslib', 'rospkg']
)

setup(
    name='roskit',
    packages=['rosbag', 'roslz4', 'rospy', 'roslib'],
    package_dir={
        'rosbag': join(rosbag_src, 'rosbag'),
        'roslz4': join(roslz4_src, 'roslz4'),
        'rospy': 'rospy',
        'roslib': 'roslib'
    },
    scripts=['rosbag/scripts/rosbag'],
    ext_modules=[roslz4],
    requires=['rospkg'],
    setup_requires=['wheel'],
)
