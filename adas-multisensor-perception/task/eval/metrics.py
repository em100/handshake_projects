"""
Metric computation utilities for ADAS perception evaluation.

TB3-friendly: real metric math left for the agent to implement.
"""

import numpy as np

class Metrics:
    @staticmethod
    def compute_map(detections, ground_truth):
        """
        Compute mean Average Precision (mAP).

        detections: list of predicted bounding boxes
        ground_truth: list of true bounding boxes

        Returns:
            float or None
        """
        # TODO: Implement real mAP computation
        return None

    @staticmethod
    def compute_tracking_accuracy(tracks, gt_tracks):
        """
        Compute tracking accuracy.

        tracks: list of predicted track states
        gt_tracks: list of ground-truth track states

        Returns:
            float or None
        """
        # TODO: Implement real tracking accuracy
        return None

    @staticmethod
    def compute_false_positive_rate(detections, ground_truth):
        """
        Compute false positive rate.

        Returns:
            float or None
        """
        # TODO: Implement real FPR computation
        return None

    @staticmethod
    def compute_latency(timestamps):
        """
        Compute average latency from a list of timestamps.

        timestamps: list of processing times in milliseconds

        Returns:
            float
        """
        if not timestamps:
            return None
        return float(np.mean(timestamps))

    @staticmethod
    def compute_robustness_score(health_signals):
        """
        Compute robustness score based on sensor-health signals.

        health_signals: list of {"camera": status, "lidar": status}

        Returns:
            float or None
        """
        # TODO: Implement real robustness metric
        return None
