"""
Timestamp synchronization utilities for camera–LiDAR alignment.

TB3-friendly: real interpolation and sync logic left for the agent.
"""

class TimeSync:
    def __init__(self, tolerance_ms=50):
        """
        tolerance_ms: maximum allowed timestamp difference for sync
        """
        self.tolerance_ms = tolerance_ms

    def is_synced(self, ts_cam, ts_lidar):
        """
        Check if camera and LiDAR timestamps are within tolerance.

        ts_cam, ts_lidar: timestamps in milliseconds

        Returns:
            True if synced, False otherwise
        """
        return abs(ts_cam - ts_lidar) <= self.tolerance_ms

    def sync_frames(self, cam_frames, lidar_frames):
        """
        Pair camera and LiDAR frames based on timestamps.

        cam_frames: list of {"timestamp": ...}
        lidar_frames: list of {"timestamp": ...}

        Returns:
            list of (cam_frame, lidar_frame) pairs
        """
        synced = []

        # TODO: Implement real interpolation-based sync
        for cam in cam_frames:
            for lidar in lidar_frames:
                if self.is_synced(cam["timestamp"], lidar["timestamp"]):
                    synced.append((cam, lidar))
                    break

        return synced
