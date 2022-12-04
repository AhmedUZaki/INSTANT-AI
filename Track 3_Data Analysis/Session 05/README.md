`Subject:` Pandas(2)
 `Date:` 16 Oct 22 `Session No.` 05

#### Notes:

- **Nan Values**

  <p align="center"><img src='https://i.imgur.com/ZWLqbZe.jpeg' width="600"/>

<p align="center"><img src='https://i.imgur.com/CZ8wezX.jpeg' width="500"/>

<p align="center"><img src='https://i.imgur.com/MzqQXLf.jpeg' width="500"/>

- **Use method to determine how to fill NA values**

  - ```python
    #Forward fill
    new_df = df.fillna(method="ffill")
    #Backword fill
    new_df = df.fillna(method="bfill")
    # axis is either "index" or "columns"
    new_df = df.fillna(method="bfill", axis="columns") 
    ```

  - ```python
    #With Limit
    new_df = df.fillna(method="ffill",limit=2)
    
    ```

- **Interpolate**


  - ```python
    #Interpolation in Python is a technique used to estimate unknown data points between two known data points. Interpolation is mostly used to impute missing values in the dataframe or series while preprocessing data.
    
    new_df = df.interpolate()
    ```


- **Time**

  - ```python
    import pandas as pd
    df = pd.read_csv("weather_data.csv", parse_dates=['day'])
    df
    ```

  <p align="center"><img src='https://i.imgur.com/gbLphow.jpeg' width="400"/>

#### Notebooks

- [Notebooks](https://github.com/AhmedUZaki/INSTANT-AI/tree/main/Track%203_Data%20Analysis/Session%2005/Notebooks)

### Tasks:

1. Append data to exist csv / excel file.

### Solution:

- [Task Solution](https://github.com/AhmedUZaki/INSTANT-AI/blob/main/Track%202_%20Mathematics%20%20for%20Data%20science/Session%2003/Task%20Solution.md)

