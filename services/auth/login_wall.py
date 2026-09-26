import streamlit as st

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
 
    st.title("🏋️‍♂️AI Real-Time GYM Trainer")
    st.markdown("### Welcome! Please enter a username to start.")  #for h3 heading

    return False