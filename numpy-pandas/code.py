# --------------
#Importing the modules
import pandas as pd
import numpy as np
from scipy.stats import mode 


#Code for categorical variable
def categorical(df):
    categorical_var = list(df.select_dtypes(include = ['object']).columns)
    return categorical_var
    """ Extract names of categorical column
    
    This function accepts a dataframe and returns categorical list,
    containing the names of categorical columns(categorical_var).
    
    Keyword arguments:
    df - Pandas dataframe from which the columns name will be extracted
        
    Returns:
    categorical_var - List of categorical features
    """
 


#Code for numerical variable
def numerical(df):
    numerical_var = list(df.select_dtypes(include = ['number']).columns)
    return numerical_var
    """ Extract names of numerical column
    
    This function accepts a dataframe and returns numerical list,
    containing the names of numerical columns(numerical_var).
        
    Keyword arguments:
    df - Pandas dataframe from which the columns name will be extracted
    
    Returns:
    numerical_var - List of numerical features
    """
    

#code to check distribution of variable
def clear(df,col,val):
    value_counts = df[col].value_counts()[val]
    return value_counts
    """ Check distribution of variable
    
    This function accepts a dataframe,column(feature) and value which returns count of the value,
    containing the value counts of a variable(value_counts)
    
    Keyword arguments:
    df - Pandas dataframe
    col - Feature of the datagrame
    val - value of the feature
    
    Returns:
    value_counts - Value count of the feature 
    """
   



#Code to check instances based on the condition
def instances_based_condition(df,col1,val1,col2,val2):
    instance = df[(df[col1] > val1) & (df[col2] == val2)]
    return instance
    """ Instances based on the condition
    
    This function accepts a dataframe, 2 columns(feature) and 2 values which returns the dataframe
    based on the condition.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - First feature of the dataframe on which you want to apply the filter
    val1 - Value to be filtered on the first feature
    col2 - Second feature of the dataframe on which you want to apply the filter
    val2 - Value to be filtered on second feature
    
    Returns:
    instance - Generated dataframe
    """
    
    



# Code to calculate different aggreagted values according to month

def agg_values_ina_month(df,date_col,agg_col, agg):
    df['Date/Time'] = pd.to_datetime(df['Date/Time'])
    df['Month'] = df['Date/Time'].apply(lambda x: x.month_name())
    lst = list(df.columns)
    lst = lst[0:1] + lst[-1:] + lst[1:-1]
    df = df[lst]
    aggregated_value = pd.pivot_table(df,index = date_col, values = agg_col, aggfunc = agg)
    return aggregated_value
    """  Aggregate values according to month
    
    This function accepts a dataframe, 2 columns(feature) and aggregated funcion(agg) which returns the Pivot 
    table with different aggregated value of the feature with an index of the month.
     
    Keyword arguments:
    df - Pandas dataframe which has the data.
    date_col - Date feature of the dataframe on which you want to apply to_datetime conversion
    agg_col - Feature of the dataframe on which values will be aggregated.
    agg - Dictionary of aggregate functions with feature as the key and func as the value
    
    Returns:
    aggregated_value - Generated pivot table
    """



# Code to group values based on the feature
def group_values(df,col1,agg1):
    grouping = df.groupby(col1).agg(agg1)
    return grouping

    """ Agrregate values by grouping
    
    This function accepts a dataframe, 1 column(feature) and aggregated function(agg1) which groupby the 
    datframe based on the column.
   
   Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    



# function for conversion 
def convert(df,celsius):
    df[celsius] = df[celsius].apply(lambda x: (x*9/5)+32)
    converted_temp = df
    return converted_temp
    """ Convert temperatures from celsius to fahrenhheit
    
    This function accepts a dataframe, 1 column(feature) which returns the dataframe with converted values from 
    celsius to fahrenhheit.
         
    Keyword arguments:
    df - Pandas dataframe which has the data.
    celsius - Temperature feature of the dataframe which you want to convert to fahrenhheit
    
    Returns:
    converted_temp - Generated dataframe with Fahrenhheit temp.
    
    """
    


# Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable `path` for you.

weather = pd.read_csv(path)

# As you have now loaded the weather data you might want to check the categorical and numerical variables. You can check it by calling categorical and numerical function. 

categorical(weather)
numerical(weather)

#You might be interested in checking the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values.
#You can check it by calling the function clear with respective parameters.
#By using index of the value or name of the value you can check the number of count

clear(weather,'Weather','Cloudy')


# Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can dicretly check it by calling the function instances_based_condition with respective parameters.
wind_speed_35_vis_25 = instances_based_condition(weather,'Wind Spd (km/h)',35,'Visibility (km)',25)


#You have temperature data and want to calculate the mean temperature recorded by month.You can generate a pivot table which contains the aggregated values(like mean, max ,min, sum, len) recoreded by month. 
#You can call the function agg_values_ina_month with respective parameters. 

agg_values_ina_month(weather,'Month','Temp (C)', ['min','max','sum','mean','median'])

# To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. You can call the function group_values.
# Feel free to try on diffrent aggregated functions like max, min, sum, len

mean_weather = group_values(weather,'Weather',['mean'])

# You have a temperature data and wanted to convert celsius temperature into fahrehheit temperatures you can call the function convert.


