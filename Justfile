build:
    source /opt/ros/foxy/setup.bash
    colcon build --symlink-install
    source /install/setup.bash

pre-commit:
    # code cleanup
    autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place --ignore-init-module-imports .
    # sort imports
    isort --profile black --line-length 119 .
    #linter
    black --line-length 119 .
    # static type checking
    #    mypy --ignore-missing-imports ./src/

