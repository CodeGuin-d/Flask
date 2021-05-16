from flask import Flask, redirect, url_for, render_template, request
import random
app = Flask(__name__)

boxes= [1,2,3,4]
random.shuffle(boxes)
#HOMEPAGE
@app.route("/")
@app.route("/home")
@app.route("/home/<name>")
def home(name="Home Page!"):
    return render_template("home.html", content=name) 

@app.route("/box", methods=['GET','POST'])
def box():
    if request.method == 'POST':
        request.method=""
        if request.form.get('sort') == 'Bubble Sort':
            bubble()
        elif request.form.get('random') == 'Randomize List':
            randomize()
    return render_template("box.html", boxes=numToStr(boxes), len=len(boxes))  
def bubble():
    for _ in range(len(boxes)):
        for i in range(len(boxes)-1):
            if boxes[i]>boxes[i+1]:
                boxes[i], boxes[i+1] = boxes[i+1], boxes[i]
                box()

def randomize():
    random.shuffle(boxes)
    box()

def numToStr(arr):
    str=[]
    for i in range(len(arr)):
        if arr[i] ==1:
            str.append("ONE")
        elif arr[i] ==2:
            str.append("TWO")
        elif arr[i]==3:
            str.append("THREE")
        elif arr[i]==4:
            str.append("FOUR")
    return str
if __name__ == "__main__":
    app.run(debug=True)