import os
import webbrowser

def main():
    print("Hi! my name is Aayushker a Web Developer from India. Here's my resume:")
    resume_path = os.path.join(os.path.dirname(__file__), "resume.pdf")
    print(f"Resume saved at: {resume_path}")
    print("Opening my portfolio website in your browser...")
    webbrowser.open("https://aayushker.netlify.app")
