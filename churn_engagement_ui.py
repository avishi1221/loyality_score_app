import streamlit as st
from datetime import datetime, timedelta

# Function to determine user engagement and generate notifications
def generate_notification(user_id, last_visit, time_spent, pages_viewed, interaction_score):
    try:
        # Convert last_visit to datetime if it's a string
        if isinstance(last_visit, str):
            last_visit = datetime.strptime(last_visit, "%Y-%m-%d")

        days_since_last_visit = (datetime.today() - last_visit).days

        # Determine user status
        if interaction_score < 0.5 and days_since_last_visit > 3:
            notification_type = "Email" if pages_viewed > 3 else "SMS"
            message = f"Hey {user_id}, we miss you! Get exclusive offers and new content just for you!"
        else:
            notification_type = "None"
            message = "User is engaged, no notification needed."

        return notification_type, message
    
    except Exception as e:
        return "Error", str(e)

# Streamlit UI
st.title("Churn Risk-Based Customer Engagement System")

user_id = st.text_input("User ID")
last_visit = st.date_input("Last Visit Date", datetime.today() - timedelta(days=5))
time_spent = st.number_input("Time Spent (minutes)", min_value=0.0, step=0.1)
pages_viewed = st.number_input("Pages Viewed", min_value=0, step=1)
interaction_score = st.slider("Interaction Score (0-1)", 0.0, 1.0, 0.5)

if st.button("Generate Notification"):
    notification_type, message = generate_notification(user_id, last_visit, time_spent, pages_viewed, interaction_score)
    
    st.write(f"**User ID:** {user_id}")
    st.write(f"**Notification Type:** {notification_type}")
    st.write(f"**Message:** {message}")
