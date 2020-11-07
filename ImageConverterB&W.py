# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO CONVERT & SAVE IMAGES INTO BLACK & WHITE IMAGE USING THE PIL LIBRARY

# Images can be converted into Black And White Images with the help of PIL Library.
# Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python
# Imaging Library by Fredrik Lundh and Contributors
#
# Python Imaging Library adds image processing capabilities to Python interpreter.
# This library provides extensive file format support, an efficient internal
# representation, and fairly powerful image processing capabilities.
# The core image  library is designed for fast access to data stored in a few basic
# pixel formats.
# It should provide a solid foundation for a general image processing tool.
#
# The module can be installed using the command - pip install Pillow

# Importing necessary packages
import os
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    label = Label(text="IMAGE : ", bg="darkslategray4")
    label.grid(row=0, column=1, padx=5, pady=5)
    root.entry = Entry(width=30, textvariable=imagePath)
    root.entry.grid(row=0, column=2, padx=5, pady=5)
    button = Button(width=10, text="UPLOAD", command=imageBrowse)
    button.grid(row=0, column=3, padx=5, pady=5)

    label = Label(text="INPUT IMAGE : ", bg="darkslategray4")
    label.grid(row=1, column=1, padx=5, pady=5)
    root.inputImageLabel = Label(root)
    root.inputImageLabel.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

    # Opening a random image using open() of Image class to be displayed when program starts
    # The following 5 Lines Of Code are optional
    inputRandomImage = Image.open('YOUR RANDOM IMAGE PATH')
    # Resizing the image using Image.resize()
    imageResize = inputRandomImage.resize((400, 400), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the image
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.inputImageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.inputImageLabel.image = imageDisplay

    button = Button(width=10, text="CONVERT", command=imageConvert)
    button.grid(row=3, column=2, padx=5, pady=5)

    label = Label(text="CONVERTED IMAGE", bg="darkslategray4",  font=('',20))
    label.grid(row=0, column=4, padx=5, pady=5, columnspan=3)
    root.outputImageLabel = Label(root)
    root.outputImageLabel.grid(row=2, column=4, columnspan=3, padx=5, pady=5)

    # Opening a random image using open() of Image class to be displayed when program starts
    # The following 5 Lines Of Code are optional
    outputRandomImage = Image.open('YOUR RANDOM IMAGE PATH')
    # Resizing the image using Image.resize()
    imageResize = outputRandomImage.resize((400, 400), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the image
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the image
    root.outputImageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.outputImageLabel.image = imageDisplay

# Defining imageBrowse() to select and display the input image to convert to Black & White
def imageBrowse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in destinationDirectory
    # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
    i_Image = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH")
    # Displaying the directory in the directory textbox
    imagePath.set(i_Image)
    # Opening the image using open() of Image class which takes the input image as argument
    imageView = Image.open(i_Image)
    # Resizing the image using Image.resize()
    imageResize = imageView.resize((400,400), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.inputImageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.inputImageLabel.image = imageDisplay

# Defining imageDecode() to deocde the user selected image to decode
def imageConvert():
    # Fetching user-input image path from the tkinter variable and storing it in codeImage
    i_Image = imagePath.get()
    # Opening the image using open() of Image class which takes the input image as argument
    imageObj = Image.open(i_Image)

    # Converting the image to black & white using convert() with mode 'L'
    # Mode L converts the image to black and white
    convertedImage = imageObj.convert('L')

    # Fetching the name of the input image from the user-input image path
    input_image_name = os.path.splitext(os.path.basename(i_Image))[0]
    # Contatenating keyword B&W with image name and storing the new name
    converted_image_name = input_image_name + "-B&W.jpg"
    # Fetching the path of the user-input image
    input_image_path = os.path.dirname(os.path.abspath(i_Image))
    # Concatenating the input_image_path with converted_image_name
    final_converted_image_name = input_image_path + "/" + converted_image_name
    # Saving converted image in the same path using the save() of the Image Library Object
    convertedImage.save(final_converted_image_name)

    # Opening the converted image using the open() of Image class
    imageView = Image.open(final_converted_image_name)
    # Resizing the image using Image.resize()
    imageResize = imageView.resize((400,400), Image.ANTIALIAS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.outputImageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.outputImageLabel.image = imageDisplay

# Creating object root of tk
root = tk.Tk()

# Setting the title, window size, disabling the resizing property and setting the
# background color
root.title("PythonImageConverter")
root.geometry("980x570")
root.resizable(False, False)
root.config(background = "darkslategray4")

# Creating tkinter variable
imagePath = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop to run application
root.mainloop()
