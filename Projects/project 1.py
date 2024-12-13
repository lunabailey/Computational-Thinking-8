###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("summer")

q1=codesters.Square(100, 100, 200, 'Aquamarine')
q2=codesters.Square(-100, 100, 200, 'Lightskyblue')
q3=codesters.Square(-100, -100, 200, 'orange')
q4=codesters.Square(100, -100, 200, 'Coral')

s1=codesters.Sprite("flower",100,100)
s1.set_size(1.8) 
s2=codesters.Sprite("moonstar1",-100,100)
s2.set_size(0.1)
s3=codesters.Sprite("amongus1",100,-100)
s3.set_size(0.1)
s4=codesters.Sprite("bunny1",-100,-100)
s4.set_size(0.2)
message1=codesters.Text("Luna Bailey",0,220,"white")
message2=codesters.Text("This is my cote of arms",0,-220,"white")
