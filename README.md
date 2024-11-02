# Threat Detection with YOLOv5

This project demonstrates how to train a YOLOv5 model for threat detection (specifically, detecting guns and knives) and integrate it into a real-time object detection application using OpenCV.

## Project Structure

* `yolov5`: Contains the YOLOv5 source code (clone from the official repository).
* `dataset`: Contains your dataset of images and labels, along with `data.yaml` and `classes.txt`.
* `best.pt`: Your trained YOLOv5 model weights. [model nomenclature: best-{dataset_size}-{model_size}-{accuracy}]. You can find trained models at `./trained/`
* `threat.py`: The Python script for real-time threat detection using OpenCV.
* `requirements.txt`: Lists the project dependencies.
* `.gitignore`: Specifies files and directories to be ignored by Git.
* `README.md`: This file.

## Setup

1. Clone the YOLOv5 repository:

   ```bash
   git clone [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
   ```
2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```
3. Prepare your dataset:

* Organize your images and labels into a `dataset` folder.
* Create `data.yaml` and `classes.txt` within the `dataset` folder.

4. Train the Model:
    ```bash
    #Run the line in Terminal
    python train.py --weights yolov5s.pt --img 640 --batch 16 --epochs 50 --data ../dataset/data.yaml --cache
    ```

## Run Threat Detection Model
    ```bash
    python threat.py
    ```
## Customization
* Adjust the `threat.py` script to modify detection settings (confidence threshold, labels, etc.).
* Experiment with different YOLOv5 model sizes (`yolov5s.pt`, `yolov5m.pt`, `yolov5l.pt`, `yolov5x.pt`) for varying levels of speed and accuracy.
* Fine-tune the model by adjusting hyperparameters or using data augmentation techniques.
* Integrate the threat detection functionality into your own applications.