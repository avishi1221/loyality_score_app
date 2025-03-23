import streamlit as st
from datetime import datetime

# Streamlit UI setup
st.title("Customer Loyalty Score & Reward System")
st.write("Enter customer details to calculate their loyalty score and get reward recommendations.")

# Input fields
user_id = st.text_input("User ID", "")
purchases = st.number_input("Number of Purchases", min_value=0, value=5)
last_activity = st.date_input("Last Activity Date")
feedback_score = st.slider("Feedback Score (1-5)", 1.0, 5.0, 4.0)
engagement_score = st.slider("Engagement Score (0-1)", 0.0, 1.0, 0.5)

# Function to calculate loyalty score
def calculate_loyalty(purchases, last_activity, feedback, engagement):
    days_inactive = (datetime.today() - last_activity).days

    # Simple formula for loyalty score
    score = (purchases * 10) + (feedback * 15) + (engagement * 40) - (days_inactive * 2)
    score = max(0, min(100, score))  # Keep score between 0-100

    # Categorization
    if score > 70:
        category = "Loyal"
        reward = "Exclusive VIP access + 20% discount"
    elif score >= 40:
        category = "At-Risk"
        reward = "Limited-time 10% discount"
    else:
        category = "Churned"
        reward = "Come back offer: 30% off"

    return score, category, reward

# Button to calculate score
if st.button("Calculate Loyalty Score"):
    if user_id:
        score, category, reward = calculate_loyalty(purchases, last_activity, feedback_score, engagement_score)
        st.success(f"Loyalty Score: {score}")
        st.write(f"Category: **{category}**")
        st.write(f"Recommended Reward: **{reward}**")
    else:
        st.error("Please enter a valid User ID.")
