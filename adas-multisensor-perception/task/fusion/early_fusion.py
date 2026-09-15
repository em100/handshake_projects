"""
Early feature fusion implementation.
"""

from fusion.base_fusion import FusionBase

class EarlyFusion(FusionBase):
    def __init__(self, config):
        super().__init__(config)

    def fuse(self, camera_features, lidar_features):
        """
        TODO: Implement feature concatenation + MLP.
        """
        pass
