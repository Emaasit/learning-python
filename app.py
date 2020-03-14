# An App to calculate the sum of two numbers
# Created by Gloria Apolot
# Created on March 14, 2020


# This file is located in this directory
# C:\Users\Apolot\Your team Dropbox\Gloria Apolot\Gloria\Apps>

# First import a package (an add-on) called streamlit
from streamlit import title
from streamlit import subheader
from streamlit import write
from streamlit import slider

# Then use streamlit to create a title of the App
title("Gloria Apolot First App")

# Then use streamlit to add a sub title
subheader("Summing two numbers")

# Then use streamlit to write our task for this App
write("This is my first app. I am going to add two numbers. z = x + y")

# Then, add two numbers and write the answer to a holder named x
# 100 + 120 
speed = slider('Select speed', 0, 100, 80, 10)
time = slider('Select time', 0, 24, 8, 2)
distance = speed * time

# Then use streamlit to create a user interface (UI) that displays the answer
write(speed)
write(time)
write(distance)
