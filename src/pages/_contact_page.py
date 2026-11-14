import streamlit as st

def contact_page():
    """
    Render the contact page
    """
    st.title("Contact")
    
    st.write("""
    ### Get in Touch
    
    For questions, feedback, or suggestions about this application,
    [open an issue on GitHub](https://github.com/Jhwong19/optimiser-schedular-app/issues).
    
    ### Repository
    
    This project is open-source. Find the code on GitHub:
    [optimiser-schedular-app](https://github.com/Jhwong19/optimiser-schedular-app)
    
    ### License
    
    This project is licensed under the GNU General Public License v3.0.
    See the LICENSE file for more details.
    """)

# Make sure the function can be executed standalone
if __name__ == "__main__":
    contact_page()
