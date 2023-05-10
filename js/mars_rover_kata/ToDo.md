- [ ] A function `sendSettings` that takes and input and set the grid, the position for each rover and the list of instructions
- [ ] A recursive function `moveRover` that takes the grid size, the current position coordinates`X, Y`, the current
      direction, and a list of movements, returns the last position and direction.
- [X] A function `getNewdirection` that takes the current direction, `L` or `R` and returns the direction for the next step
- [X] A function `setNewPosition` that takes the grid size, the current position and the direction for the next step and
      returns the coordinates of the new position or throws and error if reach the edges.
  - [X] A function `calculateNewPositionCoordinates` that takes the current position and the direction for the next step.
- [X] A function `validateEdges` that takes the grid size, the coordinates of the current position, and the coordinates
      of the new position, returns `true` if the movement can be done and `false` in another way
 
# Work flow
 The `sendSetting` functions, set the "environment" and communicate the appropiated settings for each rover. Call the
 `moveRover` function. The `moveRover` function set the new direction calling the `setNextDirection` function and call
 the `setNextPosition` function that call the `validateEdged`, if the return of the last one is `true` makes the next
 step and do the recursive called if the list of moves has more 
 
# Considerations
- I need to consider some edge cases like that the grid has only one dimention (row or column)
 
