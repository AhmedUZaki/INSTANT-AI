`Subject:` Statistics and Probability (1)
 `Date:` 14 Sep 22 `Session No.` 02

### Session content:

- [What is statistic?](#What-is-statistic)
- [How to choose a sample from a population?](#How-to-choose-a-sample-from-a-population)
- [Measures of Central Tendency](#Measures-of-Central-Tendency)
- [Types of Data](#Types-of-Data)
- [Notebooks](#Notebooks)

### Notes:

#### What is statistic?

- **Statistics** is the study and manipulation of data, including ways to gather, review, analyze, and draw conclusions from data. 
- From Data we can get:
  - **Information** ---> Conclusion.
  - **Insights** ---> Read between the lines.
  - We cannot be certain that the information/Insights that we get from information are always correct, So there is a new field called **Decision Sciences**.
  
- Don't trust any statistics you didn't fake yourself.

- Statistics is the science of changing your mind under **uncertainty**.

#### How to choose a sample from a population?

- Step 1: Define the population (Domain knowledge).
- Step 2: Decide on the sample size.
  - In the worst circumstances, 30-40% max.
- Step 3: Randomly select your sample.
  - Branch off the entire population into multiple **non-overlapping**, **homogeneous** groups and randomly choose final members from the various strata for research.
- Step 4: Repeat the experiment and take the average.
- Step 5: Collect data from your sample.

#### Measures of Central Tendency

- #### Mean

  - This is calculated as the sum of the values in the dataset, divided by the number of observations in the dataset. 

$$
\bar{x} = \frac{\displaystyle\sum_{i=1}^{n}x_{i}}{n}
$$

```python
def mean(x):
    _sum = 0
    for i in x:
        _sum += i
    print(_sum/len(x))
```

- #### Median

  - To calculate the median, we need to sort the values into ascending order and then find the middle-most value. 
  - The closer the mean and median are to each other in value, this will be the best case.

```python
def median(x):
    if (len(x) % 2 == 1):
        x = sorted(x)
        return x[(len(x)// 2)]
    else:
        return ( x[len(x) // 2] + x[(len(x) // 2)+ 1] ) 
```

- #### [Mode](https://medium.com/analytics-vidhya/python-mean-median-mode-functions-without-importing-anything-b2be91870280)

  - Mode is the most frequently occurring value

```python
def mode(lst):
    frequency = {}
    for number in lst:
        frequency.setdefault(number, 0)
        frequency[number] += 1
        
    highestFrequency = max(frequency.values())
    highestFreqLst = []
    
    for number, freq in frequency.items():
        if freq == highestFrequency:
            highestFreqLst.append(number)
    return highestFreqLst
```

### Types of Data

<p align="center"><img src='https://lh3.googleusercontent.com/ouaZ3rY3a2NL356W3kDyYr5HTBFFMzSVK2QSQmptX4oMWmH5rmiBix3RIu-aZ9ptEZZUcKkDhN2A7BmPKgs_bCN6raFf5Car4CxHKsPqu_rmB5f-engm9BsHnTyR2rgLmxCSgq9s' width="400"/>

#### Notebooks

- [04-01-Data and Visualization.ipynb](https://github.com/AhmedUZaki/Basic-Mathematics-for-Machine-Learning/blob/master/Statistics%20and%20Probability%20by%20Hiren/04-01-Data%20and%20Visualization.ipynb)
- [04-02-Statistics Fundamentals.ipynb](https://github.com/AhmedUZaki/Basic-Mathematics-for-Machine-Learning/blob/master/Statistics%20and%20Probability%20by%20Hiren/04-02-Statistics%20Fundamentals.ipynb)
