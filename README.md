# YOLOv3 for RoboCup "What is That" Project

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![YOLOv3](https://img.shields.io/badge/YOLOv3-Darknet-red)
![RoboCup](https://img.shields.io/badge/RoboCup-Open%20Challenge-lightgrey)

## 📌 Project Overview  
This project provides a production-ready YOLOv3 implementation specifically tailored for the object recognition challenge in RoboCup. It focuses on real-time detection and is designed for robotics competitions. Due to the large size of the dataset and weights, they cannot be uploaded here. This repository focuses on the communication and learning aspects of the dataset processing script.  
If you want to learn more about YOLOv3, please refer to the `readme_.md`.

## ⚠️ Dataset & Weights
Due to GitHub restrictions:
- **Competition dataset (15GB)** is available at the [RoboCup Data Portal](http://data.robocup.org).
- **Pretrained weights:**
  - Official YOLOv3 weights:
    ```bash
    wget https://pjreddie.com/media/files/yolov3.weights -P models/
    ```
## 🛠️ Setup & Installation

1. **Create a Conda Environment:**
   ```bash
   conda create -n robocup python=3.7
   conda activate robocup
