#Imports
from taipy.gui import Gui

#Variables
img_path = 'placeholder_image.png'
#Define the app as a Gui
index = """
<|text-center|
<|{"logo.png"}|image|>

<|{img_path}|file_selector|extensions=.png|>
 Select an image to classify
 
<|{img_path}|image|>
>
"""
app = Gui(page = index)

#Run script
if __name__ =="__main__":
    app.run(use_reloader=True)
