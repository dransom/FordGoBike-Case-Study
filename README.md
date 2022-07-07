# Ford GoBike Data Anlysis
## by Dane


## Dataset

The data explored is the Ford GoBike data from San Francisco, California from February 1st to 28th, 2019.  The data contains the following information about the riders:

- Memember information: gender, birth year, Subscriber or Customer (one time user).
- Ride information: duration, start station, end station, start and end times.
- Station information: station name, longitutde, latitude.

The data was wrangled/modified in the following ways:

### Quality issues
1. start_time & end_time are strings and should be datetime.
2. start_station_id & end_station_id are floats and should be strings (also drop .0)
3. bike_id: int to string
4. member_gender: string to category
5. user_type: string to category
6. birth_year: float to int

### Tidiness issues
1. Separate station information into a separate DF & file: (station)id, latitude, longitude, & name.  In main DF, keep start_station_id & end_station_id in the column where the ID refers to the station DF.

All the wrangling is documented in Ford-GoBike-Data-Wrangling.ipynb

After the wrangling was done, it was separated into a separate Python script (titled 'gobike_data_wrangling.py'), in order to automate it for future analysis and for the analysis performed.

## Summary of Findings

The goal of the study was to examine some of the riding insights of the different members.

Here is some basic information about the riders during the analysis:

- The majority of the riders identify as Male (~70%).
- The majority of riders are born in the 1980s and 1990s.  There is a percentage of riders who marked their birh year as pre-1940s; while it is possible some of the riders are that age, many of them most likely marked a large enough year to get through prompts for rental.
- The fast majority of riders are Subscribers and not Customers.

All the above data will be included.

After examining some basic member information about riders, the rides were examined.  Specifically, the duration, start times, and start days of rides were examined.  It was found that there are specific times and days that most rides happened.  This information  will not be included in the final because the amount of the influence between the member types is so huge.

After the above, more detailed information was analyzed about the rides differences between Subscribers and Members.  It was found that Subscribers tend to ride their bike around traditional commuting times/days and usually bike for shorter periods of times.  Customers behaved different as they ride the bikes for longer, generally around weekends (Thursday - Monday), and at all hours; this may be because Customers are more likely to be people visiting as they would not need a monthly subscription.  This data will be included in the final presentation.

## Key Insights for Presentation

> Select one or two main threads from your exploration to polish up for your presentation. Note any changes in design from your exploration step here.

The insights for the presentation will focus on two main areas:
1. Basic information/analysis of the ridership from the dataset.
2. Insights into Subscibers vs Customes ridership in terms of when they start their ride (hour of day, day of week) and differences in the duration of their ride.

My originaly thought was to explore the differences all differences in riders such as gender, year of birth, etc.  However, I found little difference in the ride lengths, etc of different genders.