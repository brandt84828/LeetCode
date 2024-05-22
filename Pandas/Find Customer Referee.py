#1
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df=customer[(customer['referee_id']!=2) | pd.isnull(customer['referee_id'])]
    df=df[['name']]
    return df

#2
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer['referee_id'].fillna(0, inplace = True)
    filtered_data = customer[customer['referee_id'] != 2] 
    
    return filtered_data[['name']]