import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('results/clustered_customers.csv')

st.title('Retail Customer Segmentation Dashboard')

clusters = sorted(df['Cluster'].unique())
selected_cluster = st.sidebar.selectbox('Select Cluster to View', clusters)

genders = df['Gender'].unique()
selected_genders = st.sidebar.multiselect('Filter by Gender', genders, default=list(genders))

age_min, age_max = int(df['Age'].min()), int(df['Age'].max())
selected_age = st.sidebar.slider('Select Age Range', age_min, age_max, (age_min, age_max))

income_min, income_max = int(df['Annual Income (k$)'].min()), int(df['Annual Income (k$)'].max())
selected_income = st.sidebar.slider('Select Income Range', income_min, income_max, (income_min, income_max))

spending_min, spending_max = int(df['Spending Score (1-100)'].min()), int(df['Spending Score (1-100)'].max())
selected_spending = st.sidebar.slider('Select Spending Score Range', spending_min, spending_max, (spending_min, spending_max))

filtered_df = df[
    (df['Cluster'] == selected_cluster) &
    (df['Gender'].isin(selected_genders)) &
    (df['Age'] >= selected_age[0]) & (df['Age'] <= selected_age[1]) &
    (df['Annual Income (k$)'] >= selected_income[0]) & (df['Annual Income (k$)'] <= selected_income[1]) &
    (df['Spending Score (1-100)'] >= selected_spending[0]) & (df['Spending Score (1-100)'] <= selected_spending[1])
]

st.subheader(f"Showing {len(filtered_df)} customers for Cluster {selected_cluster}")

st.dataframe(filtered_df)

st.markdown(f"### Summary Statistics for Cluster {selected_cluster}")
st.write(filtered_df.describe())

st.markdown("### Age Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['Age'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

st.markdown("### Spending Score vs Annual Income")
fig2, ax2 = plt.subplots()
sns.scatterplot(data=filtered_df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Gender', ax=ax2)
st.pyplot(fig2)

st.markdown("### Gender Distribution")
gender_counts = filtered_df['Gender'].value_counts()
fig3, ax3 = plt.subplots()
ax3.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
ax3.axis('equal')
st.pyplot(fig3)

csv = filtered_df.to_csv(index=False)
st.download_button(label="Download Filtered Data as CSV", data=csv, file_name='filtered_customers.csv', mime='text/csv')
