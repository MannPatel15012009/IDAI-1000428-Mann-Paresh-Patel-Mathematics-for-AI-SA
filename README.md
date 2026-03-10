# 🚀 Aerospace Data Insights: Rocket Launch Visualization Dashboard

## 🌍 Project Overview

The **Aerospace Data Insights: Mission Dashboard** is an interactive web app built with **Python, Streamlit, and Plotly** to analyze space mission data. It enables users to explore relationships between mission parameters like payload weight, fuel consumption, cost, crew size, duration, and success rates through dynamic, filterable visualizations.

The dashboard includes a **rocket launch simulation** based on **Newton's Second Law (F = ma)**. Users can adjust mass, thrust, fuel, payload, and burn rate to see how these factors affect altitude and velocity over time—with optional atmospheric drag for realism.

The app combines **real-world mission analytics** with **physics-based simulation**, offering an engaging platform to understand aerospace data and rocket dynamics.

---
## Live App Link
 https://idai-1000428-mann-paresh-patel-mathematics-for-ai-sa-ueuqd2t7x.streamlit.app/
## 📊 What Does This Web App Visualise?

This web application visualizes **key relationships between aerospace mission parameters and mission outcomes**.

The dashboard provides insights into how variables such as:

- Payload weight
- Fuel consumption
- Mission cost
- Mission distance
- Mission duration
- Crew size
- Scientific output

impact the **success or failure of space missions**.

Using interactive graphs and filters, users can explore how mission factors correlate with one another and identify patterns within historical space mission data.

Additionally, the application includes a **physics-based rocket launch simulation**, demonstrating how **thrust, fuel mass, payload weight, and air drag influence rocket altitude and velocity** during launch.

---
## 💻Integration Details

Follow these steps to run the app locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/rocket-mission-dashboard.git
```

```
cd rocket-mission-dashboard
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

Create a `requirements.txt` file containing:

```
streamlit
pandas
numpy
plotly
matplotlib
seaborn
```

Then run:

```
pip install -r requirements.txt
```

---

### 4️⃣ Run the Streamlit App

```
streamlit run app.py
```

The application will open automatically in your browser.

Default local URL:

```
http://localhost:8501
```

---

## ☁️ Deployment Instructions
You can deploy this dashboard online for free using **Streamlit Community Cloud**.

---

### Step 1: Push Code to GitHub

Upload the repository to GitHub.

---

### Step 2: Go to Streamlit Cloud

Visit:

```
https://share.streamlit.io
```

Sign in with GitHub.

---

### Step 3: Deploy App

Click **New App** and select:

- Repository
- Branch
- `app.py` file

---

### Step 4: Add Dependencies

Make sure `requirements.txt` exists in the repository.

---

### Step 5: Deploy

Streamlit will automatically install dependencies and deploy the app.

Your app will be accessible via a **public URL**.

---

## ✨ Key Features

### 📊 Interactive Data Visualization
The dashboard includes multiple professional visualizations:

#### 1️⃣ Payload vs Fuel Consumption
A scatter plot that shows how **payload weight affects fuel requirements**.

Insights:
- Larger payloads require significantly more fuel.
- Successful missions tend to cluster around optimal payload-to-fuel ratios.

---

#### 2️⃣ Mission Cost vs Outcome
A bar chart showing **average mission cost for successful vs failed missions**.

Insights:
- Allows comparison of resource investment between mission outcomes.

---

#### 3️⃣ Mission Duration vs Distance
A line graph visualizing how **distance from Earth impacts travel duration**.

Insights:
- Longer distances typically require longer mission durations.
- Shows scaling patterns in deep space missions.

---

#### 4️⃣ Crew Size vs Mission Success Rate
A box plot that categorizes missions into:

- Small Crew (1–20)
- Medium Crew (21–50)
- Large Crew (51+)

Insights:
- Helps determine whether larger crews influence mission success.

---

#### 5️⃣ Correlation Heatmap
A correlation matrix visualizing relationships between all numerical mission variables.

Insights:
- Identifies strong positive and negative correlations between mission parameters.

---

#### 6️⃣ Scientific Yield vs Mission Cost
A scatter plot showing the relationship between:

- Scientific output
- Mission budget

Insights:
- Helps determine whether higher budgets produce more scientific value.

---

### 🚀 Rocket Launch Simulation

The dashboard includes a **rocket physics simulator** that models launch behavior using **Newton's Second Law**:

```
F = ma
```

The simulator calculates rocket motion using:

- Thrust force
- Gravitational force
- Air drag (optional)
- Changing rocket mass due to fuel burn

---

### ⚙️ Adjustable Simulation Parameters

Users can control:

- Rocket Empty Mass
- Engine Thrust
- Initial Fuel
- Payload Weight
- Fuel Burn Rate
- Air Drag (Realism Mode)

---

### 📈 Simulation Outputs

The simulator generates two graphs:

#### Altitude vs Time
Shows how the rocket ascends during launch.

#### Velocity vs Time
Shows the rocket's velocity changes during ascent.

These visualizations help understand **rocket acceleration and flight dynamics**.

---

### 🎛 Dashboard Filters

Users can interactively filter mission data using the sidebar:

- 🚀 **Launch Vehicle Selector**
- 📏 **Distance Slider**
- 🟢 **Show Only Successful Missions**

The dashboard dynamically updates all visualizations based on these filters.

---

## 🧠 Technologies Used

| Technology | Purpose |
|--------|--------|
| Streamlit | Web application framework |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Matplotlib | Scientific plotting |
| Seaborn | Data visualization utilities |

---

## 📂 Project Structure

```
rocket-mission-dashboard
│
├── app.py
├── space_missions_dataset.csv
├── requirements.txt
└── README.md
```

### Files Description

**app.py**

Main Streamlit application containing:

- Data cleaning
- Dashboard interface
- Visualizations
- Rocket simulation

**space_missions_dataset.csv**

Dataset containing mission data including:

- Mission duration
- Payload
- Fuel consumption
- Scientific yield
- Mission cost
- Success rates

---



## 📈 Example Use Cases

This dashboard can be used for:

- Aerospace data analysis
- Data science learning
- Interactive physics demonstrations
- STEM education
- Data visualization portfolios

---

## 🔬 Scientific Concepts Demonstrated

The project demonstrates several key scientific and data science concepts:

#### Newton's Second Law
Used in the rocket simulation.

#### Correlation Analysis
Understanding relationships between mission variables.

#### Data Cleaning
Handling missing values and inconsistent data.

#### Interactive Visualization
Dynamic dashboards for exploratory analysis.

---

## 🎓 Learning Outcomes

By studying this project, users can learn:

- Building interactive dashboards with Streamlit
- Data preprocessing with Pandas
- Visualizing data using Plotly and Matplotlib
- Creating physics-based simulations
- Deploying Python apps to the cloud

---

## Visuals of the App:
<img width="1383" height="630" alt="Screenshot 2026-03-10 183008" src="https://github.com/user-attachments/assets/b627e4a6-81cb-43d2-8af9-2335f697ab9d" />
<img width="1847" height="799" alt="Screenshot 2026-03-10 181935" src="https://github.com/user-attachments/assets/55beec8e-2358-4a1d-a9be-109ad751f68f" />
<img width="1840" height="577" alt="Screenshot 2026-03-10 182035" src="https://github.com/user-attachments/assets/2287cc1d-3db3-4616-b19d-6d0ada9c9b52" />
<img width="1920" height="1080" alt="Screenshot (187)" src="https://github.com/user-attachments/assets/1f649f85-24c3-429c-9555-56b362f850d2" />
<img width="1500" height="533" alt="Screenshot 2026-03-10 182106" src="https://github.com/user-attachments/assets/db58b083-903f-47f3-bd2b-98cff7e7b05c" />
<img width="1332" height="791" alt="Screenshot 2026-03-10 182157" src="https://github.com/user-attachments/assets/cf2a9823-08a1-4c21-94e3-093d525c78e2" />
<img width="1338" height="603" alt="Screenshot 2026-03-10 182231" src="https://github.com/user-attachments/assets/2bef5b49-e7ff-4235-adf9-352cea2a2b03" />
<img width="927" height="545" alt="Screenshot 2026-03-10 182922" src="https://github.com/user-attachments/assets/594a72c5-9b41-421e-acd8-1bf3e56e8e9b" />

## Live Web App Link
[Streamlit App](https://idai-1000428-mann-paresh-patel-mathematics-for-ai-sa-ueuqd2t7x.streamlit.app/)
## 👨‍💻 Author

**Mann Patel**
WACP Candidate Number-1000428
---

## ⭐ Contributing

Contributions are welcome.

You can contribute by:

- Adding new visualizations
- Improving the physics simulation
- Enhancing UI/UX
- Expanding the dataset

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🚀 Future Improvements

Potential future upgrades include:

- Real NASA mission dataset integration
- 3D rocket trajectory simulation
- Machine learning success prediction
- Satellite orbit visualization
- Real-time launch API integration

---

## 🌌 Final Thoughts

The **Aerospace Data Insights Dashboard** combines:

- **data science**
- **interactive visualization**
- **physics simulation**

to create an engaging platform for exploring the science behind space missions.

It demonstrates how **data analytics** and **physics models** can work together to provide meaningful insights into complex aerospace systems.

