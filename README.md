# Disk Scheduling Visualizer

A web-based analytical tool for visualizing and calculating Disk Scheduling algorithms. This project demonstrates how Operating Systems manage R/W head movements to optimize data retrieval from hard disk drives.

## Features

* **Interactive Visualization**: Real-time plotting of the R/W head path using Chart.js.
* **Multiple Algorithms**:
    * FCFS (First Come First Serve)
    * SSTF (Shortest Seek Time First)
    * SCAN (Elevator Algorithm)
    * C-SCAN (Circular SCAN)
    * LOOK
    * C-LOOK
* **Performance Metrics**:
    * Total Head Movement (Tracks)
    * Average Seek Distance per Request
    * Estimated Execution Time (ms)
* **Customizable Parameters**: User-defined initial head position, request queue, and seek rate.

## Mathematical Model

The system calculates the **Total Head Movement (THM)** using the following formula:

$$THM = \sum_{i=1}^{n} |T_i - T_{i-1}|$$

Where:
* $T_i$ is the track position at step $i$.
* $n$ is the total number of movements in the sequence.

The **Estimated Execution Time** is calculated by:
$$\text{Time} = THM \times \text{Seek Rate}$$

## Tech Stack

* **Backend**: Python 3.x, Flask
* **Frontend**: Tailwind CSS (UI/UX), Chart.js (Data Visualization)
* **Logic**: Python-based algorithmic processing

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/Arjunren/disk-scheduling-visualizer.git](https://github.com/Arjunren/disk-scheduling-visualizer.git)
   cd disk-scheduling-visualizer
   ```

2. **Install dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install flask
   ```

3. **Project Structure**:
   ```text
   .
   ├── app.py              # Flask server and algorithm logic
   ├── templates/
   │   └── index.html      # Frontend with Tailwind & Chart.js
   └── README.md
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Enter the **Initial R/W Head Position** (e.g., 50).
2. Enter the **Request Queue** as a comma-separated list of track numbers (e.g., 82, 170, 43, 140).
3. Select the desired **Algorithm** from the dropdown menu.
4. Set the **Seek Rate** (milliseconds per track).
5. Click **Analyze & Visualize** to generate the path and analytics.

---
