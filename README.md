# Inwk6312
# Programming Task

  - You have to clone this repo to your account, you should be seeing this on your account, if someone elses name is listed call an instructor for help.
  - Use the Ubuntu VM to write the progrm.
  - Use git add, commit and push to send the code back. 
  - Don't forget to add user name and email on git. 
  - You are allowed to use any form of searching and documentation reading and book reading is promoted
  - You cannot talk to your other people or ask for help!

# Halifax Open Data

You are given a csv file from [Halifax's open data](https://www.halifax.ca/home/open-data). 

  - The file is a csv (comma seperated values); i.e, it's like a excel spreadsheet but simple
  - You can read the file without modification to it.
  - You are asked to extract some information from it. 

### Bus Routes

The CSV you are given has details of the Point representation of bus stop locations which occur along roadways, terminals and park and ride facilities in HRM. Includes information on the type of bus stop and stop number.  This is a point dataset that has been derived from the source data in Hastus (Halifax Transit system).

This is the origianl source  -> https://catalogue-hrm.opendata.arcgis.com/datasets/bus-stops

### Street Centerlines

Another CSV that is given has the details of the Single line representation of every street in HRM with associated street names and types, address block face ranges, ownership and communities. Base layer of street information to be used for civic addressing, emergency service providers and routing requirements.

This is the origianl source  -> https://catalogue-hrm.opendata.arcgis.com/datasets/street-centrelines

## Create a different python file for each task with the format task#.py (where # = task number!)

### Task - 1

Read the StreetCenterlines.csv and return the following(Use functions for each subtask and call them):

  - Easy: A tuple of (STR_NAME,FULL_NAME,FROM_STR,TO_STR) 
  - A histogram of the different types of maintenance. [Result has to be a dictionary with key as Maintenance  and number of streets as values] ["MAINTENANCE"]
  - List of unique owners for the streets ["OWN"]
  - Different types of Street classes ["ST_CLASS"] and a list of streets undereach class

You can ignore edge cases or null data. 

### Task - 2

Use both Bus_Stops.csv and Street_Centerlines.csv to find out number of busstops that are 

- Accessible and in a ARTERIAL road
- Non-Standard and in a LOCAL STREET 
- Inaccessible and in a MINOR COLLECTOR

You can ignore edge cases or null data. 

### Bonus

Handle edge cases and null data.



### Output formatting

If asked for an output, use a string to write the description and the data for it
You need to print a table that has a solution like this (Do not print all the data):

| Stop Number | Location | FCODE |
| ------ | ------ |------ |
| 6123 | Barrington St Before Spring Garden Rd (6123) |Conventional Transit Bus Stop |
| 9110 | Lacewood Terminal Bay 10 (9110) |Terminal |


License
----

MIT
https://www.halifax.ca/home/open-data/open-data-license




