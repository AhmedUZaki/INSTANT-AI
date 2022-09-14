`Subject:` Statistics 
 `Date:` 14 Sep 22 `Session No.` 02

### Session content:

- [What is statistic?](#What-is-statistic)

- [How to choose a sample from a population?](#How-to-choose-a-sample-from-a-population)

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

#### Notebook

- 

#### Mean/Median/Mode

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

So, for our graduate salaries; first lets sort the dataset:

| Salary      |
|-------------|
| 40,000      |
| 50,000      |
| 50,000      |
| 54,000      |
| 55,000      |
| 59,000      |
| 189,000     |

There's an odd number of observation (7), so the median value is at position (7 + 1) &div; 2; in other words, position 4:

| Salary      |
|-------------|
| 40,000      |
| 50,000      |
| 50,000      |
|***>54,000*** |
| 55,000      |
| 59,000      |
| 189,000     |

- #### Median

  - To calculate the median, we need to sort the values into ascending order and then find the middle-most value. 

```python
def median(x):
    if (len(x) % 2 == 1):
        x = sorted(x)
        return x[(len(x)// 2)]
    else:
        return ( x[len(x) // 2] + x[(len(x) // 2)+ 1] ) 
```

- #### Mode

  - Mode is the most frequently occurring value
