# Airbnb Housing Market Analysis in Germany

## Overview
This project is a Streamlit application designed to analyze Airbnb listings in various neighborhoods across Germany. Using this tool, users can explore different aspects of the Airbnb market, such as price distribution, room type popularity, availability, and more. The app provides a user-friendly interface to visualize and understand trends in the Airbnb market, making it valuable for both hosts and potential guests.

## Features
- **Neighborhood Group Filter**: Select a neighborhood group (e.g., a city or district) to focus your analysis on a specific area.
- **Price Distribution**: Visualize how Airbnb prices are distributed within the selected neighborhood group.
- **Room Type Distribution**: See the frequency of different room types (Entire home/apt, Private room, etc.) in the selected area.
- **Price vs. Number of Reviews**: Explore the relationship between listing prices and the number of reviews.
- **Availability vs. Price**: Analyze how the availability of listings correlates with their price.
- **Average Price by Neighbourhood**: Compare average prices across different neighborhoods within the selected group.

## Getting Started

### Prerequisites
- Python 3.x
- The following Python packages:
  - `streamlit`
  - `pandas`
  - `seaborn`
  - `matplotlib`

You can install these packages using pip:

```bash
pip install streamlit pandas seaborn matplotlib
```

## Dataset
The application uses an Airbnb dataset with the following structure:

- id: Listing ID
- name: Name of the listing
- host_id: Host ID
- host_name: Host name
- neighbourhood_group: Larger area or district (e.g., city)
- neighbourhood: Specific neighborhood
- latitude, longitude: Geographical coordinates
- room_type: Type of room (Entire home/apt, Private room, etc.)
- price: Price per night
- minimum_nights: Minimum nights stay required
- number_of_reviews: Total reviews
- last_review: Date of the last review
- reviews_per_month: Average reviews per month
- calculated_host_listings_count: Number of listings the host has
- availability_365: Number of available days in a year

## How to Use
- Select a Neighborhood Group: Start by choosing a neighborhood group to filter the data.
- Explore Data: Use the visualizations to explore price distributions, room types, and other key metrics.
- Gain Insights: Understand market trends, price ranges, and the impact of factors like room type and availability.

## License
This project is open-source and available under the MIT License.