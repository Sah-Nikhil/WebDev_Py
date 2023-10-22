import streamlit as st
import os
import base64
import requests
from PIL import Image
from streamlit_lottie import st_lottie

#website title bar
st.set_page_config(page_title="WLSN", page_icon=":video_camera:", layout="wide")

#setup to add hyperlinks to images/gifs
@st.cache_data()
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data()
def get_img_with_href(local_img_path, target_url):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
    <a href="{target_url}">
        <img src="data:image/{img_format};base64,{bin_str}" />
    </a>'''
    return html_code


#setting variable for lottie animation
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#loading css(local)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#function call
local_css("style/style.css")

#loading assets
lottie_1 = load_lottie_url("https://lottie.host/ef86396b-cbaf-4e76-b2d1-c32accf87011/DpkPeY2ZgY.json")
gif_html = get_img_with_href('gifgit.gif', 'https://www.linkedin.com/in/Sah-Nikhil/')

contact_form = """
<form action="https://formsubmit.co/nikku.k70@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" palceholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <textarea name="message" placeholder="Message" required></textarea>
    <button type="submit">Send</button>
</form>
"""


#website body
with st.container():
    st.subheader("Hello, I'm WLSN!")
    st.header("A Videographer from India")
    st.write("I am passionate about creating unique and engaging visuals. I am currently based in New Delhi, India.")
    st.write("[Check out my work](https://instagram.com/kliqs.nikhil)")

with st.container():
    st.write("------")
    left_column, right_column = st.columns((2,1))
    
    with left_column:
        st.subheader("What I do")
        st.write("##")
        st.write(
            """
            I am Agastya S. Wilson,
            - A passionate video production specialist, with a keen eye for detail and a knack for creating engaging visuals.
            - The CFO and cheif Video Production Specialist of Kshatriya Media, a media production house where we specialize in producing long form podcasts.
            - A final year student at the University of Delhi, pursuing a degree in Economics Honors.
            """
            )
        with st.container():
            st.markdown(gif_html, unsafe_allow_html=True) 
            
    with right_column:
        with st.container():
            st_lottie(lottie_1, height=400)
    st.write("------")
    
    
    with st.container():
        lft_col, rt_col = st.columns(2) 
        with rt_col:
            st.subheader("My Skills")
            #st.write("##")
            left_col, right_col = st.columns(2)
            with left_col:
                st.write("""            
                    - Video Production
                    - Video Editing
                    - Video Post-Production
                    - Video Color Grading
                    - Video Compression
                    - Video Rendering
                    """)
            with right_col:
                st.write("""
                    - Video Uploading
                    - Video Optimization
                    - Audio Production
                    - Audio Editing
                    - Audio Rendering
                    - Audio Optimization""")
        with lft_col:
            st.image('adobe_suite.jpg', width=500)
    st.write("------")
    with st.container():
        st.header("Let's Collaborate!")
        lc, rc = st.columns(2)
        with lc:
            st.write("I am always looking for new and exciting projects to work on. If you have an idea, let's collaborate!")
            st.write("##")
            st.markdown(contact_form, unsafe_allow_html=True)
        with rc:
            st.empty()