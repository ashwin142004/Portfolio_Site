import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

# --- Page Config ---
st.set_page_config(
    page_title="Ashwin Mysore | Portfolio",
    page_icon="�‍💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Load Assets ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

# --- Sidebar ---
with st.sidebar:
    st.image("assets/profile.jpg", width=150) # Profile Pic
    st.markdown("## Ashwin Narendra Mysore")
    st.markdown("Information Science & Engineering Student")
    st.markdown("📍 Bengaluru, India")
    
    selected = option_menu(
        menu_title=None,
        options=["Home", "Skills", "Projects", "Experience", "Achievements", "Contact"],
        icons=["house", "code-slash", "briefcase", "clock-history", "trophy", "envelope"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#00adb5", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#333"},
            "nav-link-selected": {"background-color": "#00adb5"},
        }
    )
    
    st.markdown("---")
    st.markdown("""
    <div style="display: flex; justify-content: center; gap: 20px;">
        <a href="https://www.linkedin.com/in/ashwin-mysore-6564b425a" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/linkedin.png" width="30"/>
        </a>
        <a href="https://github.com/ashwin142004" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/github.png" width="30"/>
        </a>
        <a href="https://www.instagram.com/__user2004__/" target="_blank">
            <img src="https://img.icons8.com/fluent/48/000000/instagram-new.png" width="30"/>
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- Home Section ---
if selected == "Home":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.title("Hi, I'm Ashwin 👋")
        st.subheader("Aspiring Software Engineer & AI Enthusiast")
        st.write("""
        I am an Information Science and Engineering student at BNM Institute of Technology, passionate about **Automation, Artificial Intelligence, and Full-Stack Development**.
        
        I love building tools that solve real-world problems, from **Genetic Algorithms** for scheduling to **Voice-Controlled Smart Homes**.
        
        **🚀 Highlights:**
        - 9.34 GPA
        - Vice Chair, BNMIT-ACM Student Chapter
        - Multiple Hackathon Winner
        """)
        with open("assets/resume.pdf", "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name="Ashwin_Resume.pdf",
            mime="application/pdf",
        )
    with col2:
        lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
        st_lottie(lottie_coding, height=300, key="coding")

# --- Skills Section ---
elif selected == "Skills":
    st.title("Technical Arsenal 🛠️")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Proficiency Radar")
        # Radar Chart
        categories = ['Python', 'Java', 'Web Dev', 'Automation (UiPath)', 'IoT', 'AI/ML']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=[5, 3, 3, 4, 4, 4],
            theta=categories,
            fill='toself',
            name='Ashwin',
            line_color='#00adb5'
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5]
                )),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color="white")
        )
        st.plotly_chart(fig, width="stretch")
        
    with col2:
        st.subheader("Skills Breakdown")
        st.write("### 💻 Languages")
        st.write("Python, Java, C, HTML, CSS, JavaScript, SQL")
        
        st.write("### 🔧 Frameworks & Tools")
        st.write("UiPath Studio, Streamlit, PyQt, React.js, Node.js")
        
        st.write("### ☁️ Cloud & Certifications")
        st.write("AWS Academy Graduate, Google AI Essentials, UiPath Automation Suite")

# --- Projects Section ---
elif selected == "Projects":
    st.title("My Projects �")
    
    # Helper function for project cards
    def project_card(title, tech, desc):
        st.markdown(f"""
        <div class="css-card">
            <h3>{title}</h3>
            <p style="font-size: 14px; color: #ccc;">{tech}</p>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        project_card(
            "Timetable Generator", 
            "Python, PyQt, Genetic Algorithm", 
            "Automated class schedule creation avoiding conflicts using genetic algorithms."
        )
        st.write("")
        project_card(
            "Voice-Controlled Smart Home", 
            "Raspberry Pi, Python, Google Speech API", 
            "Home automation system controlling appliances via voice commands."
        )
        st.write("")
        project_card(
            "Number Plate Detection", 
            "Raspberry Pi, Python, OCR (Tesseract)", 
            "Security system to scan and verify vehicle number plates for authorized access."
        )
        st.write("")
        project_card(
            "Automatic Pet Feeding System", 
            "Arduino, C, Servo Motor", 
            "Timed pet food dispenser using RTC module and servo motors."
        )
        st.write("")
        project_card(
            "Multi-Agent Chatbot", 
            "Python, Gemini API, Gradio", 
            "Modular chatbot with dedicated agents for trivia, math, and jokes."
        )

    with col2:
        project_card(
            "File Automation System", 
            "UiPath Studio", 
            "RPA bot to automate file renaming, moving, and organizing."
        )
        st.write("")
        project_card(
            "ToDo App", 
            "Python, Streamlit", 
            "GUI-based task management app for daily planning."
        )
        st.write("")
        project_card(
            "Email Thread Extractor", 
            "Python, Gemini API", 
            "Tool to parse email threads and summarize conversations using LLM."
        )
        st.write("")
        project_card(
            "Natural Language to SQL", 
            "Python, Gemini API", 
            "Converts plain English queries into SQL commands for non-tech users."
        )
        st.write("")
        project_card(
            "Project Portfolio Website", 
            "Python, Streamlit", 
            "The website you are looking at right now! Interactive and responsive."
        )

# --- Experience Section ---
elif selected == "Experience":
    st.title("Experience & Education 🎓")
    
    st.subheader("Work Experience")
    st.markdown("""
    <div class="timeline-item">
        <h3>Summer Internship | BNMIT</h3>
        <span style="color: #00adb5;">Web Technologies & File Structures</span>
        <p><em>Built a responsive website and a C++ file-structured backend for cricket player data.</em></p>
    </div>
    
    <div class="timeline-item">
        <h3>Cybersecurity Internship | Theta Dynamics</h3>
        <span style="color: #00adb5;">Security Analyst Intern</span>
        <p><em>Learned white hat hacking, phishing prevention, and fraud detection. Hands-on with Kali Linux.</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Education")
    st.markdown("""
    <div class="timeline-item">
        <h3>B.E. Information Science & Engineering</h3>
        <span style="color: #00adb5;">BNM Institute of Technology | 2022 - 2026</span>
        <p><strong>GPA:</strong> 9.34</p>
    </div>
    """, unsafe_allow_html=True)

# --- Achievements Section ---
elif selected == "Achievements":
    st.title("Achievements & Certifications 🏆")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Hackathons & Awards")
        st.markdown("""
        - 🥇 **1st Prize** – Anveshan Prodathon, 2022
        - 🥈 **2nd Prize** – Prodathon, 2022
        - 🥈 **2nd Place** – Hardware Hackathon, IEEE-PES BMSCE, 2024
        - 🏏 **1st Place** – Inter-Department Cricket Tournament, BNMIT
        """)
        
        st.subheader("Leadership Roles")
        st.markdown("""
        - **Vice Chair** – BNMIT-ACM Student Chapter
        - **Event Coordinator** – Nexus Community BNMIT
        - **Student Coordinator** – RPA Club BNMIT
        """)

    with col2:
        st.subheader("Certifications")
        st.markdown("""
        - **Google AI Essentials** (Coursera)
        - **AWS Academy Graduate** – Cloud Web Application Builder
        - **Python for Data Science** (Infosys Springboard)
        - **DevOps & Cloud Fundamentals** (PWC Launchpad)
        - **Cybersecurity** (Theta Dynamics)
        - **UiPath Automation Suite** (UiPath Academy)
        - **CompTIA Network+ Prep**
        """)

# --- Contact Section ---
elif selected == "Contact":
    st.title("Get In Touch 📬")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("I'm always open to discussing new projects, creative ideas, or opportunities to be part of your visions.")
        st.markdown("""
        **📧 Email:** nmashwin145@gmail.com  
        **📞 Phone:** +91 7619221555
        **🏠 Address:**Bengaluru, India
        """)
        
        st.markdown("---")
        st.write("### Send a Message")
        contact_form = """
        <form action="https://formsubmit.co/nmashwin145@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="Name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
            <input type="email" name="Email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc;">
            <textarea name="Message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #ccc; min-height: 100px;"></textarea>
            <button type="submit" style="background-color: #00adb5; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer;">Send Message</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)
    
    with col2:
        st_lottie(load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_u25cckyh.json"), height=300)
