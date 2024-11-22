import streamlit as st
import base64

st.set_page_config(
    page_title="Shahad Baalkhashir",
    page_icon="⭐",
    layout="centered",
    initial_sidebar_state="auto"
)

# Custom CSS to change background color and add hover effects
background_color = """
<style>
    .stApp {
        background: linear-gradient(135deg, #BEE9E8 0%, #CAE9FF 100%);
    }
    .sidebar-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
        color: #1B4965;
    }
    .sidebar-button {
        padding: 10px;
        cursor: pointer; /* Default cursor */
        background-color: #62B6CB; /* Mid-tone blue background */
        border-radius: 5px; /* Rounded corners */
        font-size: 18px; /* Larger font size */
        font-weight: bold; /* Bold text */
        color: #1B4965; /* Deep blue text color */
        transition: background-color 0.3s ease, transform 0.3s ease; /* Smooth transition */
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }
    .sidebar-button:hover {
        background-color: #5FA8D3; /* Slightly darker blue on hover */
        transform: translateY(-2px); /* Move up slightly on hover */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); /* Stronger shadow on hover */
    }
    .sidebar-container {
        margin: 10px 0;
    }
</style>
"""
st.markdown(background_color, unsafe_allow_html=True)

# --- PAGE SETUP --- #

# Sidebar for navigation
st.sidebar.markdown("<div class='sidebar-title'>Navigation</div>", unsafe_allow_html=True)

# Initialize a session state variable to track the current page
if 'current_page' not in st.session_state:
    st.session_state.current_page = "About Me"  # Default page

# Create buttons for navigation
with st.sidebar.container():
    if st.sidebar.button("About Me", key="about_button"):
        st.session_state.current_page = "About Me"

    if st.sidebar.button("Highlights", key="highlights_button"):
        st.session_state.current_page = "Highlights"

    if st.sidebar.button("Resume", key="resume_button"):
        st.session_state.current_page = "Resume"

# Load the appropriate page based on the selected item
if st.session_state.current_page == "About Me":
    with open("views/about.py") as f:
        exec(f.read())
elif st.session_state.current_page == "Highlights":
    with open("views/extracurriculars.py") as f:
        exec(f.read())
elif st.session_state.current_page == "Resume":
    st.subheader("My Resume")
    resume_path = "pdf_files/ShahadHatim_Resume_Template.pdf"

    # Check if file exists
    try:
        with open(resume_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()

        # Download Button
        st.download_button(
            label="Download Resume",
            data=pdf_bytes,
            file_name="ShahadHatim_Resume_Template.pdf",
            mime="application/pdf"
        )

        # Inline PDF Viewer
        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
        pdf_display = f"""
        <iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" style="border: none;"></iframe>
        """
        st.markdown(pdf_display, unsafe_allow_html=True)

    except FileNotFoundError:
        st.error("The specified PDF file was not found. Please check the file path.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
