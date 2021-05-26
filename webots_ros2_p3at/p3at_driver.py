# Copyright 1996-2021 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""ROS2 P3AT driver."""

import rclpy
#from webots_ros2_core.webots_skid_steer_node import WebotsSkidSteerNode
from .webots_skid_steer_node import WebotsSkidSteerNode

class P3ATDriver(WebotsSkidSteerNode):
    def __init__(self, args):
        super().__init__(
            'p3at_driver',
            args,
            left_encoder='front left wheel sensor',
            left_joint='front left wheel',
            right_encoder='front right wheel sensor',
            right_joint='front right wheel',
            back_left_joint='back left wheel',
            back_right_joint='back right wheel',
            back_left_encoder='back left wheel sensor',
            back_right_encoder='back right wheel sensor',
            robot_base_frame='base_link',
            wheel_distance=0.4,
            wheel_radius=0.11
        )
        self.start_device_manager({
            'robot': {'publish_base_footprint': True},
#            'LDS-01': {'topic_name': '/scan'},
#            'inertial_unit+accelerometer+gyro': {'frame_id': 'imu_link', 'topic_name': '/imu'}
        })


def main(args=None):
    rclpy.init(args=args)
    driver = P3ATDriver(args=args)
    rclpy.spin(driver)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
