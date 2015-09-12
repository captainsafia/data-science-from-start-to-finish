<link href="https://gist.githubusercontent.com/tuzz/3331384/raw/94f2380c2b798fab2139fd0a8f478c4f2d642e3b/github.css" rel="stylesheet"></link>

# Data Cleaning with Bash and Pandas

Data cleaning is process that typically occurs after data retrieval and before
any analysis, modeling, or visualization is done on a particular data set. 
There is often a perception that data cleaning is cubersome, bothersome, and not
the fun part of the data science, but today we are going to change that perception.
This workshop will guide you through the basic methodology of cleaning a data set
and ensuring that you're process is through and complete.

## What is the data set?

The data set we will be using for this class is a particularly robust data set 
provided by the City of Chicago's Open Data Portal. The data set contains some
informaton about where specific crimes occur, whether or not they lead to an 
arrest, the time of the occurence, the location of the occurence, and some FBI
and CPD codes that categorize the crime.

## What are some questions that we are interested in asking about the data set?

1. What are the seasonal patterns associated with crime in the city?
2. What neighborhoods suffer from the most criminal activity?
3. What is the affect of daily temperature have on crime?
4. What crimes occur in neighborhoods that are considered more affluent versus
those that occur in neighborhoods considered less affluent?

## Setup
1. Install Python 3 using [Anaconda](http://continuum.io/downloads).
2. Go to Chicago's [Open Data Portal](https://data.cityofchicago.org).
3. Browse to the *Crimes - 2001 to present* data set.
4. Select *Export* then select *CSV* under *Download As*.

## Shedding Some Weight

If you've waited for the rather large `crimes.csv` file to download, you must 
have noticed it's rather large size. We'll shortly begin shaping the file, 
inspecting the features avaialble to us, and analyzing which ones we need and 
will need. To start, let's call the `du` command on the file with the `-h` argument,
this will allow us to see how much space the file takes up.

`{{d['clean.sh|idio']['size-file']}}`

Now that's a FAT file, let's take a look at the first couple of rows to see what 
our data looks like. 

`{{d['clean.sh|idio']['check-file']}}`

Now let's take a look at the last couple of rows.

`{{d['clean.sh|idio']['check-end-file']}}`

So it looks like our data covers a timespan from 2001 to 2015. Let's limit ourselves
to the most recent five years of data starting from January 1st, 2010.

`{{d['clean.sh|idio']['slice-file']}}`

This command is quite a mouthful to understand so lets parse it a bit. The first 
part of the command, the part that occurs before the `&&` looks for all lines 
in the file after the first occurence of the string "01/01/2010". Not that this 
will remove the headers of the file, but we'll be able to fix that later. The second
part of the file prints out the size of our now smaller data file. The data might 
not be big anymore but it's still valuable.

#### Bonus Exercises
1. Can you split the data set into two different sections, such as crimes
reported before 2010 and those reported after? Do some research on 
legislative changes with regard to the CPD and try exploring the data 
set before and after those legislations took effect to observe the differences.

## Losing A Limb

If you were fairly observant when viewng the output of the `head -5 crimes.csv` 
command above you might have noticed that the last column contains data that is 
a duplicate of the latitude and longitude files before it. This is reundant data 
so we would like to be able to remove it. Let's work through slicing columns
in the commad line. The first thing we will do is figure out the number of 
columns that are in our CSV by counting the number of commas in the first
row of the file. We can do that using the following command:

`{{d['clean.sh|idio']['remove-unneeded-geolocation-1']}}`

Next will use the cut command and the value we got from the previous command to 
slice out everything but the last column. Not that we need to account for the 
extra comma tat is in the actual "(latitude, longitude)" column when using 
this commnad.

`{{d['clean.sh|idio']['remove-unneeded-geolocation-2']}}`

Now let's see how much weight we've shed!

`{{d['clean.sh|idio']['remove-unneeded-geolocation-3']}}`.

## Going To The Zoo, Going to See the Pandas

Now that we have experminted with working with data in Bash for a litle bit, 
let's start to explore data tools that can make our lives a little bit easier.
Namely, let's beging to wok with Pandas in Python. Pandas is a set of data 
strcuturesa and functions that are designed to make working with data in Python
easy and robust. 

Execute the following command in Terminal, `{{d['clean.sh|idio']['open-ipython']}}`, 
in order to open the iPython console. Let's go ahead and import Pandas using the
following syntax:

`{{d['clean.py|idio']['import']}}`

Next, we will load our file using the following syntax. Note that we are not reading
in a header since we sliced our header out of the file earlier.

`{{d['clean.py|idio']['load']}}`

Now let's try expecting the first couple of rows of our data similar to what we 
did in the Bash prompt earlier.

`{{d['clean.py|idio']['inspect-data']}}`

As we clean up our data some more, it'll be useful to be able to refer to the 
data in the context of column names, so let's use Pandas to add back our column 
names as follows:

`{{d['clean.py|idio']['append-header']}}`

Let's also loop through and force any strings that we have in our data set to be
lowercase for easier string comparisons later on.

`{{d['clean.py|idio']['lowercase-columns']}}`

Now let's check to see if any of our data is missing. Pandas makes this quite easy, 
executing the following command will output the name of the column along with the 
number of rows where data items are missing for that column.

`{{d['clean.py|idio']['whats-missing']}}`

It appears that we've got several rows of data missing in a few of our columns.
Let's go through each column and evalutate whether or not we should keep that 
feature in our data set, omit only the rows which are missing, or investiage
the missing values a bit further.

## What time is it?
Pandas has a simple and robust technique for converting columns into Datetime
objects. In this particular data set, our `date` column is read as a string.
We can confirm this by looking into the `dtypes` attribute of the `date` column.
