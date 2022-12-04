`Subject:` Pandas(2)
 `Date:` 16 Oct 22 `Session No.` 05

#### Notes:

- **Nan Values**

  - ```python
    df = pd.read_csv("stock_data.csv", na_values=["n.a.", "not available"]) 
    ```
  
  - ```python
    df = pd.read_csv("stock_data.csv",  na_values={
            'eps': ['not available'],
            'revenue': [-1],
            'people': ['not available','n.a.']     })
    ```
- **Fill Nan Values**
  
  - ```python
    new_df = df.fillna({
            'temperature': 0,
            'windspeed': df["windspeed"].mean(),
            'event': 'No event'
        })
    ```


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
    '''
    Interpolation is mostly used to impute missing values in the dataframe 
    or series while preprocessing data.
    '''
    new_df = df.interpolate()
    ```


- **Converters**

  - ```python
    #Fill NaNs with a Custom Conditions.
    
    def convert_people_cell(cell):
        if cell=="n.a.":
            return 'data not available'
        return cell
    
    def convert_price_cell(cell):
        if cell=="n.a.":
            return 14.8
        return cell
    
    def convert_eps_cell(cell):
        if cell== "not available":
            return 18.36
        return cell
        
    df = pd.read_excel("stock_data.xlsx","Sheet1", converters= {
            'people': convert_people_cell,
            'price': convert_price_cell,
             'eps':convert_eps_cell    })
    ```
    
    
  
- **Time**

  - ```python
    import pandas as pd
    df = pd.read_csv("weather_data.csv", parse_dates=['day'])
    df
    ```

  <p align="center"><img src='https://i.imgur.com/gbLphow.jpeg' width="300"/>

#### Notebooks

- [Notebooks](https://github.com/AhmedUZaki/INSTANT-AI/tree/main/Track%203_Data%20Analysis/Session%2005/Notebooks)

### Tasks:

1. Append data to exist csv / excel file.

### Solution:

- [Task Solution](https://github.com/AhmedUZaki/INSTANT-AI/blob/main/Track%202_%20Mathematics%20%20for%20Data%20science/Session%2003/Task%20Solution.md)

