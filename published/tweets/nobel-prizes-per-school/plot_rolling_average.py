import pandas as pd
import plotly.graph_objects as go

# Read the CSV file
df = pd.read_csv('data.csv')

# Count prizes per school per year
prizes_per_year = df.groupby(['affiliation', 'year']).size().reset_index(name='count')

# Get all unique schools and years
schools = prizes_per_year['affiliation'].unique()
all_years = sorted(prizes_per_year['year'].unique())

# Calculate rolling average for each school
school_rolling_data = []
for school in schools:
    school_data = prizes_per_year[prizes_per_year['affiliation'] == school]

    # Create a complete year range with zeros for missing years
    year_range = pd.DataFrame({'year': all_years})
    school_data = year_range.merge(school_data[['year', 'count']], on='year', how='left').fillna(0)

    # Calculate rolling average (window of 10 years for display, and for ranking)
    school_data['rolling_avg'] = school_data['count'].rolling(window=10, min_periods=1).mean()
    school_data['affiliation'] = school

    school_rolling_data.append(school_data)

# Combine all school data
all_data = pd.concat(school_rolling_data, ignore_index=True)

# For each year, calculate rankings based on rolling average
all_data['rank'] = all_data.groupby('year')['rolling_avg'].rank(method='first', ascending=False)

# For each year, get the top 10 schools by rolling average at the latest year
latest_year = max(all_years)
latest_data = all_data[all_data['year'] == latest_year].nlargest(10, 'rolling_avg')
top_schools = latest_data['affiliation'].unique()

fig = go.Figure()

# Plot complete lines for top 10 schools
for school in top_schools:
    school_data = all_data[all_data['affiliation'] == school]

    fig.add_trace(go.Scatter(
        x=school_data['year'],
        y=school_data['rank'],
        mode='lines+markers',
        name=school,
        hovertemplate='<b>%{fullData.name}</b><br>Avg annual prizes (past 10 yrs): %{customdata:.3f}<extra></extra>',
        customdata=school_data['rolling_avg']
    ))

fig.update_layout(
    title='Nobel Prize Rankings by School Over Time (Top 10)',
    xaxis_title='Year',
    yaxis_title='Ranking',
    yaxis=dict(
        autorange='reversed',  # Rank 1 at top
        tickmode='linear',
        tick0=1,
        dtick=1,
        range=[0.5, 10.5]
    ),
    hovermode='closest',
    height=700,
    legend=dict(yanchor="top", y=0.99, xanchor="left", x=1.01)
)

fig.write_html('nobel_prizes_rolling_average.html')
fig.show()
