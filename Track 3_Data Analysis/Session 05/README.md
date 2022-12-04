`Subject:` Pandas (2)
 `Date:` 16 Oct 22 `Session No.` 05

#### Notes:

- **Time**

  - ```python
    import pandas as pd
    df = pd.read_csv("weather_data.csv", parse_dates=['day'])
    df
    ```

  <p align="center"><img src='https://i.imgur.com/gbLphow.jpeg' width="300"/>
  
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
            'event': 'No event'     })
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
  
- **Interpolation**


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
  
- **Drop NaNs**

  - ```python
    new_df = df.dropna(how='all')
    new_df = df.dropna(thresh=2) 
    ```
  
- **Replace**

  - ```python
    new_df = df.replace(-99999, value=5)
    
    
    new_df = df.replace(to_replace=[-99999,-88888, 10, '0'], value=5)
    
    
    new_df = df.replace({
            'temperature': -99999,
            'windspeed': -99999,
            'day': '1/1/2017',
            'event': '0'    }, np.nan)
    
    new_df = df.replace({
            -99999: np.nan,
            '0': 'Sunny',    })
    ```
  
 - **Get Group**


      - <p align="center"><img src='https://i.imgur.com/mZN46fX.jpeg' width="300"/>


      - <p align="center"><img src='https://i.imgur.com/tTZ6jYY.jpeg' width="300"/>

   - <p align="center"><img src='https://i.imgur.com/FaDCSyb.jpeg' width="500"/>

#### Notebooks:

- [Notebooks](https://github.com/AhmedUZaki/INSTANT-AI/tree/main/Track%203_Data%20Analysis/Session%2005/Notebooks)

### Tasks:

- Append data to exist csv / excel file.

### Solution:

- [Task Solution](https://github.com/AhmedUZaki/INSTANT-AI/tree/main/Track%203_Data%20Analysis/Session%2005/Task%20Solution)
