import pandas as pd

#load data
chicagodf=pd.DataFrame(pd.read_csv("chicago.csv"))
newyorkdf=pd.DataFrame(pd.read_csv("new_york_city.csv"))
washingtondf=pd.DataFrame(pd.read_csv("washington.csv"))

#used in filter function
city_to_choose={"chicago" , "washington" , "newyork" }
month_to_choose={"january","february","march","april","may","june", "all"}
day_to_choose={"saturday","sunday","monday","tuesday","wednesday","thursday","friday" , "all"}

#dictionary to file name
city_data={"chicago":"chicago.csv"   , "washington":"washington.csv" , "newyork":"new_york_city.csv" }


def filter(): #function to get data from user
    print("let's explore the data .. ")
    while True :
        try:
            entered_city=input("\n1-chicago \n2-newyork \n3-washington \n enter only one city : ").lower()
            if entered_city not  in city_to_choose : print("invalid city")
            else: break
        except: print("")

    while True:
        try:
            entered_month=input("\nenter month : ").lower()
            if entered_month not in month_to_choose : print("invalid month")
            else:break
        except:print("")

    while True:
        try:
            entered_day=input("\nenter day : ").lower()
            if entered_day not in day_to_choose : print("invalid month")
            else:break
        except: print("")
    return entered_city , entered_month ,entered_day

def data_loading(city , month , day): #function to load data
    df=pd.read_csv(city_data[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #create new columns will be used in next functions
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    return df

def common_times(df):#function to calculate the most common time of travels
    print("\n                         common times of travel : \n")
    common_month=df['month'].mode()[0]
    print("{} is the common month".format(common_month))
    print("1=Jan , up to  6=June")
    common_day=df['day'].mode()[0]
    print("{} is the common day".format(common_day))
    common_hour=df['hour'].mode()[0]
    print("{} is the most common hour\n".format(common_hour))

def common_stations(df): #function to calculate the common travel stations
    print("\n                         common travel stations :\n")
    common_start=df['Start Station'].mode()[0]
    print("{} is the most common start station".format(common_start))
    common_end=df['End Station'].mode()[0]
    print("{} is the most common end station\n".format(common_end))

def trip_duration(df):
    print("\n                         Total & Average Travels duration : \n")
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel durations {} sec".format(total_travel_time))
    average_travel_duration=df['Trip Duration'].mean()
    print("Average travel duration {} sec\n".format(average_travel_duration))

def user(df):
    user_type = df['User Type'].value_counts()
    print("{} is the count of user types".format(user_type))

    try:
        gender = df['Gender'].value_counts()
        print("{} is number of gender".format(gender))
    except:
        print("\nNo 'Gender' column in this file.")

    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print("{} is earlest birth year".format(earliest))
        print("{} is recent birth year".format(recent))
        print("{} is common birth year".format(common))
    except:
        print("No birth year column in this file.")


def main():
    while True:
        city , month , day =filter()
        df=data_loading(city,month,day)
        common_times(df)
        common_stations(df)
        trip_duration(df)
        user(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__=="__main__":
    main()
