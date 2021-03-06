# COSC2429 – Introduction to Programming
## Assignment 1 – 2021C. This repo is created to help my friend fix his mistakes.

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

Test: `python -m test/p1-test`


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

![](/images/1.png)

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

Solution:
```python
def estimate_pi(N):
    inner_counter = 0
    for i in range(N):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        dis = sqrt(x ** 2 + y ** 2)
        if dis <= 1:
            inner_counter += 1
    return 4.0 * inner_counter / N
```

Test: `python -m test/p2-test`

## Problem 3:
You are the owner of a pizza restaurant. Every two days, you have to predict the numbers
of pizzas sold in the next two days to prepare the ingredients in advance. The most
important ingredient of a pizza is bread flour. The amount of flour used for each pizza
depends on its size and thickness. A and B are the two best flour providers in the city. You
will need to estimate the total amount of flour and make the decision to buy from the
provider whose price is cheaper. You decide to write a program to help determine the
provider. The recipes of your restaurant states that:



|       | Large | Medium |
|-------|-------|--------|
| Thick | 550g  | 450g   |
| Thin  | 500g  | 400g   |



In addition, 6% of the flour will be wasted while making the pizza.
It is also known that:

- 1kg of flour costs 30.000VND and 31.000VND from providers A and B respectively
- Provider A gives a discount of 3% for orders of less than 30kg and 5% for orders of at least 30kg
- Provider B gives a discount of 5% for orders of less than 40kg and 10% for orders of at least 40kg
- Both providers deliver in bags of 2kg, so the order must be divisible by 2

Your function must take input the following variables: large_thick, large_thin,
medium_thick, medium_thin. They represent the corresponding number of pizzas
estimated for each type.

It must print out the following statement:

```
We need to order ???kg of flour, which costs ???VND if we buy from A and ???VND if we
buy from B.
```

It must also return the order amount (rounded to 2kg), the provider selected and total cost
in this exact order. If there is a tie, we buy from provider A because he is more friendly.

**IMPORTANT**: Your function must be named and must have the function parameters listed
in the same order as below. (I will use a python script with a database to automatically test
your function so please don’t do it differently)

```python
def flour_order(large_thick, large_thin, medium_thick, medium_thin):
# your logic here
# returned variables must be exactly like this
return total_flour, selected_provider, total_cost
```

Solution:
```python
def flour_order(large_thick, large_thin, medium_thick, medium_thin):
    total_flour = math.ceil((0.55 * large_thick) + (0.5 * large_thin) +  (0.45 * medium_thick) + (0.4* medium_thin))

    if total_flour % 2 == 1:
        total_flour = total_flour + 1

    shop_a_price = 30000
    shop_b_price = 31000

    cost_a = 0
    cost_b = 0
    # Shop A - Calculation
    if total_flour >= 30:
        cost_a = total_flour * shop_a_price * 0.95
    else:
        cost_a = total_flour * shop_a_price * 0.97

    # Shop B - Calculation
    if total_flour >= 40:
        cost_b = total_flour * shop_b_price * 0.9
    else:
        cost_b = total_flour * shop_b_price * 0.95

    print "We need to order %dkg of flour, which costs %fVND if we buy from A and %fVND if we buy from B."%(total_flour, cost_a, cost_b)

    selected_provider = ""
    total_cost = 0
    if cost_a <= cost_b:
        selected_provider = "A"
        total_cost = cost_a
    else:
        selected_provider = "B"
        total_cost = cost_b

    return total_flour, selected_provider, total_cost
```

Test: `python -m test/p3-test`


## Problem 4:
You decide to keep track of the number of pizzas sold for each type every day with a stacked bar chart.
Use the turtle module to draw the bar chart with the following requirements:

- Each bar includes four rectangles representing the number of pizzas sold for each type. From bottom to top,
they are large thick, large thin, medium thick and medium thin respectively.
- Each rectangle is of a different color.
- Draw the x and y axes.
- The record date must be printed below the bar.
- The total number of pizzas must be printed on top of the bar.

Example:

![](/images/2.png)

**IMPORTANT**: Your function must be named and must have the function parameters listed
in the same order as below.

```python
def draw_bar_chart(record_date, large_thick, large_thin, medium_thick, medium_thin):
# your logic here
# you don’t need to return anything
```

Solution: `/lib/p4-solution.py`

Test: `python -m lib/p4-solution`
