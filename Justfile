build:
    source /opt/ros/foxy/setup.bash
    colcon build --symlink-install
    source /install/setup.bash

# code cleanup with autoflake
autoflake:
    autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place --ignore-init-module-imports .

# linting with black
black:
    black --line-length 119 ./src

# sort imports with isort
isort: 
    isort --profile black --line-length 119 .

# cleanup + sort + linting
pre-commit: autoflake isort black



