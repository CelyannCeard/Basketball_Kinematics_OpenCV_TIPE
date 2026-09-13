<h1 align="center">🏀 Basketball Bounce Analysis via Computer Vision</h1>

<p align="center">
  <i>A Python/OpenCV kinematic analysis tool to calculate the Coefficient of Restitution (COR) of basketballs on various surfaces.</i>
</p>

## 📝 Overview
This project was initially developed as part of a TIPE (Travail d'Initiative Personnelle Encadré) during my preparatory classes at Lycée Les Eucalyptus. 

The primary objective was to determine which combination of basketball material (e.g., rubber, composite leather) and court surface (e.g., concrete, polyurethane, hardwood) provides the best dynamic response for players. To achieve this, I developed a Python script utilizing **OpenCV** to track the ball's trajectory in 960 FPS slow-motion videos, extracting position and time data to calculate the kinematic Coefficient of Restitution (COR).

<br>

## ⚙️ How It Works (The Code)
The repository contains several iterations of the script, fine-tuned (HSV parameters) for different ball colors and lighting conditions. The core logic relies on the following steps:

* **Frame Processing:** The script reads a 960 FPS video frame by frame using `cv2.VideoCapture`.
* **Color Filtering (HSV Mask):** A specific hue, saturation, and value (HSV) range is applied to isolate the basketball from the background (facilitated by a physical green screen used during recording).
* **Barycenter Tracking:** Using `cv2.moments`, the program calculates the centroid of the filtered pixels for each frame, placing a red tracking marker on the ball's center.
* **Data Extraction:** The script prints the elapsed time and the Y-axis pixel position to the console for further data processing.

<br>

## 🔬 Physics & Data Analysis
Once the raw tracking data is exported, the physical analysis is performed:
* **Pixel-to-Meter Calibration:** The pixel positions are converted into real-world meters using a simple cross-multiplication based on the known diameter of a standard size 7 basketball (e.g., 0.244m).
* **Velocity Calculation:** Speeds are calculated as the derivative of position over time during the falling and rising phases.
* **Coefficient of Restitution ($e$):** Calculated as the absolute value of the ratio between the relative speed after the collision and the relative speed before the collision. 
* **Data Filtering:** To ensure accuracy, the exact moment of impact is excluded from the speed averages, as the physical deformation of the ball momentarily alters the center of the pixel mass detected by OpenCV.

<br>

## 📊 Results & Conclusion
By comparing multiple material combinations, the data revealed that a **rubber basketball** bouncing on a **polyurethane-coated concrete floor** yields the highest Coefficient of Restitution (closest to 1), providing the most efficient and consistent bounce for gameplay.

<br>

## 🛠️ Technology Stack
* **Python 3**
* **OpenCV (`cv2`)** for computer vision and image processing.
* **NumPy** for matrix operations and array handling.
* **Microsoft Excel** for plotting kinematic graphs (Position/Time, Velocity/Time) and calculating averages.
