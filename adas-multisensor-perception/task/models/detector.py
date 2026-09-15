"""
Detector interface for camera and LiDAR models.
"""

class Detector:
    def __init__(self, config):
        self.config = config
        # TODO: Initialize model(s)

    def detect(self, fused_features):
        """
        TODO: Run detection model.
        """
        pass
