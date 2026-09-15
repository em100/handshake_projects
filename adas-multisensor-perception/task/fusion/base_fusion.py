"""
Base interface for all fusion strategies.
"""

class FusionBase:
    def __init__(self, config):
        self.config = config

    @staticmethod
    def create(config):
        if config["type"] == "early":
            from fusion.early_fusion import EarlyFusion
            return EarlyFusion(config)
        elif config["type"] == "late":
            from fusion.late_fusion import LateFusion
            return LateFusion(config)
        else:
            raise ValueError("Unknown fusion type")

    def fuse(self, camera_features, lidar_features):
        """
        Abstract fusion method.
        """
        raise NotImplementedError
