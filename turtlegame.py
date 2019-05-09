import turtle 
import random 
wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.title("Turtle Race")
lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')
andyTotalDistance=0
lanceTotalDistance=0
andy.up()
lance.up()
andy.goto(andyTotalDistance, 20)
lance.goto(lanceTotalDistance, -20)
start = turtle.Turtle()  
start.hideturtle()
for i in range(150)
    andyDistance = random.randrange(1, 5)
    lanceDistance = random.randrange(1, 5)
    andy.forward(andyDistance)
    lance.forward(lanceDistance)
    andyTotalDistance = andyTotalDistance + andyDistance
    lanceTotalDistance = lanceTotalDistance + lanceDistance
for eachInt in range(145):
    if andyTotalDistance > lanceTotalDistance:

        start.write("Andy is the winner!", move=False, align="center", font=("Arial", 25, "normal"))

    elif lanceTotalDistance > andyTotalDistance:
        start.write("Lance is the winner!", move=False, align="center", font=("Arial", 25, "normal"))

    else: print("Tie Game")

wn.exitonclick()

