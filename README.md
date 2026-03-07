# 🚀 Aerospace Data Insights: Rocket Launch Visualization Dashboard

## 🌍 Live App Overview
This project is an **interactive data visualizaton and physics simulation dashboard** built using **Streamlit, Plotly, Matplotlib, and Pandas**.

The application analyzes historical **space mission data** and visualizes relationships between mission parameters such as:

- Payload weight
- Fuel consumption
- Mission cost
- Scientific yield
- Crew size
- Mission success rates
- Mission distance
- Mission duration

In addition, the dashboard includes a **rocket launch simulation** based on **Newton’s Second Law of Motion**, allowing users to experiment with rocket parameters and visualize altitude and velocity over time.

---

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

## 💻 Local Installation & Deployment

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

## ☁️ Deploying on Streamlit Cloud

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

## 📷 Dashboard Preview

Add your **Storyboard or Dashboard Screenshots here**.

Example:

```
![Dashboard Screenshot](images/dashboard.png)
```

or

```
![Storyboard](images/storyboard.png)
```

Create a folder named:

```
images
```

inside the repository and place screenshots there.

---

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

It demonstrates how data analytics and physics models can work together to provide meaningful insights into complex aerospace systems.

