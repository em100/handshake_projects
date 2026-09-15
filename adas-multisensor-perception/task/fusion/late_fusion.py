"""
Late decision fusion implementation.
"""

from fusion.base_fusion import FusionBase

class LateFusion(FusionBase):
    def __init__(self, config):
        super().__init__(config)

    def fuse(self, camera_detections, lidar_detections):
        """
        TODO: Implement weighted decision fusion.
        """
        pass
