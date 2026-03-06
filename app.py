import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. PAGE SETUP & LAYOUT ---
st.set_page_config(page_title="Rocket Launch Dashboard", layout="wide", page_icon="🚀")
st.title("🚀 Aerospace Data Insights: Mission Dashboard")
st.markdown("Explore how factors like fuel, payload, cost, and success rates connect across past space missions.")

# --- 2. DATA LOADING & CLEANING (Stage 2) ---
@st.cache_data
def load_and_clean_data(filepath="space_missions_dataset.csv"):
    df = pd.read_csv(filepath)
    
    # Convert launch dates to proper date format
    df['Launch Date'] = pd.to_datetime(df['Launch Date'], errors='coerce')
    
    # Create an Outcome column based on success percentage (>= 90% is Success)
    df['Outcome'] = df['Mission Success (%)'].apply(lambda x: 'Success' if x >= 90 else 'Failure')
    
    return df

# Load the dataframe
df = load_and_clean_data()

# --- 3. SIDEBAR CONTROLS ---
st.sidebar.header("Dashboard Filters")
st.sidebar.markdown("Filter the dataset to explore specific scenarios.")

# Dropdown Filter for Launch Vehicle
selected_vehicle = st.sidebar.selectbox(
    "Select Launch Vehicle", 
    ["All"] + df['Launch Vehicle'].dropna().unique().tolist()
)

# Slider Filter for Distance
min_dist = float(df['Distance from Earth (light-years)'].min())
max_dist = float(df['Distance from Earth (light-years)'].max())
selected_dist = st.sidebar.slider(
    "Max Distance from Earth (light-years)", 
    min_value=min_dist, max_value=max_dist, value=max_dist
)

# Apply filters
filtered_df = df.copy()
if selected_vehicle != "All":
    filtered_df = filtered_df[filtered_df['Launch Vehicle'] == selected_vehicle]
filtered_df = filtered_df[filtered_df['Distance from Earth (light-years)'] <= selected_dist]

st.sidebar.write(f"**Total Missions Displayed:** {len(filtered_df)}")

# --- 4. COMPULSORY VISUALIZATIONS (Stage 4) ---
st.header("📊 Real-World Mission Analysis")
st.markdown("These visualizations plot the exact data points from the CSV dataset.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Payload vs. Fuel Consumption")
    # Scatter Plot using Plotly
    fig1 = px.scatter(
        filtered_df, x='Payload Weight (tons)', y='Fuel Consumption (tons)', 
        color='Outcome', hover_data=['Mission Name'],
        title="Heavier payloads generally require more fuel"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("2. Mission Cost: Success vs. Failure")
    # Bar Chart using Plotly
    cost_by_outcome = filtered_df.groupby('Outcome', as_index=False)['Mission Cost (billion USD)'].mean()
    fig2 = px.bar(
        cost_by_outcome, x='Outcome', y='Mission Cost (billion USD)', 
        color='Outcome', title="Average Cost by Mission Outcome"
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("3. Mission Duration vs. Distance")
    # Line Chart using Seaborn
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.lineplot(data=filtered_df, x='Distance from Earth (light-years)', y='Mission Duration (years)', ax=ax3, color='indigo')
    ax3.set_title("How Distance Impacts Travel Time")
    st.pyplot(fig3)

with col4:
    st.subheader("4. Crew Size vs. Mission Success %")
    # Box Plot using Seaborn
    # Binning crew sizes so the box plot looks clean
    filtered_df['Crew Category'] = pd.qcut(filtered_df['Crew Size'], q=3, labels=['Small', 'Medium', 'Large'], duplicates='drop')
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=filtered_df, x='Crew Category', y='Mission Success (%)', ax=ax4, palette="Set2")
    ax4.set_title("Success Rates by Crew Size Category")
    st.pyplot(fig4)

st.subheader("5. Scientific Yield vs. Mission Cost")
# Scatter/Bar Chart using Matplotlib
fig5, ax5 = plt.subplots(figsize=(10, 5))
ax5.scatter(filtered_df['Mission Cost (billion USD)'], filtered_df['Scientific Yield (points)'], alpha=0.6, c='teal', edgecolors='w', s=80)
ax5.set_xlabel("Mission Cost (billion USD)")
ax5.set_ylabel("Scientific Yield (points)")
ax5.set_title("Scientific Return against Financial Investment")
ax5.grid(True, linestyle='--', alpha=0.5)
st.pyplot(fig5)

# --- 5. ROCKET LAUNCH SIMULATION (Stage 3) ---
st.header("⚙️ Rocket Launch Path Simulation")
st.markdown("---")
st.markdown("This simulation applies Newton's Second Law to calculate acceleration as the difference between upward thrust and downward forces (gravity), divided by rocket mass.")

sim_col1, sim_col2 = st.columns([1, 2])

with sim_col1:
    st.markdown("### Initial Conditions")
    initial_mass = st.number_input("Rocket Empty Mass (kg)", value=50000)
    thrust = st.number_input("Engine Thrust (N)", value=2500000) 
    initial_fuel = st.number_input("Initial Fuel (kg)", value=100000)
    payload = st.number_input("Payload Weight (kg)", value=5000)
    burn_rate = st.slider("Fuel Burn Rate (kg per step)", 50, 1000, 500)
    steps = 200

    run_sim = st.button("🚀 Run Simulation", type="primary")

with sim_col2:
    if run_sim:
        time_data, alt_data, vel_data = [], [], []
        velocity, altitude = 0.0, 0.0
        gravity = 9.81
        current_fuel = initial_fuel
        
        for t in range(steps):
            total_mass = initial_mass + payload + current_fuel
            
            if current_fuel > 0:
                current_thrust = thrust
                current_fuel = max(0, current_fuel - burn_rate)
            else:
                current_thrust = 0  
                
            force_gravity = total_mass * gravity
            net_force = current_thrust - force_gravity
            
            if altitude <= 0 and net_force < 0:
                acceleration, velocity, altitude = 0, 0, 0
            else:
                acceleration = net_force / total_mass
                velocity += acceleration
                altitude += velocity
            
            if altitude < 0:
                altitude, velocity = 0, 0
                
            time_data.append(t)
            alt_data.append(altitude)
            vel_data.append(velocity)

        sim_df = pd.DataFrame({'Time Step': time_data, 'Altitude (m)': alt_data, 'Velocity (m/s)': vel_data})
        
        st.markdown("### Flight Trajectory Results")
        
        fig_alt = px.line(sim_df, x='Time Step', y='Altitude (m)', title="Altitude over Time")
        fig_alt.update_traces(line_color='#1f77b4')
        st.plotly_chart(fig_alt, use_container_width=True)
        
        fig_vel = px.line(sim_df, x='Time Step', y='Velocity (m/s)', title="Velocity over Time")
        fig_vel.update_traces(line_color='#ff7f0e')
        st.plotly_chart(fig_vel, use_container_width=True)
        
        col_res1, col_res2 = st.columns(2)
        col_res1.success(f"**Max Altitude:** {max(alt_data):,.0f} m")
        col_res2.info(f"**Max Velocity:** {max(vel_data):,.0f} m/s")
