# STEP 1: Import the necessary modules.
import streamlit as st
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

st.title("Mudra Smart Glasses App")


# STEP 2: Create an GestureRecognizer.
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

# STEP 3: Take photo 
st.info("Strike a pose of one of the following hand gestures with your hands, and we'll put our cutting-edge hand gesture recognition technology to the test!: 👍🏽,☝🏽,🖐🏽,✌🏽,👊🏽,👎🏽,🤟🏽")
picture=st.camera_input("") # Don't put anything into the quotes.


if picture:
    #st.image(picture)

    with open('gesture.jpg', 'wb') as f:
        f.write(picture.read())

    # STEP 4: Load the input picture.
    image = mp.Image.create_from_file('gesture.jpg')

    # STEP 5: Recognize gestures in the input picture.
    recognition_result = recognizer.recognize(image)

   #STEP 6: Show the resulting picture
    print(recognition_result)
    
    if recognition_result.gestures[0][0].category_name=="Pointing_Up": 
        st.header("Suchi")
        st.subheader("This mudra represents direction, the world, the number one or a needle")

    elif recognition_result.gestures[0][0].category_name=="Thumb_Up" :
        st.header("Shikara")
        st.subheader("This mudra represents heroism, a king, a bow or a mountain peak")

    if recognition_result.gestures[0][0].category_name=="Open_Palm" :
        st.header("Stop")
        st.subheader("This guesture is commenly used in ballet, representing the stop or pause motion")

    elif recognition_result.gestures[0][0].category_name=="Closed_Fist" :
        st.header("The letter A")
        st.subheader("This guesture represents the letter A in American Sign Language")

    if recognition_result.gestures[0][0].category_name=="Victory" :
        st.header("Peace")
        st.subheader("This guesture is commenly used in ballet, representing symmetry or mirroring movements between dancers.")

    elif recognition_result.gestures[0][0].category_name=="ILoveYou" :
        st.header("I Love You")
        st.subheader("This term is commenly used in American Sign Language to communicate the feeling of love.")
    
    else:
        st.write(recognition_result.gestures[0][0].category_name)


    
