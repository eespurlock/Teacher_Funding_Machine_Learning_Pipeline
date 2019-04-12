'''
Esther Edith Spurlock (12196692)

CAPP 30254

Assignment 2: Machine Learning Pipeline
'''

#Imports
import pandas as pd
import sklearn as skl
import joblib
import os.path

#Constants for this assignment
csv_file = 'credit-data.csv'

def pipeline(csv_name=csv_file):
    '''
    Goes from the beginning to the end of the machine learning pipeline

    Inputs:
        csv_name: the pathway to a csv file that we will download data from
            It is set to the name of the csv_file that I will use for this
            assignment but can be anything
    '''
    train_df, test_df, var, features = import_data(csv_name)
    if var is not None:
        model = train_data(train_df, var, features)
        test_data(model, test_df, var, features)

def import_data(csv_name):
    '''
    Loads data from a CSV file into a pandas datafram, processes the data,
    explores the data, generates features and then splits that data into 
    test and train data

    Inputs:
        csv_name: the pathway to a csv file that we will download data from

    Outputs:
        train_df: a pandas dataframe that has the data we will train on
        test_df: a pandas dataframe that has the data we will test on
        var: a column name that we will want to predict
        features: a list of column names that we will use to predict the 
            variable
    '''
    if os.path.exists(csv_name):
        df_all_data = pd.read_csv(csv_name)
    else:
        print("Pathway to the CSV does not exist")
        return None * 4
    all_cols = df_all_data.columns()
    explore_data(df_all_data)
    df_all_data = process_data(df_all_data, all_cols)
    var, features = generate_var_feat(df_all_data)
    if len(features) != len(all_cols):
        df_all_data = drop_extra_columns(df_all_data, features + var, all_cols)
    train_df, test_df = skl.model_selection.train_test_split(df_all_data,
        train_size=0.9, test_size=0.1)
    return train_df, test_df, var, features

def explore_data(df_all_data):
    '''
    Explores the raw data

    Inputs:
        df_all_data: a pandas dataframe
    '''
    data_summary = df_all_data.describe(include='all')
    #Generate distributions of variables
    #Find correlations between variables
    #Find outliers

def process_data(df_all_data, all_cols):
    '''
    Cleans and processes data

    The more in-depth cleaning is in anticipation of receiving data 
    I haven't seen

    Inputs:
        df_all_data: a pandas dataframe
        all_cols: list of all column names in the data frame

    Outputs:
        df_all_data: a pandas dataframe (cleaned)
    '''
    fill_na_vals = {}
    row_count, col_count = df_all_data.shape
    for col in all_cols:
        if df_all_data[col].isna().sum() > (row_count / 3):
            #Deletes all cols with more than a third of entries listed as na
            df_all_data.drop([col], axis=1)
        for col_compare in all_cols:
            if df_all_data[col].equals(df_all_data[col_compare]):
                #Deletes cols that are duplicates
                df_all_data.drop([col_compare], axis=1)
        if df_all_data[col].dtype is in [int, float]:
            fill_na_vals[col] = df_all_data[col].mean()
        else:
            fill_na_vals[col] = None

    #Fills the NA values of columns with column average or None
    df_all_data.fillna(value=fill_na_vals)

    return df_all_data

def generate_var_feat(df_all_data):
    '''
    Identifies which column will be the variable we want to predict and which
    columns will be the features we want to use to predict the variable

    Inputs:
       df_all_data: a pandas dataframe

    Outputs:
        var: the column name we want to predict
        features: a list of columns we will use to predict the variable
    '''

def drop_extra_columns(df_all_data, col_list, all_cols):
    '''
    Drops columns from the dataframe we are not going to use in analysis

    I am looking ahead with this function. I do not expect to use it for this
    assignment.

    Inputs:
        df_all_data: a pandas dataframe
        col_list: list of columns we are going to use
        all_cols: list of all columns in the dataframe

    Outputs:
        df_all_data: a pandas dataframe
    '''
    to_drop = []
    for col in all_cols:
        if col not in col_list:
            to_drop.append(col)
    if to_drop != []:
        df_all_data.drop(to_drop, axis=1)
    return df_all_data

'''
Notes from sklearn

we must learn from the training set using the fit() method: can only use it once
or what we do will be overwritten 

then we can predict using the predict() method

you can save a model using joblib (maybe??)
'''
def train_data(train_df, var, features):
    '''
    Takes the training data and creates a model to predict futre data

    Inputs:
        train_df: a pandas dataframe
        var: the column we want to predict
        features: the columns we will use to predict var

    Outpts:
        model: a model for analyzing the data
    '''

def test_data(model, test_df, var, features):
    '''
    Tests the model for accuracy

    Inputs:
        model: the machine learning model we are testing
        test_df: a pandas dataframe
        var: the column we want to predict
        features: the columns we will use to predict var
    '''