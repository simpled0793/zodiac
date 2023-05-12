"""
devon drew Software Development Track
Sagittarius Constellation
"""

import turtle 
import time

turtle.Turtle()
window = turtle.Screen()
window.setup (width=1.0, height=1.0, startx=0, starty=0)
turtle.pensize(1)
turtle.shape("turtle")
turtle.hideturtle()

def firstPage():
  turtle.hideturtle()
  window.bgcolor('#3D3D3D')
  turtle.color('white')
  turtle.penup()
  turtle.goto(0,100)
  turtle.pendown()
  turtle.write("Midterm Project", font=("Arial",20,'normal'),align='center')
  turtle.right(90)
  turtle.penup()
  turtle.fd(50)
  turtle.pendown()
  turtle.write("The Cancer Constellation", font=("Arial",20,'normal'),align='center')
  turtle.penup()
  turtle.fd(50)
  turtle.pendown()
  turtle.write("Devon Drew", font=("Arial",20,'normal'),align='center')
firstPage()
time.sleep(20)
turtle.clear()

def secondPage():
    turtle.bgpic('cancer.gif')
    turtle.color('white')
secondPage()
time.sleep(20)
window.clear()

def thirdPage():
    turtle.bgcolor('black')
    turtle.color('white')
    turtle.dot(15)
    turtle.write('Iota Cacri', font=("arial",18,'italic'))
    # observe the directions according to our requirment
    turtle.right(85)
    turtle.forward(80)
    turtle.dot(10)
    turtle.write('Asellus Borealis', font=("arial",18,'italic'))
    #turn turtle to its right
    turtle.right(18)
    turtle.forward(40)
    turtle.write('Asellus Australis', font=("arial",18,'italic'))
    # here every length or angle is jst assumed
    # jst cchange the angles and lengths according to our required output
    turtle.dot(15)
    turtle.left(50)
    turtle.forward(80)
    turtle.dot(15)
    turtle.write('Altarf', font=("arial",18,'italic'))
    #now penup go back to the previous dot and then pen down
    turtle.right(180)
    turtle.penup()
    turtle.forward(80)
    turtle.pendown()
    #now observe the direction of the turtle
    turtle.left(108)
    turtle.forward(50)
    turtle.dot(10)
    turtle.write('acubens', font=("arial",18,'italic'))
    turtle.penup()
    turtle.forward(-450)
    turtle.pendown()
    turtle.color('purple')
    turtle.write('The Cancer Constellation', font=("Arial",20,'italic'))

thirdPage()
time.sleep(30)
window.clear()

def fourthpage():
    turtle.bgpic('night.gif')
    turtle.color('white')
    time.sleep(10)
    turtle.dot(15)
    turtle.write('Iota Cacri', font=("arial",18,'italic'))
    # observe the directions according to our requirment
    turtle.right(85)
    turtle.forward(80)
    turtle.dot(10)
    turtle.color('yellow')
    turtle.write('Asellus Borealis', font=("arial",18,'italic'))
    #turn turtle to its right
    turtle.right(18)
    turtle.forward(40)
    turtle.write('Asellus Australis', font=("arial",18,'italic'))
    # here every length or angle is jst assumed
    # jst cchange the angles and lengths according to our required output
    turtle.dot(15)
    turtle.left(50)
    turtle.forward(80)
    turtle.dot(15)
    turtle.color('yellow')
    turtle.write('Altarf', font=("arial",18,'italic'))
    #now penup go back to the previous dot and then pen down
    turtle.right(180)
    turtle.penup()
    turtle.forward(80)
    turtle.pendown()
    #now observe the direction of the turtle
    turtle.left(108)
    turtle.forward(50)
    turtle.dot(10)
    turtle.write('acubens', font=("arial",18,'italic'))
    turtle.penup()
    turtle.forward(-450)
    turtle.pendown()
    turtle.color('Red')
    turtle.write('Cancer: The Crab', font=("Arial",20,'bold'))

fourthpage()
time.sleep(30)
window.clear()
