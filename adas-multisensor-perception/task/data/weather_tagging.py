"""
Weather tagging utilities for ADAS perception evaluation.

This module provides lightweight helpers for:
- Assigning weather labels to scenes
- Basic heuristics for weather classification
- Integration with evaluation harnesses

TB3-friendly: real weather detection logic is left for the agent to implement.
"""

class WeatherTagger:
    def __init__(self, config=None):
        """
        config: optional dictionary containing weather-scene mappings
        """
        self.config = config or {}

    def tag_scene(self, scene_id):
        """
        Return the weather tag for a given scene_id.

        If config contains explicit mappings:
            config["weather_conditions"][weather] = [scene1, scene2, ...]

        Otherwise, return a placeholder tag.
        """
        if self.config and "weather_conditions" in self.config:
            for weather, scenes in self.config["weather_conditions"].items():
                if scene_id in scenes:
                    return weather

        # TODO: Implement automatic weather classification
        return "unknown"

    def classify_frame(self, frame):
        """
        Classify weather for a single frame.

        frame: dictionary containing camera/lidar data

        Returns:
            "clear", "rain", "fog", "night", or "unknown"
        """
        # TODO: Implement real weather heuristics (brightness, noise, etc.)
        return "unknown"

    def tag_sequence(self, frames):
        """
        Assign weather tags to an entire sequence of frames.

        Returns:
            {
                "scene_weather": <tag>,
                "frame_tags": [tag1, tag2, ...]
            }
        """
        frame_tags = [self.classify_frame(f) for f in frames]

        # Simple heuristic: majority vote
        scene_weather = self._majority_vote(frame_tags)

        return {
            "scene_weather": scene_weather,
            "frame_tags": frame_tags
        }

    def _majority_vote(self, tags):
        """
        Return the most common tag in a list.
        """
        if not tags:
            return "unknown"

        counts = {}
        for t in tags:
            counts[t] = counts.get(t, 0) + 1

        return max(counts, key=counts.get)
