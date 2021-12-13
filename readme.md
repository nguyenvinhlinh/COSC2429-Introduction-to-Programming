# COSC2429 – Introduction to Programming
## Assignment 1 – 2021C

Please submit a zip folder including 4 python files, 1 for each of these questions. They must
be named p1.py, p2.py, p3.py, and p4.py accordingly. No capital letter in the file names. There
will be automatic unit test, so if you don’t follow the naming and data type instruction
carefully, your programs might fail all the test cases.

Point deduction will be given if you:

- Have incorrect file names, function names, variable names
- Forget file header in the correct format
- Forget function docstrings in the correct format
- Have no or little code comment
- Writing too long and repetitive code where iteration can help shorten it

Note:

- Please don’t have any user input function
- Pay attention to data type of the outputs


## Problem 1:
Given a list of 20 integers, write a function to find the number in the list where exactly 80%
of numbers in the list are equal to or smaller than it (not including itself).

Your function takes the list of 20 integers as input and outputs the desired number.

IMPORTANT: Your function must be named and must have the function parameters listed in the same
order as below. (I will use a python script with a database to automatically test your function
so please don’t do it differently.)

```python
def find_split_80(integer_list):
# your logic here
# return the desired number
return split_80
```

Solution:
```python
def find_split_80(integer_list):
    integer_list.sort()
    split_80 = integer_list[16]
    return split_80
```


## Problem 2:
The constant π is defined as the ratio between a circle’s circumference to its diameter.
Given the circle in the image below, we know that it has a radius of 1, and its area equals to π.
Therefore, a method to estimate π is to estimate the area of this circle. This is done by
generating random points within the square bordering the circle. The total number of
points generated correlates to the area of the square (which is 4), and the total number of
points within the circle correlates to π. As a result, if 1000 points are generated and 800 of
them are in the circle, π is then estimated to be `4*800/1000=3.2`

You will write a program to estimate π using this algorithm. In particular, it is as follows:
- Generate N random points:
  - Each point has two coordinates x and y
  - Both x and y are generated using the function uniform() from package random
  - The range of both x and y are from -1 to 1
- For each point:
  - Calculate their distance to the origin, which is sqrt(x2+y2)
  - If the distance to the origin is greater than 1, the point is outside of the circle. Otherwise, it is inside the circle.
- Count the number of points inside the circle.
- Calculate the estimated π as shown above and return it

The input of your function is the number of random points to generate, and the output is
the estimated π.

**IMPORTANT**: Your function must be named and must have the function parameters listed
in the same order as below. (I will use a python script with a database to automatically test
your function so please don’t do it differently)
```python
def estimate_pi(N):
# your logic here
# return the estimated number
return estimated_pi
```
