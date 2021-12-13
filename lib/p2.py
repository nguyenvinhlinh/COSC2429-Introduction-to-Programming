# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2021C
# Assignment: 1
# Author: Nguyen Cong Thinh (s3926387)
# Created date: 10/11/2021
# Last modified date: 27/11/2021


import random
from math import sqrt

# Original answers
def estimate_pi(N):
    I = 0
    for i in range(N):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        dis = sqrt(x ** 2 + y ** 2)
        if dis <= 1:
            I += 1
    return "estimated_pi: " + str(4 * I / N)


# Solution
def estimate_pi_2(N):
    inner_counter = 0
    for i in range(N):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        dis = sqrt(x ** 2 + y ** 2)
        if dis <= 1:
            inner_counter += 1
    return 4.0 * inner_counter / N
