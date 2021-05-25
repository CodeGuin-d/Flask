from flask import Flask, redirect, url_for, render_template, request
import random
import time
app = Flask(__name__)

boxes= [1,2,3,4]
random.shuffle(boxes)
#HOMEPAGE
@app.route("/")
@app.route("/home")
@app.route("/home/<name>")
def home(name="Home Page!"):
    return render_template("home.html", content=name) 

@app.route("/bubble", methods=['GET','POST'])
def bsort():
    if request.method == 'POST':
        request.method="GET"
        if request.form.get('sort') == 'Bubble Sort':
            bubble()
        elif request.form.get('random') == 'Randomize List':
            randomize()
    return render_template("bsort.html", boxes=numToStr(boxes), len=len(boxes))

@app.route("/quick", methods=['GET','POST'])
def qsort():
    if request.method == 'POST':
        request.method="GET"
        if request.form.get('sort') == 'Quick Sort':
            quick(0, len(boxes)-1, boxes)
        elif request.form.get('random') == 'Randomize List':
            randomize()
    return render_template("qsort.html", boxes=numToStr(boxes), len=len(boxes))


@app.route("/bogo", methods=['GET','POST'])
def bogosort():
    if request.method == 'POST':
        request.method="GET"
        if request.form.get('sort') == 'Bogosort':
            bogosort()
        elif request.form.get('random') == 'Randomize List':
            randomize()
    return render_template("bogosort.html", boxes=numToStr(boxes), len=len(boxes))


def bubble():
    for _ in range(len(boxes)):
        for i in range(len(boxes)-1):
            if boxes[i]>boxes[i+1]:
                boxes[i], boxes[i+1] = boxes[i+1], boxes[i]
                bsort()
 #Python3 implementation of QuickSort 
 
# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively
def partition(start, end, array):
     
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]
     
    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:
         
        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1
             
        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1
         
        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if(start < end):
            array[start], array[end] = array[end], array[start]
     
    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    
    # Returning end pointer to divide the array into 2
    return end
     
# The main function that implements QuickSort
def quick(start, end, array):
    if (start < end):
         
        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)
         
        # Sort elements before partition
        # and after partition
        quick(start, p - 1, array)
        quick(p + 1, end, array)
     
# This code is contributed by Adnan Aliakbar

def bogosort():
    while boxes!=[1,2,3,4]:
        randomize()
        time.sleep(0.5)
    return render_template("bogosort.html", boxes=numToStr(boxes), len=len(boxes))
def randomize():
    random.shuffle(boxes)

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
