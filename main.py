# Using requests to make HTTP requests
import requests
from requests.exceptions import ConnectionError

# For displaying the information in a table
from tabulate import tabulate as table

# For import current data in order to get today's time-table from the website
from datetime import date as dt

# Request URL gathered from Network data at time-table.sicsr.ac.in; Manipulating the string according to today's date
with open('./requestURL.txt','r') as url_file:
    request_url = url_file.read()

request_url = request_url.format(from_day = str(int(dt.today().strftime('%d'))), from_month = str(int(dt.today().strftime('%m'))), from_year = str(int(dt.today().strftime('%Y'))), to_day = str(int(dt.today().strftime('%d'))), to_month = str(int(dt.today().strftime('%m'))), to_year = str(int(dt.today().strftime('%Y'))))

try: results = requests.get(request_url,timeout=5)                                 # Making the HTTP request
except ConnectionError:
    print('Connection Error!')
    exit()
else: pass

def process_data(txt):
    dataset = []
    lecture = txt.split('\n')                                       # Converting each lecture into a single element
    lecture.pop(0)                                                  # Removing the headers 
    lecture.pop(-1)                                                 # and last empty dataset from the data
    for i in range(len(lecture)):
        lecture[i] = lecture[i].replace('"','')                     # Removing the existing "" characters
    details = []
    for i in lecture:
        details.append(i.split(','))                                # Splitting the list for only importing certain data
    for lecture in details:
        dataset.append([lecture[0][:lecture[0].rindex('-')], lecture[2], lecture[3][0:8], lecture[4][0:8], int(lecture[5][0])])
    return dataset                                                  # Return the processed data for displaying information

def display_results(dataset):
    if len(dataset)==0:                                             # If no lectures are there today
        print("There are no lectures today.")
        exit()
    noOfLectures = len(dataset)                                     # For displaying the total number of lectures
    noOfHours = 0                                                   # Storing the number of hours
    for i in dataset: noOfHours += i[-1]                            # Calculating the total numbers of hours
    print("Today is:", dt.today().strftime('%d-%m-%Y'))             # Displaying the date in DD-MM-YYYY format
    print("There are {} lectures today".format(noOfLectures))       # No. of Lectures
    print("You have to attend {} hours today".format(noOfHours))    # No. of Hours
    print("Your college day starts from {} and ends at {}".format(dataset[0][2], dataset[-1][3]))
    print(table(dataset, headers = ["Lecture Name", "Room No.", "Start Time", "End Time", "Duration (in hrs)"], tablefmt='grid'))       # Printing the information in a table

display_results(process_data(results.text))
