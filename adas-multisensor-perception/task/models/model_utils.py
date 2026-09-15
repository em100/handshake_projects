"""
Utility functions and helper classes for perception models.

Includes:
- Lightweight backbone wrappers
- Feature extraction helpers
- Confidence weighting utilities
- Bounding box operations
- Track state utilities

TB3-friendly: real model logic is left for the agent to implement.
"""

import numpy as np


# ----------------------------------------------------------------------
# Backbone Models (Camera + LiDAR)
# ----------------------------------------------------------------------

class CameraBackbone:
    """
    Placeholder camera feature extractor.
    Real implementation should wrap a CNN (e.g., ResNet, YOLO backbone).
    """

    def __init__(self, config=None):
        self.config = config or {}

    def extract_features(self, image):
        """
        Extract camera features from an image.

        image: preprocessed camera frame

        Returns:
            feature_vector (numpy array)
        """
        # TODO: Implement real CNN feature extraction
        return np.zeros((128,), dtype=float)


class LidarBackbone:
    """
    Placeholder LiDAR feature extractor.
    Real implementation should wrap a voxel encoder or pillar encoder.
    """

    def __init__(self, config=None):
        self.config = config or {}

    def extract_features(self, pointcloud):
        """
        Extract LiDAR features from a pointcloud.

        pointcloud: preprocessed LiDAR frame

        Returns:
            feature_vector (numpy array)
        """
        # TODO: Implement real LiDAR feature extraction
        return np.zeros((128,), dtype=float)


# ----------------------------------------------------------------------
# Confidence Utilities (used in Late Fusion)
# ----------------------------------------------------------------------

def compute_confidence(scores):
    """
    Compute a normalized confidence score.

    scores: list or numpy array of raw model scores

    Returns:
        float in [0, 1]
    """
    if scores is None or len(scores) == 0:
        return 0.0

    # TODO: Replace with real confidence computation
    s = np.mean(scores)
    return float(max(0.0, min(1.0, s)))


def weighted_merge(det_cam, det_lidar, w_cam=0.5, w_lidar=0.5):
    """
    Merge camera + LiDAR detections using weighted confidence.

    det_cam: list of camera detections
    det_lidar: list of LiDAR detections

    Returns:
        merged_detections: list
    """
    # TODO: Implement real weighted merging logic
    return det_cam + det_lidar


# ----------------------------------------------------------------------
# Bounding Box Utilities
# ----------------------------------------------------------------------

def iou(box1, box2):
    """
    Compute Intersection-over-Union (IoU) between two bounding boxes.

    box format: [x1, y1, x2, y2]

    Returns:
        float or None
    """
    # TODO: Implement real IoU computation
    return None


def nms(detections, threshold=0.5):
    """
    Non-Maximum Suppression (NMS) for filtering overlapping detections.

    detections: list of {"bbox": [...], "score": float}

    Returns:
        filtered_detections
    """
    # TODO: Implement real NMS
    return detections


# ----------------------------------------------------------------------
# Track State Utilities
# ----------------------------------------------------------------------

class TrackState:
    """
    Lightweight track state container for Kalman/ByteTrack-style tracking.
    """

    def __init__(self, track_id, bbox, score, timestamp):
        self.track_id = track_id
        self.bbox = bbox
        self.score = score
        self.timestamp = timestamp

    def update(self, bbox, score, timestamp):
        """
        Update track state with new detection.
        """
        # TODO: Implement real track update logic
        self.bbox = bbox
        self.score = score
        self.timestamp = timestamp

    def to_dict(self):
        """
        Convert track state to dictionary for pipeline output.
        """
        return {
            "track_id": self.track_id,
            "bbox": self.bbox,
            "score": self.score,
            "timestamp": self.timestamp
        }
