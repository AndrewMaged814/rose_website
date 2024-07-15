
import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="ROSE - Robot Features", layout="wide")

# Title and Introduction
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🚀 ROSE: The Future of Educational Robots 🚀</h1>",
            unsafe_allow_html=True)

# Contact Information
st.markdown("""
<h3 style='text-align: center; color: #4B4BFF;'>Contact Us:</h3>
<p style='text-align: center;'>
<strong>Andrew Maged:</strong> andrewmaged814@gmail.com<br>
<strong>Adham Haytham:</strong> adhamhithamaz@gmail.com<br>
<strong>Mina Samy:</strong> m.s.milad@student.aast.edu<br>
<strong>Malak Khaled:</strong> khaledmalak001@student.aast.edu<br>
<strong>Mohamed Abdalla:</strong> m.a.abdelrahman6@student.aast.edu<br>
<strong>Yostina Aziz:</strong> yostina.a.aziz@student.aast.edu<br>
</p>
""", unsafe_allow_html=True)

st.markdown("""
*Welcome to the official page of ROSE!*
Dive into the world of advanced AI and discover how ROSE can revolutionize education with its cutting-edge features and interactive capabilities. Scroll down to explore what makes ROSE the ultimate educational companion.
""")

# Section: Functional Capabilities
st.markdown("<h2 style='color: #FF4B4B;'>🌟 Functional Capabilities 🌟</h2>",
            unsafe_allow_html=True)

# PDF Chatting
st.markdown("<h3 style='color: #4BFF4B;'>📄 PDF Chatting</h3>",
            unsafe_allow_html=True)
st.write("""
ROSE lets you interact with PDF documents effortlessly. Simply upload your documents and ask ROSE any questions to retrieve relevant information instantly. 
""")
st.image("PDF-LangChain_white.jpg",
         caption="PDF Chatting Feature", use_column_width=True)

# Quiz Generation
st.markdown("<h3 style='color: #4B4BFF;'>📝 Quiz Generation</h3>",
            unsafe_allow_html=True)
st.write("""
Transform study materials into quizzes automatically with ROSE. Generate questions and test your knowledge with ease.
""")
st.image("rose_soft_arch_quiz2.png",
         caption="Quiz Generation Feature", use_column_width=True)

# Emotion-Based Music Playing
st.markdown("<h3 style='color: #FF4BFF;'>🎵 Emotion-Based Music Playing</h3>",
            unsafe_allow_html=True)
st.write("""
ROSE can sense your mood and play music to match. Whether you need to relax or get energized, ROSE has the perfect playlist ready for you.
""")
st.image("rose_soft_arch_emotion.png",
         caption="Emotion-Based Music Feature", use_column_width=True)

# Conversational AI
st.markdown("<h3 style='color: #FFD700;'>🗣 Conversational AI</h3>",
            unsafe_allow_html=True)
st.write("""
Engage in meaningful, intelligent conversations with ROSE. Our advanced AI understands your queries and provides insightful responses, making learning interactive and fun.
""")

# Study Plan Maker
st.markdown("<h3 style='color: #FF4500;'>📅 Study Plan Maker</h3>",
            unsafe_allow_html=True)
st.write("""
ROSE helps you create personalized study plans tailored to your learning pace and goals. Stay organized and on track with ROSE's study plan suggestions.
""")

# Image and Face Recognition
st.markdown("<h3 style='color: #32CD32;'>📸 Image and Face Recognition</h3>",
            unsafe_allow_html=True)
st.write("""
With advanced image and face recognition capabilities, ROSE can identify objects and people, enhancing interactive learning experiences.
""")
st.image("face.png",
         caption="Image and Face Recognition Feature", use_column_width=True)

# GPT-4 Turbo with Vision
st.markdown("<h3 style='color: #FF69B4;'>🔍 GPT-4 Turbo with Vision</h3>",
            unsafe_allow_html=True)
st.write("""
Combining advanced language processing with powerful visual recognition, GPT-4 Turbo with Vision interprets and analyzes both text and images, providing comprehensive insights and solutions across various applications.
""")
st.image("GPT with vision.png",
         caption="GPT4-Turbo with vision Feature", use_column_width=True)


# Exam Evaluation using GPT-4 Turbo with Vision
st.markdown("<h3 style='color: #B22222;'>📝 Exam Evaluation</h3>",
            unsafe_allow_html=True)
st.write("""
Designed to revolutionize educational support, this tool analyzes exam images, extracts and understands text, separates questions from answers, and provides accurate evaluations and scores.
""")
st.image("eval.png",
         caption="Exam Evaluation Feature", use_column_width=True)

# Question Extraction and Answering from PDF
st.markdown("<h3 style='color: #8A2BE2;'>❓ Question Extraction from PDF</h3>",
            unsafe_allow_html=True)
st.write("""
This tool allows ROSE to analyze the content of a given PDF, extract questions, and provide accurate answers based on the context, simplifying information retrieval and understanding.
""")
st.image("qa_with_PDF.png",
         caption="Question Extraction and Answering from PDF Feature", use_column_width=True)
# Video to Text
st.markdown("<h3 style='color: #FF7F50;'>🎥 Video to Text</h3>",
            unsafe_allow_html=True)
st.write("""
Transcribe video content in real-time. Engage in dynamic chats and discussions directly within the transcribed content, fostering a more interactive and inclusive communication experience.
""")
st.image("vidpng.png",
         caption="Video to Text Feature", use_column_width=True)
# Braille to English
st.markdown("<h3 style='color: #20B2AA;'>♿ Braille to English</h3>",
            unsafe_allow_html=True)
st.write("""
Convert Braille text into English, providing a seamless and inclusive experience for visually impaired individuals, promoting equal access to information.
""")
st.image("Braille.png",
         caption="Braille Feautre", use_column_width=True)
# Links Section
st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>🔗 Learn More About ROSE 🔗</h2>",
            unsafe_allow_html=True)
st.markdown("""
For more information, visit our [GitHub repository](https://github.com/AndrewMaged814/R.O.S.E/tree/rose-final) or watch our [YouTube video](https://youtu.be/pKGvKF1Qh6w).
""")

# Footer
st.markdown("<p style='text-align: center; color: #AAAAAA;'>© 2024 ROSE Project. All rights reserved.</p>",
            unsafe_allow_html=True)
