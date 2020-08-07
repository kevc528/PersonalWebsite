# UPenn Crime Mapping
> Analyzing and mapping the crime reports near UPenn

![Graphs](/content/images/crime-graphs.jpg)

![Map](/content/images/crime-map.jpg)

For this project, I analyzed a few months of crime data at UPenn by scraping it off the crime log posted by the 
Division of Public Safety. After doing some basic I/O and data manipulation using Python, I was able to clean the 
dataset and analyze the trends in crime at Penn. To divide the crimes into categories, I used a wordnet from the 
NLTK package to find synonyms of crime categories, like theft or assualt, within the crime descriptions.

Then I used HTML/CSS/JavaScript with Google Maps API to map crime with filters on time of day and type of crime.