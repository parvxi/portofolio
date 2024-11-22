import streamlit as st
# Color palette
# Updated color palette with lighter colors
colors = {
    'lightest_blue': '#CAE9FF',  # A very light blue
    'light_blue': '#BEE9E8',  # Soft blue
    'medium_blue': '#62B6CB',  # Medium blue
    'dark_blue': '#5FA8D3',  # Brighter blue
    'darkest_blue': '#1B4965',  # Vibrant blue
    'white': '#FFFFFF',  # White
}

# Updated background gradient for a lighter theme
st.markdown(f"""
<style>
    .stApp {{
background: rgb(27,73,101);
background: linear-gradient(90deg, rgba(27,73,101,1) 51%, rgba(98,182,203,1) 100%, rgba(190,233,232,1) 100%); !important;

    }}
</style>
""", unsafe_allow_html=True)


# HTML and CSS for the centered baby blue interactive timeline with polaroid-style photos
timeline_html = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Covered+By+Your+Grace&family=Homemade+Apple&display=swap');
:root {{
    --lightest-blue: {colors['lightest_blue']};
    --light-blue: {colors['light_blue']};
    --medium-blue: {colors['medium_blue']};
    --dark-blue: {colors['dark_blue']};
    --darkest-blue: {colors['darkest_blue']};
    --white: {colors['white']};
}}
.timeline-container {{
    display: flex;
    justify-content: center;
    width: 100%;
    padding: 10px;
}}
.timeline {{
    position: relative;
    max-width: 1200px;
    width: 100%;
}}
.timeline::after {{
    content: '';
    position: absolute;
    width: 6px;
    background-color: var(--dark-blue);
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -3px;
}}
.timeline-item {{
    padding: 10px 40px;
    position: relative;
    background-color: inherit;
    width: 50%;
    box-sizing: border-box;
}}
.timeline-item::after {{
    content: '';
    position: absolute;
    width: 25px;
    height: 25px;
    right: -17px;
    background-color: var(--darkest-blue);
    border: 4px solid var(--darkest-blue);
    top: 15px;
    border-radius: 50%;
    z-index: 1;
}}
.left {{
    left: 0;
}}
.right {{
    left: 50%;
}}
.right::after {{
    left: -16px;
}}
.timeline-content {{
    padding: 20px 30px;
    position: relative;
}}
.timeline-year {{
    font-weight: bold;
    font-family: 'Montserrat', sans-serif;
    font-size: 1.8em;
    color: var(--dark-blue);
    margin-bottom: 10px;
    transition: all 0.3s ease;
}}
.timeline-text {{
    color: var(--medium-blue);
    margin-bottom: 10px;
    font-family: 'Montserrat', sans-serif;
}}
.timeline-photo {{
    background-color: var(--white);
    border: 1px solid var(--light-blue);
    padding: 2px 3px 10px 3px;
    transform: rotate(-2deg);
    width: 200px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 15px;
    transition: all 0.3s ease;
}}
.timeline-photo img, .timeline-photo iframe {{
    width: 100%;
    height: 150px;
    object-fit: cover;
    display: block;
}}
.timeline-photo p {{
    text-align: center;
    margin-top: 10px;
    font-size: 1.3em;
    font-family: "Covered By Your Grace", cursive;
    color: var(--darkest-blue);
}}
.timeline-item:hover .timeline-year {{
    font-size: 1.5em;
    color: var(--darkest-blue);
}}

.timeline-item:hover .timeline-photo {{
    transform: rotate(0deg) scale(1.05);
    box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}}
.timeline-text-list {{
    list-style-type: none;
    padding-left: 0;
    margin-bottom: 15px;
}}

.timeline-text-list li {{
    position: relative;
    padding-left: 20px;
    margin-bottom: 5px;
    font-size: 0.9em;
    color: var(--white);
    font-family: 'Montserrat', sans-serif;
}}

.timeline-text-list li a:hover,
.timeline-text-list li a:active {{
    color: var(--lightest-blue);
    border-bottom-color: var(--lightest-blue);
}}


.timeline-text-list li a {{
    color: var(--light-blue);
    text-decoration: none;
    transition: all 0.3s ease;
    border-bottom: 1px solid transparent;
}}

.timeline-text-list li a:hover,
.timeline-text-list li a:active {{
    color: var(--lightest-blue);
    border-bottom-color: var(--lightest-blue);
}}

@media (hover: hover) {{
    .timeline-text-list li a:hover {{
        color: var(--lightest-blue);
        border-bottom-color: var(--lightest-blue);
    }}
     .timeline-text-list li:hover {{
        transform: scale(1.03);
    }}

}}


.timeline-text-list li::before {{
    content: '•';
    position: absolute;
    left: 0;
    color: var(--dark-blue);
}}


@media screen and (max-width: 600px) {{
    .timeline::after {{
        left: 31px;
    }}
    .timeline-item {{
        width: 100%;
        padding-left: 70px;
        padding-right: 25px;
    }}
    .left::after, .right::after {{
        left: 15px;
    }}
    .right {{
        left: 0%;
    }}
}}
</style>

<div class="timeline-container">
    <div class="timeline">
        <div class="timeline-item right">
            <div class="timeline-content">
                <div class="timeline-year"> Nov 2024</div>
                <div class="timeline-text">Le Wagon Data Science Bootcamp (Saudi Digital Academy)</div>
                <ul class="timeline-text-list">
                    <li>Completed a 480+ hour intensive program in data science, focusing on machine learning, data processing, and analytics.</li>
                    <li>Worked on projects involving predictive modeling, data cleaning, and feature engineering.</li>
                    <li>Developed a capstone project addressing real-world business challenges using advanced techniques.</li>
                    <li>Collaborated on innovative solutions, blending technical proficiency with creativity to meet industry standards.</li>
                </ul>
                <div class="timeline-photo">
                    <iframe src="https://drive.google.com/file/d/17Ci9eFTih2IpYyuoNXtw18UpEZFha0rN/preview" width="640" height="480" allow="autoplay"></iframe>
                    <p>Le Wagon Bootcamp Journey!</p>
                </div>
            </div>
        </div>
    </div>
</div>















<div class="timeline-container">
    <div class="timeline">
        <div class="timeline-item left">
            <div class="timeline-content">
                <div class="timeline-year">Oct 2024</div>
                <div class="timeline-text">SUKOON Team Interview - Al-Madina Newspaper</div>
                <ul class="timeline-text-list">
                    <li>Featured in Al-Madina newspaper, interviewed by Nafisa Maghfouri from Jazan.</li>
                    <li>Highlighted the journey and vision behind SUKOON, an EEG-based stress detection project.</li>
                    <li>Reflected on the experience of promoting mental health awareness through innovation.</li>
                </ul>
                <div class="timeline-photo">
                    <iframe src="https://drive.google.com/file/d/1fV1aoLpHjDaDfvUoDfzSfKdARGSWrG--/preview" width="640" height="480" allow="autoplay"></iframe>
                    <p>SUKOON Team Interview!</p>
                </div>
            </div>
        </div>
    </div>
</div>















        <div class="timeline-container">
    <div class="timeline">
        <div class="timeline-item right">
            <div class="timeline-content">
                <div class="timeline-year"> Sep 2024</div>
                <div class="timeline-text">TechHub Event</div>
                <ul class="timeline-text-list">
                    <li>Participated in a 3-day TechHub event at King Abdulaziz University, showcasing **SUKOON**, a stress-detection project using EEG-based technology.</li>
                    <li>Presented our poster to various audiences, including industry experts, professors, and students, receiving valuable feedback.</li>
                    <li>Built connections with professionals and innovators, paving the way for future collaborations.</li>
                </ul>
                <div class="timeline-photo">
                    <iframe src="https://drive.google.com/file/d/10H88kPmG41PIkzJAezsz1w3Jy7lwRSE5/preview" width="640" height="480" allow="autoplay"></iframe>
                        <p>Tech-hub Event!</p>
                </div>
            </div>
        </div>
    </div>
</div>



<div class="timeline-item left">
    <div class="timeline-content">
        <div class="timeline-year">May 2024</div>
        <div class="timeline-text">2nd Place, KAU Scientific Forum</div>
        <ul class="timeline-text-list">
            <li>Awarded 2nd place at the KAU Scientific Forum for an EEG-based emotion detection project.</li>
            <li>Focused on using cutting-edge technology to analyze brain wave data for emotional analysis and detection.</li>
            <li>Contributed to Saudi Vision 2030 by advancing knowledge-based innovation and showcasing the potential of human capital through research and development.</li>
        </ul>
        <div class="timeline-photo">
            <iframe src="https://drive.google.com/file/d/1GEF2sXCEx5sfDG2XldkKbBpOdC8bYB_K/preview" width="400" height="150" allow="autoplay"></iframe>
            <p>2nd Place Award!</p>
        </div>
    </div>
</div>


<div class="timeline-item right">
    <div class="timeline-content">
        <div class="timeline-year">Aug 2023</div>
        <div class="timeline-text">Center of Excellence in Intelligent Engineering Systems (CEIES)</div>
        <ul class="timeline-text-list">
            <li><strong>AI Specialist Trainee</strong></li>
            <li>Designed and developed an application utilizing real-time brain wave data processing algorithms for stress detection.</li>
            <li>Created a user-friendly interface for visualization and interaction to enhance user engagement.</li>
        </ul>
        <div class="timeline-photo">
            <iframe src="https://drive.google.com/file/d/1JXbCG-KxHmCuXzf2ST-pcRiLTugU039D/preview" width="400" height="150" allow="autoplay"></iframe>
            <p>CEIES Ending Ceremony!</p>
        </div>
    </div>
</div>

<div class="timeline-container">
    <div class="timeline">
        <div class="timeline-item left">
            <div class="timeline-content">
                <div class="timeline-year">May 2023</div>
                <div class="timeline-text">IEEEXtreme Coding Competition - Top 10 Teams at KAU</div>
                <ul class="timeline-text-list">
                    <li>Participated in the IEEEXtreme Coding Competition, a global 24-hour programming challenge organized by IEEE.</li>
                    <li>Achieved recognition as one of the Top 10 Teams at King Abdulaziz University (KAU), showcasing strong problem-solving abilities and technical expertise.</li>
                    <li>Solved a variety of complex problems, including algorithm design, data structures, and optimization tasks, under strict time constraints.</li>
                    <li>Demonstrated effective teamwork and innovative thinking, making a significant mark in a competitive university setting.</li>
                </ul>
                <div class="timeline-photo">
                    <iframe src="https://drive.google.com/file/d/1bO9pphAeWE1R-1OB2cVmmRxtnRTKIk-S/preview" width="640" height="480" allow="autoplay"></iframe>
                    <p>IEEEXtreme Achievement!</p>
                </div>
            </div>
        </div>
    </div>
</div>

 <div class="timeline-item right">
    <div class="timeline-content">
        <div class="timeline-year">Jan 2023</div>
        <div class="timeline-text">Microsoft Student Club Member</div>
        <ul class="timeline-text-list">
            <li>UI/UX Developer at Microsoft Student Club.</li>
            <li>Enhanced UI/UX skills through workshops, hackathons, and industry events.</li>
            <li>Collaborated with club members to organize and promote events that encouraged student participation and learning. <a href="https://drive.google.com/file/d/1owrQBSIjvoKrhdvjUybk0IMbpOJRKN7F/preview"></a></li>
        </ul>
        <div class="timeline-photo">
            <iframe src="https://drive.google.com/file/d/1AdkakSYvSLaHRJiYppPhX0g0NeNaDgTG/preview" width="640" height="480" allow="autoplay"></iframe>
            <p>MLSAC Family!</p>
        </div>
    </div>
</div>
    </div>
</div>

"""

























st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    .title {
        font-family: 'Montserrat', sans-serif;
        color: {colors['lightest_blue']}; /* Change title color */
        font-size: 2.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add custom CSS for styling (if not already present)
st.markdown(f"""
<style>
    .hover-effect {{
        transition: color 0.3s ease, transform 0.3s ease; /* Smooth hover effect */
        color: {colors['lightest_blue']}; /* Default color */
        text-align: center; /* Keep text always centered */
    }}
    .hover-effect:hover {{
        color: {colors['dark_blue']}; /* Color on hover */
        transform: translateY(-5px); /* Slight move up effect */
    }}
</style>
""", unsafe_allow_html=True)


# Create the timeline with hover effect on the title
st.markdown("<h1 class='title hover-effect'>Career Highlights</h1><h2 class='subtitle'></h2>", unsafe_allow_html=True)

def show():
    # Renderizar a timeline
    st.components.v1.html(timeline_html, height=1000, scrolling=True)

# Chamar a função show
show()
