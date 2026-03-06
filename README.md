# 🚀 Aerospace Data Insights: Rocket Launch Visualization Dashboard

## ➢ Project Overview
This project is an interactive, data-driven Streamlit web application developed for Aerospace Data Insights. The primary goal of this dashboard is to visualize, compare, and analyze different aspects of simulated past space missions. By combining simulated physics results with exploratory data analysis (EDA) on mission data, this project provides a hands-on approach to real-world aerospace problem-solving. Users—such as engineers or mission planners—can explore how factors like fuel consumption, payload capacity, financial cost, and crew sizes correlate with mission success rates.

 ## ➢ Live Web App Link
🔗 https://idai-1000428-mann-paresh-patel-mathematics-for-ai-sa-ueuqd2t7x.streamlit.app/
## ➢ Core Features & Functional Modules
The application is divided into three functional modules:

### 1. Interactive Dynamic Filtering
* **Launch Vehicle Filter:** A dropdown menu allowing users to isolate mission data based on specific launch vehicles (e.g., SLS, Starship, Falcon Heavy, Ariane 6).
* **Mission Distance Filter:** A dynamic slider enabling users to filter missions based on their maximum distance from Earth (in light-years).
* **Real-time Data Updates:** All connected visualizations instantly update based on the selected constraints.

### 2. Exploratory Data Analysis (EDA)
The dashboard features five compulsory statistical visualizations mapped from the `space_missions_dataset.csv` file:
* **Payload vs. Fuel Consumption (Scatter Plot):** Visualizes the correlation between heavier payloads and increased fuel requirements, color-coded by mission success.
* **Mission Cost: Success vs. Failure (Bar Chart):** Compares the average financial investment of successful missions against failed ones.
* **Mission Duration vs. Distance (Line Chart):** Maps how travel time scales with distance from Earth.
* **Crew Size vs. Mission Success (Box Plot):** Analyzes statistical distributions to see if larger or smaller crews yield higher success rates.
* **Scientific Yield vs. Mission Cost (Scatter Plot):** Investigates whether higher mission costs guarantee a better scientific return.

### 3. Rocket Launch Physics Simulation
* **Newtonian Mechanics Application:** Simulates rocket launch trajectories applying Newton's Second Law (Force = mass × acceleration).
* **Customizable Parameters:** Users can adjust the rocket's empty mass, engine thrust, initial fuel, payload weight, and fuel burn rate.
* **Dynamic Trajectory Rendering:** Plots real-time Altitude (m) and Velocity (m/s) over time, accounting for gravity and decreasing mass as fuel burns.

## ➢ Integration Details & Tech Stack
This application integrates several modern Python libraries to process data and render a highly interactive user interface.
* **Frontend Framework:** `streamlit` (Powers the web app structure, layout, and interactive widgets).
* **Data Processing:** `pandas` and `numpy` (Used to load, clean, and manipulate the dataset, convert date formats, and handle missing values).
* **Interactive Visualizations:** `plotly.express` and `plotly.graph_objects` (Used for interactive scatter plots, bar charts, and simulation trajectory line graphs).
* **Static/Statistical Visualizations:** `seaborn` and `matplotlib.pyplot` (Used for detailed statistical charts like box plots and line distributions).

## ➢ Project Directory Structure
To ensure the app deploys correctly, the GitHub repository is structured as follows:
```text
├── app.py                            # The main Streamlit Python script
├── space_missions_dataset.csv        # The raw dataset of 500 space missions
├── requirements.txt                  # List of Python dependencies for cloud deployment
└── README.md                         # This documentation file
```
## ➢ Deployment Instructions
### Option A: Local Deployment (Testing)
To run this application on your local machine:

#### Clone the repository:
Download the files to your local machine.

#### Ensure Python is installed: 
Python 3.9 or higher is recommended.

#### Install Dependencies: 
Open your terminal/command prompt, navigate to the project folder, and run:
```bash
pip install -r requirements.txt
```
#### Run the App: 
Execute the following command in the terminal:
``` bash
streamlit run app.py
```
#### View the App: The dashboard will automatically open in your default web browser at http://localhost:8501.

### Option B: Streamlit Cloud Deployment (Live App)
This app is designed to be hosted seamlessly on Streamlit Community Cloud:

Upload app.py, space_missions_dataset.csv, and requirements.txt to a public GitHub repository.

Navigate to Streamlit Community Cloud and log in with your GitHub account.

Click on "Deploy an app".

Select your newly created repository, choose the main branch, and specify app.py as the main file path.

Click Deploy! Streamlit will automatically install the dependencies from your requirements.txt file and launch the app.

