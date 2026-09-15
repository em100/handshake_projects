"""
Runtime status monitor for the ADAS perception pipeline.

Tracks:
- Sensor health signals
- Fusion mode status
- Degradation logic state
- Per-frame runtime metrics

TB3-friendly: real logging, dashboards, and analytics left for the agent.
"""

import time

class StatusMonitor:
    def __init__(self):
        self.history = []

    def record_frame_status(self, frame_timestamp, health, fusion_mode, degradation_state):
        """
        Record the status of a single perception frame.

        frame_timestamp: timestamp of the frame
        health: {"camera": status, "lidar": status}
        fusion_mode: string ("early", "late", "fallback", etc.)
        degradation_state: string describing fallback behavior

        Stores:
            {
                "timestamp": ...,
                "camera_health": ...,
                "lidar_health": ...,
                "fusion_mode": ...,
                "degradation_state": ...,
                "runtime_ms": ...
            }
        """

        entry = {
            "timestamp": frame_timestamp,
            "camera_health": health.get("camera", "unknown"),
            "lidar_health": health.get("lidar", "unknown"),
            "fusion_mode": fusion_mode,
            "degradation_state": degradation_state,
            "runtime_ms": self._compute_runtime()
        }

        self.history.append(entry)

    def _compute_runtime(self):
        """
        Placeholder runtime computation.

        Returns:
            float or None
        """
        # TODO: Replace with real per-frame runtime measurement
        return None

    def summarize(self):
        """
        Produce a summary of the pipeline status history.

        Returns:
            {
                "total_frames": ...,
                "camera_failures": ...,
                "lidar_failures": ...,
                "fallback_frames": ...,
                "fusion_modes_used": {...}
            }
        """

        if not self.history:
            return {}

        camera_fail = sum(1 for h in self.history if h["camera_health"] != "ok")
        lidar_fail = sum(1 for h in self.history if h["lidar_health"] != "ok")
        fallback = sum(1 for h in self.history if h["degradation_state"] != "normal")

        fusion_modes = {}
        for h in self.history:
            mode = h["fusion_mode"]
            fusion_modes[mode] = fusion_modes.get(mode, 0) + 1

        return {
            "total_frames": len(self.history),
            "camera_failures": camera_fail,
            "lidar_failures": lidar_fail,
            "fallback_frames": fallback,
            "fusion_modes_used": fusion_modes
        }

    def export(self, path):
        """
        Export status history to JSON.

        path: output file path
        """
        import json
        with open(path, "w") as f:
            json.dump(self.history, f, indent=4)
