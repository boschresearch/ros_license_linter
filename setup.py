# Copyright (c) 2022 - for information on the respective copyright owner
# see the NOTICE file and/or the repository https://github.com/boschresearch/ros_license_linter

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="ros_license_linter",
    description="Checks ROS packages for correct license declaration.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Christian Henkel",
    author_email="christian.henkel2@de.bosch.com",
    license="Apache License, Version 2.0",
    url="tbd",
    keywords=["license", "ROS"],
    packages=["ros_license_linter"],
    install_requires=[
        'rospkg',
        'scancode-toolkit',
        'spdx-tools'
    ],
    package_dir={"": "src"},
    data_files=[],
    scripts=["bin/ros_license_linter"]
)
