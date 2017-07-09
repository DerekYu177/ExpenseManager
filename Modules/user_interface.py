#!/usr/bin/python2.7

# for file prompt
import Tkinter as tk
from tkFileDialog import askdirectory

# for displaying images
from PIL import ImageTk, Image

def prompt_user_for_location():
    # exists outside of class
    tk_prompt = tk.Tk()

    tk_prompt.withdraw()
    return askdirectory()

class UserInterface:

    def __init__(self, image_path):
        self.image_path = image_path

        # single declaration
        root = tk.Tk()

        self.default_iphone_photo_size = "750x1335"

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        self.root = root

    def display_image(self):
        window = self.root
        window.title("Title")
        window.configure(background="grey")

        path = self.image_path

        image = Image.open(path)
        tk_image = ImageTk.PhotoImage(self.__resize(image))

        panel = tk.Label(window, image = tk_image)

        panel.pack(side = "bottom", fill = "both", expand = "yes")

        window.mainloop()

    def __resize(self, image):
        image_width, image_height = image.size

        desired_height = self.screen_height/2

        adjustment_ratio = desired_height/float(image_height)
        desired_width = int((float(image_width)*adjustment_ratio))

        image = image.resize((desired_width, desired_height), Image.ANTIALIAS)

        return image
