



\# Robust Multi-Sensor Perception Pipeline for Adverse-Weather Autonomous Driving



\## Domain

Autonomous driving • Robotics perception • Multi-modal sensor fusion • ML systems engineering



\## Problem Background

Modern ADAS systems degrade sharply in adverse weather such as rain, fog, snow, and nighttime low visibility. Camera-only pipelines fail under illumination changes; LiDAR provides geometric cues but introduces noise and dropouts. Real OEM and Tier-1 teams require robust multi-sensor fusion pipelines that maintain reliable detection and tracking across environmental variability and sensor degradation.



Most open-source stacks lack:

\- Configurable fusion strategies  

\- Weather-aware preprocessing  

\- Runtime sensor-health monitoring  

\- Graceful degradation logic  

\- Realistic evaluation harnesses  



This task requires a modular, testable, production-style perception pipeline.



\## Task Objective

Build a complete perception pipeline that ingests camera + LiDAR data, performs calibration, applies configurable fusion, runs detection + tracking, monitors sensor health, and gracefully degrades under failure. Include a weather-aware evaluation harness and Dockerized execution.



\## Key Requirements

1\. \*\*Data ingestion \& preprocessing\*\*

2\. \*\*Calibration \& synchronization\*\*

3\. \*\*Early + late fusion strategies\*\*

4\. \*\*Detection \& tracking\*\*

5\. \*\*Sensor-health monitoring\*\*

6\. \*\*Graceful degradation logic\*\*

7\. \*\*Weather + failure evaluation harness\*\*

8\. \*\*Reproducible Docker execution\*\*



\## Deliverables

\- Modular codebase under `task/`

\- Fusion, weather, and failure configs

\- Evaluation harness scripts

\- Architecture diagram

\- README.md

\- Dockerfile + run.sh



\## Success Criteria (RTD)

\- Pipeline runs end-to-end in Docker  

\- Fusion strategies switchable via config  

\- Sensor-health + degradation logic functional  

\- Evaluation harness produces metrics  

\- Code is modular and professional  

\- Documentation enables full reproduction  



