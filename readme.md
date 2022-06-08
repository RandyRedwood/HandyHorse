# HandyHorse read me
---
## Problem
Calculate the number of possible numbers a knight can dial on a cellphone numberpad in N moves
from the start position S.

## My Solution
To calculate the ammount of possible numbers we are interested in the number of different paths the knight can travel in N steps.
The only thing we need to remember about a particular path,from step to step, is the end position of the knight since that dictates how many new path he will find and the end positions of these new paths.

Each position will produce two more positions on the next step, except for the four and six positions which will produce three.

We can reduce the number of positions by bundling existing positions together.

1,3,7,9 are all the corner positions which create one side position which can reach zero and one side position which can't reach zero on the next step.

2,8 are side positions which can't reach zero and will generate two corner positions on the next step.

4,6 are side positions which can reach zero and generate two corner and one 0-position on the next step.

0 is the 0-position which generates two side positions which can reach zero.

Five is a special case since it can't reach any of the other positions and is mostly irrelevant for the problem.

After simplifying down to four relevant types of positions we get the following equations for the amount of new positions at the next step calculated from the old amount of endpositions

new_corners = sides_can_zero * 2 + sides * 2

new_sides = corners

new_sides_can_zero = corners + zero_positions * 2

new_zero_positions = sides_can_zero

The startposition S sets the amount of positions for one type of position to one.

Afterwards we use these equations to calculate the new ammounts for the different type of endpositions after each step.

We do this N-times.

After we reached the number of required steps we sum up the ammounts of endpositions to get the total ammount of endpositions which is equal to the number of possible paths in N steps.