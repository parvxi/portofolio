import streamlit as st
from streamlit.components.v1 import html

# Permissions Policy Meta Tag
st.markdown("""
    <meta http-equiv="Permissions-Policy" content="ambient-light-sensor=(), battery=(), document-domain=(), layout-animations=(), legacy-image-formats=(), oversized-images=(), vr=(), wake-lock=()">
""", unsafe_allow_html=True)

# Define colors
colors = {
    'background': '#F4F6F9',      # Soft, light gray background
    'primary_text': '#1A2B3C',    # Deep navy blue for main text
    'secondary_text': '#4A5568',  # Soft gray for secondary text
    'accent': '#3182CE',          # Vibrant blue for highlights
    'card_background': '#FFFFFF', # Clean white for cards
    'hover_color': '#2C5282',     # Darker blue for hover states
}

# Advanced Typography and Layout CSS
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        .stApp {{
            background-color: {colors['background']};
            font-family: 'Inter', sans-serif;
        }}

        /* Modern Card Design */
        .stCard {{
            background-color: {colors['card_background']};
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            transition: transform 0.3s ease;
        }}

        .stCard:hover {{
            transform: translateY(-5px);
        }}

        /* Typography Styles */
        h1, h2, h3 {{
            color: {colors['primary_text']};
            font-weight: 700;
        }}

        p {{
            color: {colors['secondary_text']};
            line-height: 1.6;
        }}

        /* Modern Button Styling */
        .stButton > button {{
            background-color: {colors['accent']};
            color: white;
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-weight: 600;
            transition: all 0.3s ease;
        }}

        .stButton > button:hover {{
            background-color: {colors['hover_color']};
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
        }}

        /* Social Links */
        .social-links a {{
            color: {colors['accent']};
            text-decoration: none;
            margin-right: 15px;
            font-weight: 500;
            transition: color 0.3s ease;
        }}

        .social-links a:hover {{
            color: {colors['hover_color']};
        }}
    </style>
""", unsafe_allow_html=True)

# Header Section
html_typing_effect = """
<div style='text-align: center; margin-top: 50px; margin-bottom: 40px;'>
    <h1 style='font-size: 3rem; margin-bottom: 15px;'>Hello, I am Shahad Baalkhashir</h1>
    <h3 style='font-size: 1.8rem; color: #4A5568;'>
        <span id="dynamic-typing"></span>
    </h3>
</div>
<script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
<script>
    new Typed('#dynamic-typing', {
        strings: ["a Data Scientist", "a Creative Thinker", "a Tech Enthusiast", "a Logical Problem Solver"],
        typeSpeed: 80,
        backSpeed: 40,
        loop: true
    });
</script>
"""
html(html_typing_effect, height=200)

# Divider
st.divider()

class AboutMe:
    def __init__(self, title, about, img, width=None):
        self.title = title
        self.about = about
        self.img = img
        self.width = width

    def display(self):
        col1, col2 = st.columns([10, 9])

        with col1:
            st.markdown(f"<h2 style='color: {colors['primary_text']};'>{self.title}</h2>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: {colors['secondary_text']};'>{self.about}</p>", unsafe_allow_html=True)
            st.markdown("""
                <div class="social-links">
                    <a href="https://www.linkedin.com/in/shahad-k-baalkhashir-822629209/" target="_blank">🔗 LinkedIn</a>
                    <a href="mailto:shahadhatemba@gmail.com" target="_blank">📨 Email</a>
                    <a href="https://github.com/parvxi" target="_blank">💻 Github</a>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.image(self.img, use_container_width=True)

# Description Section
description = """
I'm a passionate tech enthusiast and a Computer Science graduate with a talent for merging creativity and innovation. My expertise lies in data science and developing smart, user-friendly applications that address real-world challenges.

What excites me most is transforming complex ideas into practical, impactful solutions that make a difference. I thrive on continuous learning, meaningful collaboration, and pushing the boundaries of what technology can achieve.

Let's connect and bring visionary ideas to life—together, we can create something extraordinary!
"""

about = AboutMe(
    title="About Me",
    about=description,
    img="img/profile.png",
    width=700
)
about.display()

# Divider
st.divider()

# Technical Skills Section
# Technical Skills Section with Balanced Cards
st.markdown("<h2 style='text-align: center; color: #1A2B3C;'>Technical Skills</h2>", unsafe_allow_html=True)

skills = [
    {"category": "👩🏻‍💻 Programming Languages", "items": ["Python", "Java"]},
    {"category": "📖 Libraries & Frameworks", "items": ["Pandas", "PyTorch", "TensorFlow", "Streamlit"]},
    {"category": "☁️ Cloud & Deployment", "items": ["Docker"]},
    {"category": "👾 Version Control", "items": ["Git"]},
    {"category": "✒️ Formatting Tools", "items": ["LaTeX"]},
]

# CSS Styling for cards with scrollable content
st.markdown(f"""
    <style>
        .skill-card {{
            background-color: {colors['card_background']};
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 15px;
            margin: 10px;
            text-align: center;
            height: auto;
            min-height: 200px; /* Set a minimum height for balance */
            max-height: 300px; /* Limit maximum height */
            display: flex;
            flex-direction: column;
            justify-content: flex-start; /* Align content at the top */
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}

        .skill-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
        }}

        .skill-title {{
            font-size: 1.2rem;
            font-weight: bold;
            color: {colors['primary_text']};
            margin-bottom: 10px;
        }}

        .skill-item-container {{
            overflow-y: auto; /* Scrollable area for long lists */
            max-height: 150px; /* Limit height of scrollable area */
        }}

        .skill-item {{
            font-size: 1rem;
            color: {colors['secondary_text']};
            margin: 5px 0;
        }}

        /* Add scrollbar styles for a modern look */
        .skill-item-container::-webkit-scrollbar {{
            width: 6px;
        }}
        .skill-item-container::-webkit-scrollbar-thumb {{
            background-color: {colors['hover_color']};
            border-radius: 4px;
        }}
        .skill-item-container::-webkit-scrollbar-track {{
            background-color: {colors['background']};
        }}
    </style>
""", unsafe_allow_html=True)

# Display skills as cards with scrollable content
cols = st.columns(3)
for idx, skill in enumerate(skills):
    with cols[idx % 3]:  # Rotate through columns
        st.markdown(f"""
            <div class="skill-card">
                <div class="skill-title">{skill['category']}</div>
                <div class="skill-item-container">
                    {"".join(f"<div class='skill-item'>{item}</div>" for item in skill['items'])}
                </div>
            </div>
        """, unsafe_allow_html=True)




# Call-to-Action Button
st.markdown(
    "<div style='text-align: center; margin-top: 40px;'>"
    "<a href='mailto:shahadhatemba@gmail.com' style='text-decoration: none;'>"
    "<button style='background-color: #3182CE; color: white; border: none; padding: 12px 24px; border-radius: 8px;'>Get in Touch</button>"
    "</a>"
    "</div>",
    unsafe_allow_html=True
)

# Divider
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.divider()
st.markdown("")
# Footer Section
st.markdown(
    f"""
    <div class="footer">
        <p>Developed by Shahad Hatim K. &copy; 2024</p>
    </div>
    """,
    unsafe_allow_html=True
)
