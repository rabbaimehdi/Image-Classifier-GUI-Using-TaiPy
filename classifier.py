#Imports
from taipy.gui import Gui

#Define the app as a Gui
index_html = """<h1> Hello World</h1>"""
index_md = """# Hello World"""
app = Gui(page = index_md)

#Run script
if __name__ =="__main__":
    app.run(use_reloader=True)
