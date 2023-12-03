#Imports
from taipy.gui import Gui
from tensorflow.keras import models
from PIL import Image
import numpy as np

#Variables
classes = {
    0: 'airplane',
    1: 'automobile',
    2: 'bird',
    3: 'cat',
    4: 'deer',
    5: 'dog',
    6: 'frog',
    7: 'horse',
    8: 'ship',
    9: 'truck'
}

content=""
img_path = 'placeholder_image.png'
model = models.load_model("baseline_model.keras")
#Define model prediction function

def predict_image(model, path):
    img = Image.open(path)
    img = img.convert("RGB") 
    img = img.resize((32, 32))
    data = np.asarray(img)
    data = data / 255
    data = np.array([data])
    probs = model.predict(data)
    print(np.max(probs))
    print(np.argmax(probs))
    print(classes.get(np.argmax(probs)))
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
        predict_image(model, val)
    #print(state,var,val)
app = Gui(page = index)

#Run script
if __name__ =="__main__":
    app.run(use_reloader=True)
