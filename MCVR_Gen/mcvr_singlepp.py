import csv
import os
import random
from time import time
from faker import Faker
import glob
from tqdm import tqdm 
from time import sleep

print("\n#####  WELCOME TO THE ND VOTER FILE GENERATOR  ######\n"
"100,000 voter/supp file = approx 35 seconds\n"
"500,000 voter/supp file = approx 2 minutes 55 seconds\n"
"1,000,000 voter/supp file = approx 5 minutes 50 seconds\n")
print('Do NOT USE Commas - "Exmaple: 100000"\n\n')
RECORD_COUNT = int(input('Number of Voters in the North Dakota Parser Election File?\nVoters: '))

fake = Faker()

def create_csv_file():

    with open('./files/MCVR_Election_File.csv', 'w', newline='') as csvfile:
        # ELECTION AND VOTER INFORMATION
        fieldnames = ['ELECTION DATE','ELECTION TYPE','ELECTION NAME','VOTER ID','Last Name','First Name', 'Middle Name', 'Suffix', 'DOB', 'VOTER STATUS', 'VOTER STATUS REASON','ABSENTEE INFORMATION',
        # VOTER ADDRESS  INFORMATION 
        'MAILING ADDRESS','HOUSE NUMBER', 'HOUSE SUFFIX','PRE DIRECTION','STREET NAME','STREET TYPE','POST DIRECTION','UNIT TYPE','UNIT NUMBER', 'NON STANDARD ADDRESS', 'CITY', 'STATE', 'ZIP',
        # VOTER POLLING LOCATION AND BALLOT INFORMATION
        'POLLING PLACE CODE', 'POLLING PLACE NAME','POLLING PLACE ADDRESS', 'PRECINCT CODE', 'PRECINCT NAME', 'SPLIT','BALLOT STYLE','REGISTRATION DATE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'ELECTION DATE': '01/01/2021',
                    'ELECTION TYPE': 'General',
                    'ELECTION NAME': 'MCVR TEST ELECTION',
                    'VOTER ID': fake.random_int(min=11111111, max=99999999),
                    'Last Name': fake.last_name(),
                    'First Name': fake.first_name(),
                    'Middle Name': fake.first_name(),
                    'Suffix': random.choice('PhD,MD'.split(',')),
                    'DOB': '5/27/1980',
                    'VOTER STATUS': random.choice('Active Active Active Active Inactive'.split()),
                    'VOTER STATUS REASON': '',
                    'ABSENTEE INFORMATION': '',
                    'MAILING ADDRESS': '',
                    'HOUSE NUMBER': fake.random_int(min=1001, max=9999),
                    'HOUSE SUFFIX': random.choice('A,B,C,D'.split(',')),
                    'PRE DIRECTION': random.choice('N, S, West, East'.split(',')),
                    'STREET NAME': fake.street_name(),
                    'STREET TYPE': random.choice('DR, ST, AVE, BLVD'.split(',')),
                    'POST DIRECTION': random.choice('N, S, North, South'.split(',')),
                    'UNIT TYPE': random.choice('APT, Trailer, Unit, STE'.split(',')),
                    'UNIT NUMBER': fake.random_int(min=1, max=9999),
                    'NON STANDARD ADDRESS': 'fake non stand address',
                    'CITY': 'St. Louis',
                    'STATE': 'MO',
                    'ZIP': '63134',
                    'POLLING PLACE CODE': '1003',
                    'POLLING PLACE NAME': 'Missouri Botanical Garden',
                    'POLLING PLACE ADDRESS': '4344 Shaw Blvd St. Louis, MO 63110',
                    'PRECINCT CODE': '101',
                    'PRECINCT NAME': '101',
                    'SPLIT': '1',
                    'BALLOT STYLE': '101-1',
                    'REGISTRATION DATE': '01/01/2019'
                }
            )


if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT)), ncols = 100, desc ="File Generation"): 
        sleep(0.00035)

    create_csv_file()

    for file in os.listdir('./files'):  # use the directory name here

        file_name, file_ext = os.path.splitext(file)

        if file_ext == '.csv':
            with open('./files/MCVR_Election_File.csv','r') as csv_file:
                csv_reader = csv.reader(csv_file)

                newfile = ('./files/MCVR_Election_File' + '.txt')

                for i in tqdm(range(int(RECORD_COUNT)), ncols = 100, desc ="File Conversion"): 
                    sleep(0.0001)

                for line in csv_reader:
                    with open(newfile, 'a') as new_txt:    #new file has .txt extn
                        txt_writer = csv.writer(new_txt, delimiter = '\t') #writefile
                        txt_writer.writerow(line) 


