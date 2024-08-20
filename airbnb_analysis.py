import airbnb_analysis as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv("airbnb_data.csv")
    return data


# Display the header
st.title("Airbnb Housing Market Analysis in Germany")
st.write(
    """
This app provides an analysis of Airbnb listings in various neighborhoods in Germany.
"""
)

# Load and display data
data = load_data()

# Filter by neighborhood group
neighbourhood_groups = data["neighbourhood_group"].unique()
selected_neighbourhood_group = st.selectbox(
    "Select a Neighbourhood Group", neighbourhood_groups
)

filtered_data = data[data["neighbourhood_group"] == selected_neighbourhood_group]

# Display neighborhood data
st.write(f"## {selected_neighbourhood_group} Listings Data")
st.write(filtered_data)

# Price Distribution
st.write("### Price Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_data["price"], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Room Type Distribution
st.write("### Room Type Distribution")
room_type_counts = filtered_data["room_type"].value_counts()
fig, ax = plt.subplots()
sns.barplot(x=room_type_counts.index, y=room_type_counts.values, ax=ax)
st.pyplot(fig)

# Price vs. Number of Reviews
st.write("### Price vs. Number of Reviews")
fig, ax = plt.subplots()
sns.scatterplot(
    data=filtered_data, x="number_of_reviews", y="price", hue="room_type", ax=ax
)
st.pyplot(fig)

# Availability vs. Price
st.write("### Availability vs. Price")
fig, ax = plt.subplots()
sns.scatterplot(
    data=filtered_data, x="availability_365", y="price", hue="room_type", ax=ax
)
st.pyplot(fig)

# Average Price by Neighbourhood
st.write("### Average Price by Neighbourhood")
avg_price_by_neighbourhood = (
    filtered_data.groupby("neighbourhood")["price"].mean().reset_index()
)
fig, ax = plt.subplots()
sns.barplot(data=avg_price_by_neighbourhood, x="price", y="neighbourhood", ax=ax)
st.pyplot(fig)
