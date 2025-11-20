import turtle

def hit_check(actor1: turtle.Turtle, actor2: turtle.Turtle, threshold):
    distance = actor1.distance(actor2)
    return distance < threshold