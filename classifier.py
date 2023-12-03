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


model = models.load_model("baseline_model.keras")

content=""
img_path = 'placeholder_image.png'
prob = 0
pred = ""
#Define model prediction function

def predict_image(model, path):
    img = Image.open(path)
    img = img.convert("RGB") 
    img = img.resize((32, 32))
    data = np.asarray(img)
    data = data / 255
    data = np.array([data])
    probs = model.predict(data)

    top_prob = probs.max()
    top_pred = classes.get(np.argmax(probs))
    return top_prob, top_pred
    
#Define the app as a Gui
index = """
<|text-center|
<|{"logo.png"}|image|>

<|{content}|file_selector|extensions=.png|>
 Select an image to classify
 
<|{pred}|>

<|{img_path}|image|>

<|{prob}|indicator|value={prob}|min=0|max=100|width=22vw|>
>
"""

def on_change(state, var, val):
    if var == "content":
        top_prob, top_pred = predict_image(model, val)
        
        state.img_path = val
        state.prob = round(top_prob * 100)
        state.pred = f"This is a {top_pred}"
    #print(state,var,val)
app = Gui(page = index)

#Run script
if __name__ =="__main__":
    app.run(use_reloader=True)
