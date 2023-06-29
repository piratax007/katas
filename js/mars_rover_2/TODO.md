1 rover behavior:
 -[ ]one instruction:
    -[x] turning left
    -[ ] turning right
    -[ ] move foward

-[ ] 
rover object:
 { x,y, orientation}


stuff:

switch (instruction) {
case "L": return turnToLeft(rover.direction)
case "R": return turnToRight(rover.direction)
}
