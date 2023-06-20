
# VacantCoach

A command line python tool to show available seats of railway for possible upcoming days.


## Features

- Shows available seats for upcoming 10 days
- Sorts out avaiable seats on the basis of class and train
- Searches for every possible classes on every possible trains traveling among current and desired destination


## Installation

```bash
  git clone https://github.com/afjal-al-sayed/vacantcoach
  cd vacantcoach
  python3 -m pip install -r requirements.txt
  python3 main.py
```

    
## Usage/Examples

```bash
Welcome to VacantCoach
Please enter the station name you want to depart from: Brahmanbaria
Please enter the station name you want to go: Dhaka


**   Brahmanbaria ->> Dhaka   **


Searching for available seats. Please wait.....

>>>>><<<<<<<<<<<<< 24-Jun-2023 <<<<<<<<<<<<<<<<<<<<<<<


MOHANAGAR EXPRESS (721)
---------------------------------
S_CHAIR                  13
SNIGDHA                  2



>>>>><<<<<<<<<<<<< 25-Jun-2023 <<<<<<<<<<<<<<<<<<<<<<<


MOHANAGAR EXPRESS (721)
---------------------------------
S_CHAIR                  7


...

```


## Things to keep in mind
- use proper station names to get correct result
- if it shows any error, try to run the file again and check if all required packages are installed correctly on your device
- it may be slow in some cases. So, please be patient.
## Terms of Use

 - This tool illustrates **publicly available data** from railway's website and automates it. **It doesn't sell tickets.**
 - It doesn't access any kind of private data nor use any method that might be harmful/illegal for data sources.
 - In some cases it may fail to pull data from data sources
 - VacantCoach nor it's author doesn't ensure to any of the users of it that the data provided by the tool is correct and reliable. It totally depends upon the data sources it relies on.
 - VacantCoach only shows the available seats at that particular moment. It doesn't ensure that anyone could be able to buy those tickets. It totally depends on the Railway authority.
 - VacantCoach nor it's author has any kind of relation or deal with railway.
 - **This tool is made for educaitonal perposes only**. The user will be responsile for using it. VacantCoach nor it's author will take any kind of responsibility.



## Data Source
VacantCoach uses publicly available data from the following website: https://eticket.railway.gov.bd/