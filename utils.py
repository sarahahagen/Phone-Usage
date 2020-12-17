##############################################################
# Programmer: Sarah Hagen
# Class: CPSC 222-01, Fall 2020
# Final Project
# 12/15/2020
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

def join(merge_on, df_name_1, df_name_2):
    '''
    Returns a data frame of two merged dataframes into a CSV file
    Parameter data: uses the string to be merged on, and two data frames to merge into one data frame
    Returns: a merged data frame
    '''
    merged_df = df_name_1.merge(df_name_2, on=merge_on)
    merged_df.to_csv("merged_df.csv")

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
    
    return total, avg, std_dev, smallest_rounded, largest_rounded, median_rounded

def print_stats_minutes(att, total, avg, std_dev, smallest, largest, median):
    '''
    Displays the statistics for minutes attribute in the Jupyter Notebook
    Parameter data: all of the statistics computed
    Returns: nothing
    '''
    print(att, "Total:", total, "minutes")
    print(att, "Average:", avg, "minutes")
    print(att, "Standard Deviation:", std_dev, "minutes")
    print(att, "Least:", smallest, "minutes")
    print(att, "Most:", largest, "minutes")
    print(att, "Median:", median, "minutes")
    print(att, "Range:", largest - smallest, "minutes")
    
def print_stats_times(att, total, avg, std_dev, smallest, largest, median):
    '''
    Displays the statistics for number of times attributes in the Jupyter Notebook
    Parameter data: all of the statistics computed
    Returns: nothing
    '''
    print(att, "Total:", total, "times")
    print(att, "Average:", avg, "times")
    print(att, "Standard Deviation:", std_dev, "times")
    print(att, "Least:", smallest, "times")
    print(att, "Most:", largest, "times")
    print(att, "Median:", median, "times")
    print(att, "Range:", largest - smallest, "times")


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