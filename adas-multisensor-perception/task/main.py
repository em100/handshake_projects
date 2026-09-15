
"""
Main entry point for the ADAS multi-sensor perception pipeline.
"""

import yaml

# Data ingestion + preprocessing
from data.loaders.nuscenes_loader import NuScenesLoader
from data.preprocessing.camera_preprocess import preprocess_camera
from data.preprocessing.lidar_preprocess import preprocess_lidar

# Core modules
from fusion.base_fusion import FusionBase
from models.detector import Detector
from models.tracker import Tracker

# Runtime modules
from runtime.sensor_health import SensorHealthMonitor
from runtime.degradation_logic import DegradationLogic


class ADASPipeline:
    def __init__(self, config):
        self.config = config

        # Initialize dataset loader
        self.loader = NuScenesLoader(config["data"]["root"])

        # Initialize core modules
        self.fusion = FusionBase.create(config["fusion"])
        self.detector = Detector(config["model"])
        self.tracker = Tracker(config["model"])

        # Runtime modules
        self.sensor_health = SensorHealthMonitor(config["runtime"])
        self.degradation = DegradationLogic(config["runtime"])

    # ----------------------------------------------------------------------
    # Full pipeline execution (used for run.sh)
    # ----------------------------------------------------------------------
    def run(self):
        """
        Execute the full perception pipeline across all scenes listed in config.
        """

        scenes = self.config["eval"]["weather_conditions"]

        for scene_id in scenes:
            print(f"\n--- Processing scene: {scene_id} ---")
            self.run_scene(scene_id)

    # ----------------------------------------------------------------------
    # Scene-level execution (used by evaluation harness)
    # ----------------------------------------------------------------------
    def run_scene(self, scene_id):
        """
        Execute the perception pipeline for a single scene.
        Returns per-frame outputs (placeholder).
        """

        frames = self.loader.load_scene(scene_id)
        outputs = []

        for frame in frames:

            # 1. Preprocess sensors
            cam = preprocess_camera(frame["camera"])
            lidar = preprocess_lidar(frame["lidar"])

            # 2. Sensor health check
            health = self.sensor_health.check({"camera": cam, "lidar": lidar})

            # 3. Fusion
            fused = self.fusion.fuse(cam, lidar)

            # 4. Detection
            detections = self.detector.detect(fused)

            # 5. Tracking
            tracks = self.tracker.track(detections)

            # 6. Degradation logic
            final_output = self.degradation.apply(tracks, health)

            # 7. Collect output
            outputs.append({
                "timestamp": frame["timestamp"],
                "tracks": final_output,
                "health": health,
                "metadata": frame["metadata"]
            })

        return outputs


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------
if __name__ == "__main__":



























