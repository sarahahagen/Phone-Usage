##############################################################
# Programmer: Sarah Hagen
# Class: CPSC 222-01, Fall 2020
# Final Project
# 12/12/2020
#
# Description: This program computes mutliple aspects on a 
#              CSV file using DataFrames and Series.
##############################################################

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

def load_csv_file(filename):
    '''
    Loads the CSV files into a data frame
    Parameter data: uses filename to retreive the data
    Returns: the data frame of the CSV file
    '''
    screen_time_df = pd.read_csv(filename, index_col=0)

    return screen_time_df

def column_slicing(col, dataframe):
    '''
    Returns a Series from user-input from a column from the data frame name 
    Parameter data: uses the column name and a data frame to create the Series
    Returns: the Series of column
    '''
    col_data_ser = dataframe[col].copy()

    return col_data_ser

def column_slicing_by_date(start_date, end_date, col, df_name):
    '''
    Returns a Series from user-input from a column from the data frame name 
    Parameter data: uses the start to end dates, the column name, and a data frame to create the Series
    Returns: the Series of column with the selected dates
    '''
    # start to end date of the Data Frame
    dates_df = df_name.loc[start_date: end_date]

    # column name with the start to end date Data Frame
    dates_column_ser = dates_df[col]
    numeric_data_ser = pd.to_numeric(dates_column_ser)

    return numeric_data_ser

def clean_col(column_data_ser):
    '''
    Cleans marital status column
    Parameter data: uses the marital status column for cleaning
    Returns: the Series, cleaned
    '''
    
    return column_data_ser

def join(merge_on, df_name_1, df_name_2):
    '''
    Returns a data frame of two merged dataframes into a CSV file
    Parameter data: uses the string to be merged on, and two data frames to merge into one data frame
    Returns: a merged data frame
    '''
    merged_df = df_name_1.merge(df_name_2, on=merge_on)

    return merged_df

def compute_stats(column_data):
    '''
    Computes the sum, the mean, standard deviation, and median/smallest/largest value in the column
    Parameter data: uses Series data from the given column for this function
    Returns: sum, mean, standard deviation, and smallest/largest/median
    '''
    # computing the sum of the numbers
    total = column_data.sum()

    # computing the average (mean) of the numbers
    avg = column_data.mean()
   
    # computing the standard deviation of the list of numbers
    std_dev = column_data.std()
    
    # computing smallest and largest numbers
    smallest = column_data.min()
    smallest_rounded = round(smallest, 2)

    largest = column_data.max()
    largest_rounded = round(largest, 2)
    
    # computing median number
    median = column_data.median()
    median_rounded = round(median, 2)
    
    # computing the range
    #difference = largest - smallest
    #difference_rounded = round(difference, 2)
    
    return total, avg, std_dev, smallest_rounded, largest_rounded, median_rounded

def histogram(data, category, total, mean, std_dev, x_label):
    '''
    Creates a histogram from the given data and displays in the Jupyter Notebook
    Parameter data: all of the statistics needed to create the histogram
    Returns: nothing
    '''
    plt.figure()
    plt.hist(data, bins=30, facecolor="green")
    title = f"{category} Total (N={total}): Mean={mean}, StdDev={std_dev}"
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel("Frequency")
    plt.show()
    
def line_plot(x_axis, y_axis, mins_times, category):
    '''
    Creates a line plot from the given data and displays in the Jupyter Notebook
    Parameter data: all of the statistics needed to create the line plot
    Returns: nothing
    '''
    plt.figure(figsize=[10.0, 5.0])
    plt.plot(x_axis, y_axis)
    title = f"Total {mins_times} of {category}"
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(mins_times)
    plt.xticks(rotation=90, horizontalalignment="center", fontsize=7.5)
    plt.show()
    
def pie_chart(data):
    '''
    Creates a pie chart from the given data and displays in the Jupyter Notebook
    Parameter data: all of the statistics needed to create the pie chart
    Returns: nothing
    '''
    plt.figure(figsize=[15.0, 5.0])
    plt.pie(data, labels=["Social Networking", "Entertainment", "Productivity", "Other", "Creativity", "Reading and Reference", "Pickups", "Notifications"], autopct="%1.1f%%", textprops={'fontsize': 8})
    plt.title("The Ratio of All Attributes to Eachother")
    plt.show()