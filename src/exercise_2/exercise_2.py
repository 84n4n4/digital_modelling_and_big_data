# Exercise 2

import pandas
import numpy as np


# Todo: create a sine wave USING NUMPY given a start and end value and given step size:
def create_sine_wave(start, stop, step_size):
    return None


# Todo - Sort the dataframe df by height and return the sorted dataframe
def sort_by_height(df):
    return None


# Todo - Slice the dataframe to only contain the Male students.
def only_male_students(df):
    return None


# Todo - Slice the dataframe to only contain the Male students taller than 170cm.
def only_tall_male_students(df):
    return None


# Todo - Given that now is 2024, create a new column that contains the year when the students started when they have
#  been studying for 'YearsStudying'. Write the result in a new column named 'YearStarted' and return the new dataframe.
def year_started(df):
    now = 2024
    return None


# Todo - Group the dataframe by sex and return means of age, height, and years studying. (google pandas 'groupby')
#  returned value must be a dataframe.
def group_means(df):
    return None


# Todo - Combine the two dataframes into a single one by concatenation (direction should be clear,
#  the number of columns must not change) and return the new dataframe
def concat_dataframes(df_first, df_second):
    return None


# Todo - Fill the missing values ('NaN') in the dataframe with 0.
def fill_missing_values(df):
    return None


# Todo - convert time to datetime and set the index to be that datetime (and do not have two time columns in the end,
#  returned dataframe should have only the time index and the 'measurement_a' and 'measurement_a' columns.
def make_datetime_index(df):
    return None


# Todo - calculate the difference between each measurement and the previous measurement and put it in a new
#  column namend 'difference'. (since you cannot do this for the first one, set the value to np.nan there.)
def difference_between_measurements(df):
    return None


def main():
    print('\nOutput of create_sine_wave()\n')
    print(create_sine_wave(0, 10, 0.1))

    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George', 'Hannah', 'Ivan', 'Julia'],
        'Height': [165, 170, 175, 160, 180, 155, 168, 172, 178, 169],
        'Age': [25, 32, 40, 22, 28, 30, 35, 26, 41, 29],
        'YearsStudying': [2, 5, 4, 1, 4, 4, 7, 3, 6, 2],
        'Sex': ['Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
    }
    print('\nOutput of sort_by_height()\n')
    print(sort_by_height(pandas.DataFrame(data)))
    print('\nOutput of only_male_students()\n')
    print(only_male_students(pandas.DataFrame(data)))
    print('\nOutput of only_tall_male_students()\n')
    print(only_tall_male_students(pandas.DataFrame(data)))
    print('\nOutput of group_means\n')
    print(group_means(pandas.DataFrame(data)))
    print('\nOutput of year_started()\n')
    print(year_started(pandas.DataFrame(data)))

    data_2 = {
        'Name': ['Kevin', 'Lewis'],
        'Height': [195, 172],
        'Age': [22, 27],
        'YearsStudying': [1, 3],
        'Sex': ['Male', 'Male']
    }
    print('\nOutput of concat_dataframes()\n')
    print(concat_dataframes(pandas.DataFrame(data), pandas.DataFrame(data_2)))

    data_3 = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Edward', 'Fiona', 'George', 'Hannah', 'Ivan', 'Julia'],
        'Height': [165, np.nan, 175, 160, 180, 155, 168, 172, 178, 169],
        'Age': [25, 32, 40, 22, np.nan, 30, 35, 26, 41, 29],
        'YearsStudying': [2, 5, np.nan, 1, 4, 4, 7, np.nan, 6, 2],
        'Sex': ['Female', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
    }
    print('\nOutput of fill_missing_values()\n')
    print(fill_missing_values(pandas.DataFrame(data_3)))

    data_time = {
        'time': ['2024-10-20T01:00+00:00', '2024-10-20T05:34+00:00', '2024-10-20T07:12+00:00', '2024-10-20T12:20+00:00'],
        'measurement_a': [1, 3, 8, 23],
        'measurement_b': [34, 23, 12, 33]
    }
    print('\nOutput of make_datetime_index()\n')
    print(make_datetime_index(pandas.DataFrame(data_time)))

    data_measurements = {
        'measurement_a': [1, 3, 8, 23],
        'measurement_b': [34, 23, 12, 33]
    }
    print('\nOutput of difference_between_measurements()\n')
    print(difference_between_measurements(pandas.DataFrame(data_measurements)))


if __name__ == '__main__':
    main()
