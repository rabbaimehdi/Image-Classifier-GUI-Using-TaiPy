#Imports
from taipy.gui import Gui

#Variables
img_path = 'placeholder_image.png'
#Define the app as a Gui
index = """
<|text-center|
<|{"logo.png"}|image|>

<|{content}|file_selector|extensions=.png|>
 Select an image to classify
 
<|{img_path}|image|>

<|label|indicator|value=0|min=0|max=100|width=22vw|>
>
"""

def on_change(state, var, val):
    if var == "content":
        state.img_path = val
    #print(state,var,val)
app = Gui(page = index)

#Run script
if __name__ =="__main__":
    app.run(use_reloader=True)
