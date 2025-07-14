import plotly.graph_objects as go

# Enhanced data with timeline markers
locations = [
    {'name': 'Zaporizhzhia', 'lat': 47.5075, 'lon': 35.1375, 'radiation_24h': 2.0},
    {'name': 'Dnipro', 'lat': 48.4647, 'lon': 35.0462, 'radiation_24h': 0.4},
    {'name': 'Black Sea', 'lat': 44.0, 'lon': 35.0, 'radiation_24h': 0.07},
    {'name': 'Kars', 'lat': 40.6013, 'lon': 43.0945, 'radiation_24h': 0.02},
    {'name': 'Trabzon', 'lat': 41.0027, 'lon': 39.7178, 'radiation_24h': 0.025},
    {'name': 'Ankara', 'lat': 39.9334, 'lon': 32.8597, 'radiation_24h': 0.005},
    {'name': 'Istanbul', 'lat': 41.0082, 'lon': 28.9784, 'radiation_24h': 0.002}
]

propagation_timeline = [
    {'path': ['Zaporizhzhia', 'Dnipro'], 'time': '6h', 'midpoint_lat': 47.986, 'midpoint_lon': 35.091},
    {'path': ['Dnipro', 'Black Sea'], 'time': '12h', 'midpoint_lat': 46.232, 'midpoint_lon': 35.023},
    {'path': ['Black Sea', 'Kars'], 'time': '24h', 'midpoint_lat': 42.300, 'midpoint_lon': 39.047},
    {'path': ['Black Sea', 'Trabzon'], 'time': '24h', 'midpoint_lat': 42.501, 'midpoint_lon': 37.358},
    {'path': ['Kars', 'Ankara'], 'time': '48h', 'midpoint_lat': 40.267, 'midpoint_lon': 37.996},
    {'path': ['Trabzon', 'Istanbul'], 'time': '72h', 'midpoint_lat': 41.505, 'midpoint_lon': 34.348}
]

fig = go.Figure()

# Add propagation lines with timeline labels
for route in propagation_timeline:
    start = next(loc for loc in locations if loc['name'] == route['path'][0])
    end = next(loc for loc in locations if loc['name'] == route['path'][1])
    
    # Contamination pathway
    fig.add_trace(go.Scattergeo(
        lon=[start['lon'], end['lon']],
        lat=[start['lat'], end['lat']],
        mode='lines',
        line=dict(width=2, color='red'),
        hoverinfo='none'
    ))
    
    # Timeline annotation
    fig.add_trace(go.Scattergeo(
        lon=[route['midpoint_lon']],cu
        lat=[route['midpoint_lat']],
        mode='text',
        text=route['time'],
        textfont=dict(color='black', size=10),
        showlegend=False
    ))

# Radiation markers (size scaled to radiation level)
fig.add_trace(go.Scattergeo(
    lon=[loc['lon'] for loc in locations],
    lat=[loc['lat'] for loc in locations],
    mode='markers',
    marker=dict(
        size=[loc['radiation_24h']*50 for loc in locations],  # Scale for visibility
        color=[loc['radiation_24h'] for loc in locations],
        colorscale='Hot',
        cmin=0,
        cmax=2,
        colorbar=dict(
            title='Radiation (mSv) at 24h',
            titleside='right'
        )
    ),
    text=[f"{loc['name']}: {loc['radiation_24h']} mSv" for loc in locations],
    hoverinfo='text'
))

# Map configuration
fig.update_layout(
    title='Radiation Dispersion from Zaporizhzhia to Turkey with Timeline',
    geo=dict(
        scope='europe',
        projection_type='equirectangular',
        showcountries=True,
        countrycolor='Black',
        coastlinecolor='Black',
        landcolor='rgb(217, 217, 217)',
        lataxis_range=[35, 50],
        lonaxis_range=[25, 45]
    ),
    margin=dict(l=0, r=0, t=50, b=0)
)

fig.show()