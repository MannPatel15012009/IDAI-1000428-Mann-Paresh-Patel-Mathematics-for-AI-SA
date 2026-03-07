import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# --- 1. PAGE SETUP & LAYOUT ---
st.set_page_config(page_title="Rocket Launch Dashboard", layout="wide", page_icon="🌌")
st.title("🌌 Aerospace Data Insights: Mission Dashboard")
st.markdown("### ✨ Explore how factors like fuel, payload, cost, and success rates connect across past space missions.")

# --- 2. DATA LOADING & CLEANING (Stage 2) ---
@st.cache_data
def load_and_clean_data(filepath="space_missions_dataset.csv"):
    df = pd.read_csv(filepath)
    
    # Clean dates
    df['Launch Date'] = pd.to_datetime(df['Launch Date'], errors='coerce')
    
    # Handle missing values for numeric columns
    numeric_cols = ['Distance from Earth (light-years)', 'Mission Duration (years)', 
                    'Mission Cost (billion USD)', 'Scientific Yield (points)', 
                    'Crew Size', 'Mission Success (%)', 'Fuel Consumption (tons)', 'Payload Weight (tons)']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            df[col] = df[col].fillna(df[col].median())
            
    # Create Outcome column
    df['Outcome'] = df['Mission Success (%)'].apply(lambda x: 'Success' if x >= 90 else 'Failure')
    return df

df = load_and_clean_data()

# --- 3. COLORFUL SIDEBAR CONTROLS ---
st.sidebar.header("🎛️ Dashboard Filters")

# Dropdowns and Sliders
selected_vehicle = st.sidebar.selectbox("🚀 Select Launch Vehicle", ["All"] + df['Launch Vehicle'].dropna().unique().tolist())
min_dist = float(df['Distance from Earth (light-years)'].min())
max_dist = float(df['Distance from Earth (light-years)'].max())
selected_dist = st.sidebar.slider("📏 Max Distance from Earth", min_value=min_dist, max_value=max_dist, value=max_dist)

# CHECKBUTTON 1: Filter successful missions
st.sidebar.markdown("---")
show_successful_only = st.sidebar.checkbox("🟢 Show Only Successful Missions (>= 90%)", value=False)

# Apply filters
filtered_df = df.copy()
if selected_vehicle != "All":
    filtered_df = filtered_df[filtered_df['Launch Vehicle'] == selected_vehicle]
filtered_df = filtered_df[filtered_df['Distance from Earth (light-years)'] <= selected_dist]
if show_successful_only:
    filtered_df = filtered_df[filtered_df['Outcome'] == 'Success']

st.sidebar.success(f"**Total Missions Displayed:** {len(filtered_df)}")

# --- 4. COMPULSORY VISUALIZATIONS & HEATMAP ---
st.header("📊 Real-World Mission Analysis")
outcome_colors = {'Success': '#00CC96', 'Failure': '#EF553B'}

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Payload vs. Fuel Consumption")
    fig1 = px.scatter(filtered_df, x='Payload Weight (tons)', y='Fuel Consumption (tons)', 
                      color='Outcome', color_discrete_map=outcome_colors, title="Payload vs. Fuel Requirements")
    fig1.update_layout(template="plotly_dark")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("2. Mission Cost: Success vs. Failure")
    cost_by_outcome = filtered_df.groupby('Outcome', as_index=False)['Mission Cost (billion USD)'].mean()
    fig2 = px.bar(cost_by_outcome, x='Outcome', y='Mission Cost (billion USD)', 
                  color='Outcome', color_discrete_map=outcome_colors, title="Average Cost by Mission Outcome")
    fig2.update_layout(template="plotly_dark")
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("3. Mission Duration vs. Distance")
    # Sort data by distance to ensure a clean, continuous line graph
    sorted_dist_df = filtered_df.sort_values(by='Distance from Earth (light-years)')
    
    fig3 = px.line(
        sorted_dist_df, 
        x='Distance from Earth (light-years)', 
        y='Mission Duration (years)', 
        markers=True, 
        title="How Distance Impacts Travel Time"
    )
    fig3.update_traces(line_color='#AB63FA', marker=dict(size=2, color='#00E676'))
    fig3.update_layout(template="plotly_dark")
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("4. Crew Size vs. Mission Success %")
    
    # Creating clear, easy-to-understand numerical groups instead of confusing statistical buckets
    bins = [0, 20, 50, np.inf]
    labels = ['Small Crew (1-20)', 'Medium Crew (21-50)', 'Large Crew (51+)']
    filtered_df['Crew Category'] = pd.cut(filtered_df['Crew Size'], bins=bins, labels=labels)
    
    # A clean, straightforward interactive box plot
    fig4 = px.box(
        filtered_df, 
        x='Crew Category', 
        y='Mission Success (%)', 
        color='Crew Category',
        title="Does a larger crew improve success rates?",
        category_orders={"Crew Category": ['Small Crew (1-20)', 'Medium Crew (21-50)', 'Large Crew (51+)']}
    )
    # Removing the legend since the x-axis already explains the categories perfectly
    fig4.update_layout(template="plotly_dark", showlegend=False)
    st.plotly_chart(fig4, use_container_width=True)
st.markdown("---")
st.subheader("🔥 5. Correlation Heatmap: Factors Affecting Success")
numeric_cols = ['Distance from Earth (light-years)', 'Mission Duration (years)', 'Mission Cost (billion USD)', 'Scientific Yield (points)', 'Crew Size', 'Mission Success (%)', 'Fuel Consumption (tons)', 'Payload Weight (tons)']
corr_matrix = filtered_df[numeric_cols].corr()

fig_heatmap = px.imshow(corr_matrix, text_auto=".2f", aspect="auto", color_continuous_scale='Turbo', title="Correlation Matrix")
fig_heatmap.update_layout(template="plotly_dark")
st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown("---")
st.subheader("🔬 6. Scientific Yield vs. Mission Cost")
fig5, ax5 = plt.subplots(figsize=(10, 5))
ax5.scatter(filtered_df['Mission Cost (billion USD)'], filtered_df['Scientific Yield (points)'], alpha=0.8, c='#00E676', edgecolors='w', s=80)
ax5.set_xlabel("Mission Cost (billion USD)")
ax5.set_ylabel("Scientific Yield (points)")
ax5.grid(True, linestyle='--', alpha=0.3)
# Make matplotlib figure dark to match
fig5.patch.set_facecolor('#111111')
ax5.set_facecolor('#111111')
ax5.xaxis.label.set_color('white')
ax5.yaxis.label.set_color('white')
ax5.tick_params(colors='white')
st.pyplot(fig5)

# --- 5. ROCKET LAUNCH SIMULATION ---
st.markdown("---")
st.header("⚙️ Rocket Launch Path Simulation")
st.markdown("Simulating Newton's Second Law with optional Air Drag calculation.")

sim_col1, sim_col2 = st.columns([1, 2])

with sim_col1:
    initial_mass = st.number_input("Rocket Empty Mass (kg)", value=50000)
    thrust = st.number_input("Engine Thrust (N)", value=2500000) 
    initial_fuel = st.number_input("Initial Fuel (kg)", value=100000)
    payload = st.number_input("Payload Weight (kg)", value=5000)
    burn_rate = st.slider("Fuel Burn Rate (kg per step)", 50, 1000, 500)
    
    # CHECKBUTTON 2: Realism Mode (Drag)
    include_drag = st.checkbox("💨 Enable Air Drag (Realism Mode)", value=True)
    
    run_sim = st.button("🚀 IGNITE ENGINE", type="primary", use_container_width=True)

with sim_col2:
    if run_sim:
        time_data, alt_data, vel_data = [], [], []
        velocity, altitude = 0.0, 0.0
        gravity = 9.81
        current_fuel = initial_fuel
        drag_coeff = 0.5 
        
        for t in range(200):
            total_mass = initial_mass + payload + current_fuel
            
            if current_fuel > 0:
                current_thrust = thrust
                current_fuel = max(0, current_fuel - burn_rate)
            else:
                current_thrust = 0  
                
            force_gravity = total_mass * gravity
            force_drag = drag_coeff * (velocity ** 2) if include_drag and velocity > 0 else 0
            
            net_force = current_thrust - force_gravity - force_drag
            
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
        
        fig_alt = px.line(sim_df, x='Time Step', y='Altitude (m)', title="Altitude over Time")
        fig_alt.update_traces(line_color='#00E676', line_width=4)
        fig_alt.update_layout(template="plotly_dark")
        st.plotly_chart(fig_alt, use_container_width=True)
        
        fig_vel = px.line(sim_df, x='Time Step', y='Velocity (m/s)', title="Velocity over Time")
        fig_vel.update_traces(line_color='#FF3D00', line_width=4)
        fig_vel.update_layout(template="plotly_dark")
        st.plotly_chart(fig_vel, use_container_width=True)
