from setuptools import setup

package_name = 'empty_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[ # "mount files"
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tlips',
    maintainer_email='thomas.lips@ugent.be',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'empty_python_node = empty_python.empty_python_node:main' # declare 'executable' <name> <package>.<file>:<entry-function>
        ],
    },
)
