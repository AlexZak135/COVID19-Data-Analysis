# Libraries used for the analysis
import pandas as pd

# Import the data
maryland_data = pd.read_csv("Maryland-Covid.csv")

virginia_data = pd.read_csv("Virginia-Covid.csv")

dc_data = pd.read_csv("DC-Covid.csv")

##### Maryland

# Filter for dates from March 5th, 2020 through March 4th 2021
maryland_data["date"] = pd.to_datetime(maryland_data["date"])

maryland_data = maryland_data[(maryland_data["date"] < "2021-03-01")]

# Change the format of the dates over the one year span
maryland_data["date"] = maryland_data["date"].dt.strftime("%m-%d-%y")

# Reset the index of the data frame
maryland_data = maryland_data.reset_index(drop = True)

# Select the columsn of interest in the data frames
maryland_data = maryland_data[["date", "state", "positiveIncrease", "positive",
                               "deathIncrease", "death"]]

# Rename certain columns for increased interpretability
maryland_data = maryland_data.rename({"positiveIncrease" : "daily_cases",
                                      "positive" : "cum_cases",
                                      "deathIncrease" : "daily_deaths",
                                      "death" : "cum_deaths"}, axis = 1)

# Look to see if any of the variables have null values
# Inspect data types of variables and change variable data types if necessary
maryland_data.info()
# The variables "cum_deaths" has 11 null values and it is a float

# Retrieve all of the rows with null values for the variable "cum_deaths"
maryland_null = maryland_data.loc[maryland_data["cum_deaths"].isnull()]
# Null values for "cum_deaths" are before there were any daily Covid-19 cases

# Replace the null values for "cum_deaths" with 0
maryland_data.loc[maryland_data["cum_deaths"].isnull(), "cum_deaths"] = 0

# Change the variable type of "cum_deaths" from float to integer
maryland_data["cum_deaths"] = maryland_data["cum_deaths"].astype("int")

# Get only the month and year of observations in preparation to find monthly totals
maryland_data["date"] = pd.to_datetime(maryland_data["date"]).dt.strftime("%m-%y")

# Find the number of monthly cases and deaths as well as cumulative cases and deaths 
maryland_data = maryland_data.groupby(["date", "state"], sort = False, as_index = False) \
.agg({"daily_cases" : "sum", "cum_cases" : "max", "daily_deaths" : "sum", "cum_deaths" : "max"})

# Make the dates in chronological order and then reset the index
maryland_data = maryland_data.iloc[::-1].reset_index(drop = True)

# Change column certain column names because monthly totals are displayed
maryland_data = maryland_data.rename({"daily_cases" : "monthly_cases",
                                      "daily_deaths" : "monthly_deaths"},
                                       axis = 1)
                                                         
##### Virginia

# Filter for dates from March 5th, 2020 through February 28th 2021
virginia_data["date"] = pd.to_datetime(virginia_data["date"])
virginia_data = virginia_data[(virginia_data["date"] < "2021-03-01") &
                              (virginia_data["date"] > "2020-03-04")]

# Change the format of the dates over the one year span
virginia_data["date"] = virginia_data["date"].dt.strftime("%m-%d-%y")

# Reset the index of the data frame
virginia_data = virginia_data.reset_index(drop = True)

# Select the columsn of interest in the data frames
virginia_data = virginia_data[["date", "state", "positiveIncrease", "positive",
                               "deathIncrease", "death"]]

# Rename certain columns for increased interpretability
virginia_data = virginia_data.rename({"positiveIncrease" : "daily_cases",
                                      "positive" : "cum_cases",
                                      "deathIncrease" : "daily_deaths",
                                      "death" : "cum_deaths"}, axis = 1)

# Look to see if any of the variables have null values
# Inspect data types of variables and change variable data types if necessary
virginia_data.info()

# The variables "cum_cases" is a float so change the data type to an integer
virginia_data["cum_cases"] = virginia_data["cum_cases"].astype("int")
# The variables "cum_deaths" has 10 null values and it a float

# Retrieve all of the rows with null values for the variable "cum_deaths"
virginia_null = virginia_data.loc[virginia_data["cum_deaths"].isnull()]

# Null values for "cum_deaths" are before there were any daily Covid-19 cases
virginia_data.loc[virginia_data["cum_deaths"].isnull(), "cum_deaths"] = 0

# Change the variable type of "cum_deaths" from float to integer
virginia_data["cum_deaths"] = virginia_data["cum_deaths"].astype("int")

# Get only the month and year of observations in preparation to find monthly totals
virginia_data["date"] = pd.to_datetime(virginia_data["date"]).dt.strftime("%m-%y")

# Find the number of monthly cases and deaths as well as cumulative cases and deaths 
virginia_data = virginia_data.groupby(["date", "state"], sort = False, as_index = False) \
.agg({"daily_cases" : "sum", "cum_cases" : "max", "daily_deaths" : "sum", "cum_deaths" : "max"})

# Make the dates in chronological order and then reset the index
virginia_data = virginia_data.iloc[::-1].reset_index(drop = True)

# Change column certain column names because monthly totals are displayed
virginia_data = virginia_data.rename({"daily_cases" : "monthly_cases",
                                      "daily_deaths" : "monthly_deaths"},
                                       axis = 1)

##### DC

# Filter for dates from March 5th, 2020 through February 28th 
dc_data["date"] = pd.to_datetime(dc_data["date"])
dc_data = dc_data[dc_data["date"] < "2021-03-01"]

# Change the format of the dates over the one year span
dc_data["date"] = dc_data["date"].dt.strftime("%m-%d-%y")

# Reset the index of the data frame
dc_data = dc_data.reset_index(drop = True)

# Select the columsn of interest in the data frames
dc_data = dc_data[["date", "state", "positiveIncrease", "positive",
                   "deathIncrease", "death"]]

# Rename certain columns for increased interpretability
dc_data = dc_data.rename({"positiveIncrease" : "daily_cases",
                          "positive" : "cum_cases",
                          "deathIncrease" : "daily_deaths",
                          "death" : "cum_deaths"}, axis = 1)

# Look to see if any of the variables have null values
# Inspect data types of variables and change variable data types if necessary
dc_data.info()

# The variables "cum_deaths" has 14 null values and it a float
# Retrieve all of the rows with null values for the variable "cum_deaths"
dc_null = dc_data.loc[dc_data["cum_deaths"].isnull()]

# Null values for "cum_deaths" are before there were any daily Covid-19 cases
dc_data.loc[dc_data["cum_deaths"].isnull(), "cum_deaths"] = 0

# Change the variable type of "cum_deaths" from float to integer
dc_data["cum_deaths"] = dc_data["cum_deaths"].astype("int")

# Get only the month and year of observations in preparation to find monthly totals
dc_data["date"] = pd.to_datetime(dc_data["date"]).dt.strftime("%m-%y")

# Find the number of monthly cases and deaths as well as cumulative cases and deaths 
dc_data = dc_data.groupby(["date", "state"], sort = False, as_index = False) \
.agg({"daily_cases" : "sum", "cum_cases" : "max", "daily_deaths" : "sum", "cum_deaths" : "max"})

# Make the dates in chronological order and then reset the index
dc_data = dc_data.iloc[::-1].reset_index(drop = True)

# Change column certain column names because monthly totals are displayed
dc_data = dc_data.rename({"daily_cases" : "monthly_cases",
                          "daily_deaths" : "monthly_deaths"},
                           axis = 1)

# Append the three data frames vertically
dmv_data = pd.concat([maryland_data, virginia_data, dc_data], ignore_index = True)

# Change the data type of "date" and "state" to categorical
dmv_data["date"] = dmv_data["date"].astype("category")
dmv_data["state"] = dmv_data["state"].astype("category")

# Export the data to create data visualizations in Tableau
dmv_data.to_csv("~/Desktop/dmv_data.csv", index = False)