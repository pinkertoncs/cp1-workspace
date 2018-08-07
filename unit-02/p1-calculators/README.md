# Project 1: Calculators

## Overview

- Create a computer program that can solve a variety of generalized mathematical problems.

## Directions
 
- Using the provided template, replace the **pass** statements with your solution code

- Tip: for faster development use file testing (see below)

## Problems

### Tips

- Input
    - cost of a meal
    - tax rate (as a decimal, for example 9% is 0.09)
    - tip rate (as a decimal, for example 0.20)

- Output
    - total amount to pay
- Note
    - tax and tip should both be a percent of the base meal cost

### Temperatures

- Formulas  
    - [https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature](https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature)

- CtoF
    - input Celsius
    - output Fahrenheit
- FtoC
    - input Fahrenheit
    - output Celsius

### Interest

- Formula for compound interest

    ![foo](https://wikimedia.org/api/rest_v1/media/math/render/svg/fa03ff45055223efd29eaaf990c5a85086a139aa "")

- Input
    - P : principal amount (initial investment)
    - r : annual nominal interest rate (as decimal)
    - n : number of times the interest is compounded per year
    - t : number of years
- Output
    - P' : final amount

### Distance

- Formula for distance

    ![foo](https://wikimedia.org/api/rest_v1/media/math/render/svg/617b88d273f6cec8288acc4a071c855ce441e49b "")

- Input 
    - x1 : first point x
    - y1 : first point y
    - x2 : second point x
    - y2 : second point y
- Output
    - approximate distance

### Change
    
- Input
    - price
    - amount paid
- Output
    - total change amount
    - amount of each currency denomination (from 20s to pennies) that should be returned

### Madlib

- Make a madlib!
- For examples, see [http://www.madglibs.com/]( http://www.madglibs.com/)

## Sample Input / Output

- Before you submit you MUST run your program with the provided sample input.

### p1-input.txt

```
# tips
35
.09
.18

# cToF
100

# fToC
32

# interest
100
.05
4
10

# points
42.3601
71.0589
37.7833
122.4167

# change
44.46
100

# madlib
ADD
YOUR 
OWN
VALUES

```

### Output

Your solution may not visually match the sample output, but the calculated answer should be the same for the same input.

```
# tips
44.45

# cToF
212

# fToC
0

# interest
164.36

# dist
51.5613

#change
55.54
 2 20s
 1 10s
 1 5s
 0 1s
 2 quarts
 0 dimes
 0 nicks
 4 penns

# madlib
...
```



    
