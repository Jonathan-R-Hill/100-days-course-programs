import pandas


def convert_temp(temp_day):
    temp_converted = (temp_day.temp * 9/5) + 32 # gets the temp from the row selected
    print(f"{temp_converted}")

data = pandas.read_csv("weather.csv")   # core frame dataframe
#print(data["temp"])    # series type (like a list)


# Getting data per COLUMN
"""
def column():
    data_dict = data.to_dict()
    data_list = data["temp"].to_list()

    print(f"min temp = {data.temp.min()}")      # can be used as either:
    print(f"mean temp = {data.temp.mean()}")    # data.temp    or
    print(f"max temp = {data['temp'].max()}")   # data['temp']
    #                                           # They both work the same
"""

# Getting data by ROW
temp_day = data[data.day == "Monday"]  # getting row that has Monday in day column
hottest_day = data[data.temp == data.temp.max()]  # getting day with max temp

convert_temp(temp_day)

# Creating a DATA FRAME
data_dict = {
    "students" : ["Kane", "Riley", "Jonny"],
    "scores" : [90, 85, 88]
}
my_data_frame = pandas.DataFrame(data_dict)     # Creates a table with the given dict
# my_data_frame.to_csv("new_dataframe.csv") # creates a new file with the data


