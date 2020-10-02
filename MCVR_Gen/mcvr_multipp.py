import csv, os, random
from time import time
from faker import Faker
import glob
from tqdm import tqdm 
from time import sleep
import pandas as pd


print("\n#####  WELCOME TO THE MCVR(PARSER) VOTER FILE GENERATOR  ######")
print('Do NOT USE Commas - "Exmaple: 10000"\n')
RECORD_COUNT = int(input('How many voters for MCVR PARSER Election File?\nVoters: '))

fake = Faker()

print('\nProcess will create "4 Files" > then combine them')

def create_csv_file():

    with open('./files/MCVR_Election_File_1.csv', 'w', newline='') as csvfile:
        fieldnames = ['ELECTION DATE','ELECTION TYPE','ELECTION NAME','VOTER ID','Last Name','First Name', 'Middle Name', 'Suffix', 'DOB', 'VOTER STATUS', 'VOTER STATUS REASON','ABSENTEE INFORMATION',
        'MAILING ADDRESS','HOUSE NUMBER', 'HOUSE SUFFIX','PRE DIRECTION','STREET NAME','STREET TYPE','POST DIRECTION','UNIT TYPE','UNIT NUMBER', 'NON STANDARD ADDRESS', 'CITY', 'STATE', 'ZIP',
        'POLLING PLACE CODE', 'POLLING PLACE NAME','POLLING PLACE ADDRESS', 'PRECINCT CODE', 'PRECINCT NAME', 'SPLIT','BALLOT STYLE','REGISTRATION DATE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT // 4):
            writer.writerow(
                {
                    'ELECTION DATE': '01/01/2021',
                    'ELECTION TYPE': 'General',
                    'ELECTION NAME': 'MCVR Election',
                    'VOTER ID': random.randint(10000000, 99999999),
                    'Last Name': fake.last_name(),
                    'First Name': fake.first_name(),
                    'Middle Name': fake.first_name(),
                    'Suffix': '',
                    'DOB': '5/27/1980',
                    'VOTER STATUS': random.choice('Active Active Active Active Inactive'.split()),
                    'VOTER STATUS REASON': '',
                    'ABSENTEE INFORMATION': '',
                    'MAILING ADDRESS': '',
                    # 'VOTER STATUS REASON': random.choice('Status Reason 1,Status Reason 2,Status Reason 3'.split(',')),
                    # 'ABSENTEE INFORMATION': random.choice('Absentee Sent,Absentee Received,No'.split(',')),
                    # 'MAILING ADDRESS': '',
                    'HOUSE NUMBER': random.randint(1, 99999),
                    'HOUSE SUFFIX': random.choice('A  B'),
                    'PRE DIRECTION': '',
                    'STREET NAME': fake.street_name(),
                    'STREET TYPE': random.choice('DR ST'.split()),
                    'POST DIRECTION': random.choice('N  S'),
                    'UNIT TYPE': '',
                    'UNIT NUMBER': random.randint(1, 999),
                    'NON STANDARD ADDRESS': '',
                    'CITY': 'ST LOUIS',
                    'STATE': 'MO',
                    'ZIP': '63134',
                    'POLLING PLACE CODE': '1001',
                    'POLLING PLACE NAME': 'AAA BUSCH ACADEMY',
                    'POLLING PLACE ADDRESS': '5910 CLIFTON AVE. ST LOUIS, MO 63109',
                    'PRECINCT CODE': '101',
                    'PRECINCT NAME': '101',
                    'SPLIT': '1',
                    'BALLOT STYLE': '101-1',
                    'REGISTRATION DATE': '01/01/2019'
                }
            )

if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT // 4)), smoothing = .3, ncols = 100, desc ="MCVR_File_1 (1/4) - Creating Data"): 
        sleep(0.00035)

    create_csv_file()

if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT // 4)), ncols = 100, desc ="MCVR_File_1 (1/4) - Creating File"): 
        sleep(0.00035) 

def create_csv_file2():

    with open('./files/MCVR_Election_File_2.csv', 'w', newline='') as csvfile:
        fieldnames = ['ELECTION DATE','ELECTION TYPE','ELECTION NAME','VOTER ID','Last Name','First Name', 'Middle Name', 'Suffix', 'DOB', 'VOTER STATUS', 'VOTER STATUS REASON','ABSENTEE INFORMATION',
        'MAILING ADDRESS','HOUSE NUMBER', 'HOUSE SUFFIX','PRE DIRECTION','STREET NAME','STREET TYPE','POST DIRECTION','UNIT TYPE','UNIT NUMBER', 'NON STANDARD ADDRESS', 'CITY', 'STATE', 'ZIP',
        'POLLING PLACE CODE', 'POLLING PLACE NAME','POLLING PLACE ADDRESS', 'PRECINCT CODE', 'PRECINCT NAME', 'SPLIT','BALLOT STYLE','REGISTRATION DATE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT // 4):
            writer.writerow(
                {
                    'ELECTION DATE': '01/01/2021',
                    'ELECTION TYPE': 'General',
                    'ELECTION NAME': 'MCVR Election',
                    'VOTER ID': random.randint(10000000, 99999999),
                    'Last Name': fake.last_name(),
                    'First Name': fake.first_name(),
                    'Middle Name': fake.first_name(),
                    'Suffix': '',
                    'DOB': '5/27/1980',
                    'VOTER STATUS': random.choice('Active Active Active Active Inactive'.split()),
                    'VOTER STATUS REASON': '',
                    'ABSENTEE INFORMATION': '',
                    'MAILING ADDRESS': '',
                    'HOUSE NUMBER': random.randint(1, 99999),
                    'HOUSE SUFFIX': random.choice('A  B'),
                    'PRE DIRECTION': '',
                    'STREET NAME': fake.street_name(),
                    'STREET TYPE': random.choice('DR ST'.split()),
                    'POST DIRECTION': random.choice('N  S'),
                    'UNIT TYPE': '',
                    'UNIT NUMBER': random.randint(1, 999),
                    'NON STANDARD ADDRESS': '',
                    'CITY': 'ST LOUIS',
                    'STATE': 'MO',
                    'ZIP': '63134',
                    'POLLING PLACE CODE': '1002',
                    'POLLING PLACE NAME': 'SAINT LOUIS ZOO',
                    'POLLING PLACE ADDRESS': '1 GOVERNMENT DRIVE ST. LOUIS, MO 63110',
                    'PRECINCT CODE': '201',
                    'PRECINCT NAME': '201',
                    'SPLIT': '1',
                    'BALLOT STYLE': '201-1',
                    'REGISTRATION DATE': '01/01/2019'
                }
            )

if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT // 4)), ncols = 100, desc ="MCVR_File_2 (2/4) - Creating Data"): 
        sleep(0.00035)

    create_csv_file2()

if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT // 4)), ncols = 100, desc ="MCVR_File_2 (2/4) - Creating File"): 
        sleep(0.00035) 

def create_csv_file3():

    with open('./files/MCVR_Election_File_3.csv', 'w', newline='') as csvfile:
        # ELECTION AND VOTER INFORMATION
        fieldnames = ['ELECTION DATE','ELECTION TYPE','ELECTION NAME','VOTER ID','Last Name','First Name', 'Middle Name', 'Suffix', 'DOB', 'VOTER STATUS', 'VOTER STATUS REASON','ABSENTEE INFORMATION',
        # VOTER ADDRESS  INFORMATION 
        'MAILING ADDRESS','HOUSE NUMBER', 'HOUSE SUFFIX','PRE DIRECTION','STREET NAME','STREET TYPE','POST DIRECTION','UNIT TYPE','UNIT NUMBER', 'NON STANDARD ADDRESS', 'CITY', 'STATE', 'ZIP',
        # VOTER POLLING LOCATION AND BALLOT INFORMATION
        'POLLING PLACE CODE', 'POLLING PLACE NAME','POLLING PLACE ADDRESS', 'PRECINCT CODE', 'PRECINCT NAME', 'SPLIT','BALLOT STYLE','REGISTRATION DATE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT // 4):
            writer.writerow(
                {
                    'ELECTION DATE': '01/01/2021',
                    'ELECTION TYPE': 'General',
                    'ELECTION NAME': 'MCVR Election',
                    'VOTER ID': random.randint(10000000, 99999999),
                    'Last Name': fake.last_name(),
                    'First Name': fake.first_name(),
                    'Middle Name': fake.first_name(),
                    'Suffix': '',
                    'DOB': '5/27/1980',
                    'VOTER STATUS': random.choice('Active Active Active Active Inactive'.split()),
                    'VOTER STATUS REASON': '',
                    'ABSENTEE INFORMATION': '',
                    'MAILING ADDRESS': '',
                    'HOUSE NUMBER': random.randint(1, 99999),
                    'HOUSE SUFFIX': random.choice('A  B'),
                    'PRE DIRECTION': '',
                    'STREET NAME': fake.street_name(),
                    'STREET TYPE': random.choice('DR ST'.split()),
                    'POST DIRECTION': random.choice('N  S'),
                    'UNIT TYPE': '',
                    'UNIT NUMBER': random.randint(1, 999),
                    'NON STANDARD ADDRESS': '',
                    'CITY': 'ST LOUIS',
                    'STATE': 'MO',
                    'ZIP': '63134',
                    'POLLING PLACE CODE': '1003',
                    'POLLING PLACE NAME': 'BRYAN HILL SCHOOL',
                    'POLLING PLACE ADDRESS': '2128 GANO AVE. ST LOUIS, MO 63107',
                    'PRECINCT CODE': '301',
                    'PRECINCT NAME': '301',
                    'SPLIT': '1',
                    'BALLOT STYLE': '301-1',
                    'REGISTRATION DATE': '01/01/2019'
                }
            )

if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT // 4)), ncols = 100, desc ="MCVR_File_3 (3/4) - Creating Data"): 
        sleep(0.00035)

    create_csv_file3()

if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT // 4)), ncols = 100, desc ="MCVR_File_3 (3/4) - Creating File"): 
        sleep(0.00035) 

def create_csv_file4():

    with open('./files/MCVR_Election_File_4.csv', 'w', newline='') as csvfile:
        fieldnames = ['ELECTION DATE','ELECTION TYPE','ELECTION NAME','VOTER ID','Last Name','First Name', 'Middle Name', 'Suffix', 'DOB', 'VOTER STATUS', 'VOTER STATUS REASON','ABSENTEE INFORMATION',
        'MAILING ADDRESS','HOUSE NUMBER', 'HOUSE SUFFIX','PRE DIRECTION','STREET NAME','STREET TYPE','POST DIRECTION','UNIT TYPE','UNIT NUMBER', 'NON STANDARD ADDRESS', 'CITY', 'STATE', 'ZIP',
        'POLLING PLACE CODE', 'POLLING PLACE NAME','POLLING PLACE ADDRESS', 'PRECINCT CODE', 'PRECINCT NAME', 'SPLIT','BALLOT STYLE','REGISTRATION DATE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT // 4):
            writer.writerow(
                {
                    'ELECTION DATE': '01/01/2021',
                    'ELECTION TYPE': 'General',
                    'ELECTION NAME': 'MCVR Election',
                    'VOTER ID': random.randint(10000000, 99999999),
                    'Last Name': fake.last_name(),
                    'First Name': fake.first_name(),
                    'Middle Name': fake.first_name(),
                    'Suffix': '',
                    'DOB': '5/27/1980',
                    'VOTER STATUS': random.choice('Active Active Active Active Inactive'.split()),
                    'VOTER STATUS REASON': '',
                    'ABSENTEE INFORMATION': '',
                    'MAILING ADDRESS': '',
                    'HOUSE NUMBER': random.randint(1, 99999),
                    'HOUSE SUFFIX': random.choice('A  B'),
                    'PRE DIRECTION': '',
                    'STREET NAME': fake.street_name(),
                    'STREET TYPE': random.choice('DR ST'.split()),
                    'POST DIRECTION': random.choice('N  S'),
                    'UNIT TYPE': '',
                    'UNIT NUMBER': random.randint(1, 999),
                    'NON STANDARD ADDRESS': '',
                    'CITY': 'ST LOUIS',
                    'STATE': 'MO',
                    'ZIP': '63134',
                    'POLLING PLACE CODE': '1004',
                    'POLLING PLACE NAME': 'OMEGA CENTER',
                    'POLLING PLACE ADDRESS': '3900 GOODFELLOW BLVD. ST LOUIS, MO 63120',
                    'PRECINCT CODE': '401',
                    'PRECINCT NAME': '401',
                    'SPLIT': '1',
                    'BALLOT STYLE': '401-1',
                    'REGISTRATION DATE': '01/01/2019'
                }
            )

if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT // 4)), ncols = 100, desc ="MCVR_File_4 (4/4) - Creating Data"): 
        sleep(0.00035)                                                                    

    create_csv_file4()  

if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT // 4)), ncols = 100, desc ="MCVR_File_4 (4/4) - Creating File"): 
        sleep(0.00035)  

print('Cleaing up files...')

os.chdir( './files' )
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "MCVR_Election_File.csv", index=False)              

with open('MCVR_Election_File.csv'):  # use the directory name here

    file_name, file_ext = os.path.splitext('MCVR_Election_File.csv')

    with open('MCVR_Election_File.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)

        newfile = ('MCVR_Election_File' + '.txt')

        for line in csv_reader:
            with open(newfile, 'a') as new_txt:    #new file has .txt extn
                txt_writer = csv.writer(new_txt, delimiter = '\t') #writefile
                txt_writer.writerow(line)    

os.remove('MCVR_Election_File_1.csv')
os.remove('MCVR_Election_File_2.csv')
os.remove('MCVR_Election_File_3.csv')
os.remove('MCVR_Election_File_4.csv')
os.remove('MCVR_Election_File.csv')
print('File Generation Complete')