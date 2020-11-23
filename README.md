# PolitiCovid19

PolitiCovid19 is a small data visualization application that compares the infection rates of various states with their political party affiliation.

## Description

It takes CSV datasets for Covid19 gathered from https://covidtracking.com/data/download, https://covid.cdc.gov/covid-data-tracker/#cases_casesper100klast7days, and a csv dataset for the 2020 election results that was manually created by referencing https://www.270towin.com/.

The app will generate a pdf of 4 plots. Two line plots, one for democrat affiliated states and another for republican affiliated states, showing the amount of individuals hospitalized from mid january to late november. One bar plot showing the cases per 100000 individual, color coded by state political affiliation. Blue bars are Democratic while red bars are Republican. Finally, a pie chart with two segments showing the total cases. One segment representing total cases in  Republican states and the other Democratic states. 

*disclaimer at the bottom*

## How to run

If you simply plan on running the program, I highly recommend you use regular python and not the provided Jupyter Notebook file as that was simply meant for experimentation.

If you want to mess around with the code and files Jupyter Notebook makes it really easy to change stuff and figure out where you want to take an idea.

### Running Using Python

Clone the repository

`git clone  https://github.com/RicardoValdovinos/PolitiCovid19.git`

You should probably run the following command in some kind of virtual environment just to keep your system clean.
Once you have cloned the repository you can then run the following command to install the required dependencies

`pip install -r requirements.txt`

Now that you have the dependencies installed, if you wish to save the output to a pdf, you can simply run

`python3 main.py`

Otherwise, if you want the plots all displayed outside of the pdf you can use the following command

`python3 main.py show`

### Running Using Jupyter Notebook

If you simply want to mess around in Jupyter Notebook,

Clone the repository

`git clone  https://github.com/RicardoValdovinos/PolitiCovid19.git`

then launch Jupyter Notebook inside of the repository and have at it!

# Disclaimer

I wrote this program for fun. Don't take any of this as being statistically valid or having any real meaning behind it. 
