"""
Extrinsic calibration utilities for camera–LiDAR alignment.

TB3-friendly: real calibration math is left for the agent to implement.
"""

import numpy as np

class Extrinsics:
    def __init__(self, config=None):
        """
        config: optional dictionary containing rotation/translation parameters
        """
        self.config = config or {}

        # Placeholder extrinsics (identity transform)
        self.R = np.eye(3)   # rotation matrix
        self.t = np.zeros((3, 1))  # translation vector

        # Load from config if available
        self._load_from_config()

    def _load_from_config(self):
        """
        Load extrinsic parameters from config.
        """
        if not self.config:
            return

        if "rotation" in self.config:
            self.R = np.array(self.config["rotation"])

        if "translation" in self.config:
            self.t = np.array(self.config["translation"]).reshape(3, 1)

    def transform_lidar_to_camera(self, points):
        """
        Transform LiDAR points into the camera coordinate frame.

        points: Nx3 numpy array

        Returns:
            Nx3 numpy array of transformed points
        """
        # TODO: Implement real LiDAR → camera transformation
        return points @ self.R.T + self.t.T

    def transform_camera_to_lidar(self, points):
        """
        Transform camera-frame points into LiDAR coordinates.

        points: Nx3 numpy array
        """
        # TODO: Implement real camera → LiDAR transformation
        return (points - self.t.T) @ self.R
