
"""
NuScenes dataset loader.
Returns synchronized camera + LiDAR frames in a clean dictionary format.
"""

import os

class NuScenesLoader:
    def __init__(self, root):
        self.root = root

    def load_scene(self, scene_id):
        """
        Load synchronized frames for a given scene.
        Returns a list of dictionaries:
        [
            {
                "timestamp": ...,
                "camera": <raw camera frame>,
                "lidar": <raw lidar pointcloud>,
                "metadata": {...}
            },
            ...
        ]
        """

        # TODO: Replace with real NuScenes API calls.
        # For TB3, we provide a realistic skeleton.

        scene_path = os.path.join(self.root, scene_id)

        # Placeholder: list of timestamps in the scene
        timestamps = self._load_timestamps(scene_path)

        frames = []
        for ts in timestamps:
            cam = self._load_camera_frame(scene_path, ts)
            lidar = self._load_lidar_frame(scene_path, ts)

            frame = {
                "timestamp": ts,
                "camera": cam,
                "lidar": lidar,
                "metadata": {
                    "scene_id": scene_id,
                    "frame_id": ts,
                }
            }

            frames.append(frame)

        return frames

    def _load_timestamps(self, scene_path):
        """
        TODO: Load timestamps from NuScenes scene metadata.
        For now, return a placeholder list.
        """
        return ["000001", "000002", "000003"]

    def _load_camera_frame(self, scene_path, ts):
        """
        TODO: Load camera image from disk or NuScenes API.
        For now, return a placeholder object.
        """
        return {
            "raw": None,          # replace with actual image array
            "path": f"{scene_path}/camera/{ts}.jpg"
        }

    def _load_lidar_frame(self, scene_path, ts):
        """
        TODO: Load LiDAR pointcloud from disk or NuScenes API.
        For now, return a placeholder object.
        """
        return {
            "raw": None,          # replace with actual pointcloud array
            "path": f"{scene_path}/lidar/{ts}.pcd"
        }
