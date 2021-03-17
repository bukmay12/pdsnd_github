import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ['chicago','washington','new york city']
    while (city not in ['chicago','washington','new york city']):
        city = input('\nWould you like to see data from chicago, washington or new york city?\n').lower()
        if city not in ['chicago','washington','new york city']:
            print("Invalid input, please try again.")
            continue
        else:
            break
    
  
       
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ['january', 'february', 'march', 'april', 'may', 'june','all']
    while (month not in ['january', 'february', 'march', 'april', 'may', 'june','all']):
        month = input("\nWhich is your preferred month of interest? january, february, march, april, may, june, or type 'all' to apply no month   filter?\n").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june','all'):
            print('Invalid input, please try again.')
            continue
        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    while (day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']):
        day = input("\nWhat day of the week do you want to see? Please enter the day: sunday, monday, tuesday, wednesday, thursday, friday, saturday, or type 'all' to apply no month filter?\n").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print('Invalid input, please try again.')
            continue
        else:
            break
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month          # use value_counts function & the index max method
    most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", most_common_month)
    
    # TO DO: display the most common day of week        # use value_counts function & the index max method
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print('This is the most common day:', most_common_day_of_week)
    
    # TO DO: display the most common start hour              # use value_counts function & the index max method
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)


    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)


    # TO DO: display most frequent combination of start station and end station trip  # use groupby on two columns and count methods
    freq_combo_station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost frequent combination of start station and end station trip:', most_common_start_station, " and ", most_common_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('\nCounts of Gender:\n', gender_count)
    else:
        print('\nCounts of Gender cannot be calculated because Gender does not appear in the dataframe\n')


    # TO DO: Display earliest, most recent, and most common year of birth       
    if 'Birth Year' in df:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest year of birth:', earliest_year)
    else:
        print('\nEarliest year of birth cannot be calculated because Birth Year does not appear in the dataframe')

        
    if 'Birth Year' in df:
        most_recent_year = df['Birth Year'].max()
        print('\nMost recent year of birth:', most_recent_year)
    else:
        print('\nMost recent year of birth cannot be calculated because Birth Year does not appear in the dataframe')
    
        
    if 'Birth Year' in df:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost common year of birth:', most_common_year)
    else:
        print('\nMost common year of birth cannot be calculated because Birth Year does not appear in the dataframe')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        
        i = 0
        raw = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
        pd.set_option('display.max_columns',200)
        
        while True:
            if raw == 'no':
                break
            print(df[i:i+5])
            raw = input('\nWould you like to see next rows of raw data?\n').lower()
            i += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
