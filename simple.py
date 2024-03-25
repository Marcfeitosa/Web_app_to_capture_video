import cv2
import streamlit as st
import datetime

st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get the current date and time
        current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cv2.putText(frame, f"Date and Time: {current_date_time}", (50, 50),
                    cv2.FONT_HERSHEY_PLAIN, 2, (20, 100, 200), 2, cv2.LINE_AA)

        streamlit_image.image(frame)
