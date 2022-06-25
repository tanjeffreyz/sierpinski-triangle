<div align="center">
  <h1>Sierpinski Triangle</h1>
</div>
A fun little script that draws a Sierpinski triangle.


## Methods
To generate a Sierpinski triangle, pick a random point `x` within the outermost triangle.
During each iteration, randomly pick one of the three vertices, call it `v`, and find `m = midpoint(x, v)`.
Plot `m` and update `x <- m` for the next loop.


## Results
### Starting outside the center sub-triangle
Choosing a starting point outside the center inner triangle produces a clean triangle with no blemishes:
![](triangle_start_outside_inner.png)

### Starting inside the center sub-triangle
Choosing a starting point inside the center inner triangle blemishes one sub-triangle of each size:
![](triangle_start_inside_inner.png)
