"""
Camera intrinsic calibration utilities.

TB3-friendly: real intrinsic loading and projection math left for the agent.
"""

import numpy as np

class Intrinsics:
    def __init__(self, config=None):
        """
        config: optional dictionary containing fx, fy, cx, cy
        """
        self.config = config or {}

        # Placeholder intrinsics
        self.fx = 1.0
        self.fy = 1.0
        self.cx = 0.0
        self.cy = 0.0

        self._load_from_config()

    def _load_from_config(self):
        """
        Load intrinsic parameters from config.
        """
        self.fx = self.config.get("fx", self.fx)
        self.fy = self.config.get("fy", self.fy)
        self.cx = self.config.get("cx", self.cx)
        self.cy = self.config.get("cy", self.cy)

    def project_points(self, points_3d):
        """
        Project 3D camera-frame points into 2D image coordinates.

        points_3d: Nx3 numpy array

        Returns:
            Nx2 numpy array of pixel coordinates
        """
        # TODO: Implement real pinhole projection
        x = points_3d[:, 0]
        y = points_3d[:, 1]
        z = points_3d[:, 2] + 1e-6  # avoid divide-by-zero

        u = self.fx * (x / z) + self.cx
        v = self.fy * (y / z) + self.cy

        return np.stack([u, v], axis=1)
