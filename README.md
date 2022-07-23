# Government Data Crawler

This code has been used to web scrape the Spanish Government Data for grants and concessions.

## Origin

The original idea came from the [Jaime Obregon repository for "Subenciones"](https://github.com/JaimeObregon/subvenciones) where is the original dataset made by him with web scraping. 

## Purpose of the code

The main purpose of this code is to add some columns to the dataset that could be usefull for making some insights (graphs, statistics, reports...) of the set of grants and concessions made by the spanish government. This insights are meant to be the data analysis part of a bigger project named [Academy Government Data](https://github.com/empathyco/academy-government-data).


## Instructions

### Dataset

The code loops through all the BDNS codes (códigos BDNS) that uses them to construct the urls that are going to be used for the Web Scraping. So the original datasets needs to be downloaded.

### Runing the code and stoping it

The code takes time to access all the urls because of the number of BDNS codes and the time the webpage takes to make a response. So, in order to keep the PC running for a long time (almost a day), the n (or index of the last BDNS number that has its data from the url scraped) can be saved by writing it in the code, so the next time it executes, the code starts from that n. It's also important to save the variable data (with all the data scraped so far) in a file, that it is going to be loaded as data for the following times. Additionally, if it's not the first time the code is being executed, the creating the dataframe part needs to be commented so it doesn´t delete the previous data.

