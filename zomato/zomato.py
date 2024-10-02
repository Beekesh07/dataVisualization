import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
link = 'https://raw.githubusercontent.com/TheiScale/YouTube-Video-Notes/refs/heads/main/Zomato_Python_Project/Zomato%20data%20.csv'
df = pd.read_csv(link, on_bad_lines='skip')
df = df.reset_index(drop=True)

# Data cleaning
df.rename(columns={'listed_in(type)': 'Type', 'approx_cost(for two people)': 'cost', 'rate': 'rating'}, inplace=True)
df['rating'] = df['rating'].apply(lambda x: x.split('/')[0])
df['rating'] = df['rating'].astype('float')


# Streamlit app title
st.title("Zomato Restaurant Data Analysis")

# Sidebar options for exploring the dataset
st.sidebar.title("Navigation")
options = st.sidebar.radio("Choose a section", ["Restaurant Type", "Votes by Restaurant Type", "Restaurant Ratings", "Couples' Online Orders", "Max Rating by Mode"])

# Q1: Majority of customers order from which type of restaurant?
if options == "Restaurant Type":
    st.subheader("Restaurant Type Distribution")
    colors = ['#2F4F4F', '#8B0000', '#4B0082', '#00008B']
    plt.figure(figsize=(10, 5))
    sns.countplot(x='Type', data=df, palette=colors)
    plt.title('Restaurant Type Distribution')
    st.pyplot(plt)

# Q2: Votes received by each type of restaurant
if options == "Votes by Restaurant Type":
    st.subheader("Votes Received by Restaurant Type")
    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FFD700']
    grouped_res = df.groupby('Type')['votes'].sum().plot(kind='bar', color=colors)
    plt.title('Votes for Restaurant Types')
    plt.xlabel('Restaurant Type', color='Red', size=15)
    plt.ylabel('Votes', color='Red', size=15)
    st.pyplot(plt)

# Q3: Restaurant ratings distribution
if options == "Restaurant Ratings":
    st.subheader("Histogram of Restaurant Ratings")
    plt.figure(figsize=(10, 5))
    plt.hist(df['rating'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Restaurant Ratings')
    plt.xlabel('Rating', color='red', size=15)
    plt.ylabel('Frequency', color='red', size=15)
    st.pyplot(plt)

# Q4: Average spending by couples on online orders
if options == "Couples' Online Orders":
    st.subheader("Couples' Average Spending on Online Orders")
    st.bar_chart(df['cost'].value_counts())

# Q5: Maximum rating by online/offline order
if options == "Max Rating by Mode":
    st.subheader("Online vs Offline Ratings")
    plt.figure(figsize=(4, 4))
    plt.bar(x=df['online_order'], height=df['rating'])
    plt.xlabel('Order Mode')
    plt.ylabel('Rating')
    plt.xticks(ticks=[0, 1], labels=['Online', 'Offline'])
    st.pyplot(plt)

# Run the app
if __name__ == "__main__":
    st.write("Enjoy exploring the restaurant data!")
