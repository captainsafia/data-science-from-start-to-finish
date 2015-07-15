# Data Cleaning with Bash and Panda

Data cleaning is process that typically occurs after data retrieval and before
any analysis, modeling, or visualization is done on a particular data set. 
There is often a perception that data cleaning is cubersome, bothersome, and not
the fun part of the data science, but today we are going to change that perception.
This workshop will guide you through the basic methodology of cleaning a data set
and ensuring that you're process is through and complete.

# What is the data set?

The data set we will be using for this class is a particularly robust data set 
provided by the City of Chicago's Open Data Portal. The data set contains some
informaton about where specific crimes occur, whether or not they lead to an 
arrest, the time of the occurence, the location of the occurence, and some FBI
and CPD codes that categorize the crime.

# What are some questions that we are interested in asking about the data set?

1. What are the seasonal patterns associated with crime in the city?
2. What neighborhoods suffer from the most criminal activity?
3. What is the affect of daily temperature have on crime?
4. What crimes occur in neighborhoods that are considered more affluent versus
those that occur in neighborhoods considered less affluent?

# Setup

1. Install Anaconda with Python 2.7.*.
2. Download the huge crimes.csv file at http://bit.ly/1HtHxBh.
