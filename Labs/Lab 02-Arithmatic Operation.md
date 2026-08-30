# Programming in Science - Lab 2-ArithmaticOperation

### Question(s)

1. A ball is dropped from a height `h0` (in meters), and after a given time `t` (in seconds), the height `h(t)` of the ball is given by the formula:

`h(t) = h0 - 0.5 * g * t * t`

Where:
- `h(t)` is the height of the ball at time `t` (in meters).  
- `h0` is the initial height from which the ball is dropped (in meters).  
- `g` is the acceleration due to gravity, which is approximately  `9.8` m/s^2 .  
- `t` is the time elapsed since the ball was dropped (in seconds).  

Tasks:  

1.	Define an algorithm that describes the steps to calculate the height of the ball at time `t` using the given formula.  
2.	Write a Python function that calculates the height of the ball at time `t` after being dropped from an initial height `h0`.  
3.	Perform arithmetic operations to calculate the height of the ball at a given time.  
4.	Test your function by calculating the height of a ball dropped from a height of 50 meters at 3 different time intervals (e.g., at 1 second, 2 seconds, and 3 seconds).
5.	Apply basic debugging techniques to check that your code works for different inputs and edge cases (e.g., when `t = 0` ).  

Example Output for calculate_height() Function:  

When running the program for calculate_height(), here’s how the interaction should look:  
```
Enter initial height: 50
Enter time: 1
Height of the ball at time 1 second = 45.1 meters

Enter initial height: 50
Enter time: 2
Height of the ball at time 2 seconds = 30.4 meters

Enter initial height: 50
Enter time: 3
Height of the ball at time 3 seconds = 5.9 meters
```

2. A car travels at a constant speed of `20` meters per second. Calculate the distance the car will travel in a given time `t`(in seconds). Use the formula:  

`distance = speed * time`

where:  
- `speed` = 20 meters/second  
- `time` = given as input in seconds.  

When running the program for `calculate_car_distance()`, the interaction should look as follows:  

```
Enter time for car (in seconds): 1
The car will travel 20 meters in 1 second.

Enter time for car (in seconds): 2
The car will travel 40 meters in 2 seconds.

Enter time for car (in seconds): 3
The car will travel 60 meters in 3 seconds.
```
