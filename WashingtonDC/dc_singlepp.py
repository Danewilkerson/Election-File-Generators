import csv, os, random, shutil
from time import time
from faker import Faker
from tqdm import tqdm 
from time import sleep

print("\n#####  WELCOME TO THE ND VOTER FILE GENERATOR  ######\n")
print('Do NOT USE Commas - "Exmaple: 100000"\n\n')
RECORD_COUNT = int(input('Number of Voters in the Washington DC Parser Election File?\nVoters: '))

fake = Faker()

def create_csv_file():

    with open('./files/Voter_20191115113037_small.csv', 'w', newline='') as csvfile:
        fieldnames = [
                    "Systemid",
                    "Voterid",
                    "SDRid",
                    "ElectionNumber",
                    "ElectionDate",
                    "RegistrationDate",
                    "Last4SSN",
                    "LastName",
                    "FirstName",
                    "MiddleName",
                    "Suffix",
                    "Status",
                    "Party",
                    "TelephoneNumber",
                    "BirthDate",
                    "PrecinctSplit",
                    "Precinct",
                    "BallotStyle",
                    "StreetNumber",
                    "StreetNumberSuffix",
                    "StreetName",
                    "StreetType",
                    "StreetDirSuffix",
                    "ApartmentNumber",
                    "City",
                    "State",
                    "ZipCode",
                    "IdRequiredToVote",
                    "MailingAddress1",
                    "MailingAddress2",
                    "MailingAddress3",
                    "MailingCity",
                    "MailingState",
                    "MailingState",
                    "MailingZip",
                    "PollPlace",
                    "PollName",
                    "PollAddress",
                    "AbsenteeType",
                    "ABSRequestedDate",
                    "ABSMailedDate",
                    "ABSReturnedDate",
                    "ABSStatus",
                    "CityWard",
                    "AdvisoryNeighborhoodCommission",
                    "SingleMemberDistrict",
                    "LastActivityDate",
                    "RecordLastChanged",
                    "FederalElectionOnly"
                    ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Systemid': fake.random_int(min=111111111, max=999999999),
                    'Voterid': fake.random_int(min=1111111111, max=9999999999),
                    'SDRid': '',
                    'ElectionNumber': '120',
                    'ElectionDate': '12/25/19 0:00',
                    'RegistrationDate': '3/5/96 0:00',
                    'Last4SSN': '',
                    'LastName': fake.last_name(),
                    'FirstName': fake.first_name(),
                    'MiddleName': fake.first_name(),
                    'Suffix': '',
                    'Status': 'A',
                    'Party': random.choice('REP, DEM'.split(',')),
                    'TelephoneNumber': '',
                    'BirthDate': '1/28/78 0:00',
                    'PrecinctSplit': '135.03',
                    'Precinct': '135.03',
                    'BallotStyle': '3A',
                    'StreetNumber': '58',
                    'StreetNumberSuffix': '',
                    'StreetName': 'Channing',
                    'StreetType': 'St',
                    'StreetDirSuffix': 'NW',
                    'ApartmentNumber': '',
                    'City': 'District Of Columbia',
                    'State': 'DC',
                    'ZipCode': '20001',
                    'IdRequiredToVote': 'N',
                    'MailingAddress1': '',
                    'MailingAddress2': '',
                    'MailingAddress3': '',
                    'MailingCity': '',
                    'MailingState': '',
                    'MailingState': '',
                    'MailingZip': '',
                    'PollPlace': '135',
                    'PollName': 'Mt. Bethel Baptist Church',
                    'PollAddress': '75 Rhode Island Ave NW',
                    'AbsenteeType': 'C',
                    'ABSRequestedDate': '',
                    'ABSMailedDate': '',
                    'ABSReturnedDate': '',
                    'ABSStatus': '',
                    'CityWard': '5',
                    'AdvisoryNeighborhoodCommission': 'ANC 5E',
                    'SingleMemberDistrict': 'SMD 5E09',
                    'LastActivityDate': '11/8/16 0:00',
                    'RecordLastChanged': '1/25/07 13:25',
                    'FederalElectionOnly': ''
                }
            )


if __name__ == '__main__':
    for i in tqdm(range(int(RECORD_COUNT)), ncols = 100, desc ="File Generation"): 
        sleep(0.00035)

    create_csv_file()

    for file in os.listdir('./Files'):

        file_name, file_ext = os.path.splitext(file)

        if file_ext == '.csv':
            with open('./files/Voter_20191115113037_small.csv','r') as csv_file:
                csv_reader = csv.reader(csv_file)

                newfile = ('./files/Voter_20191115113037_small' + '.txt')

                for i in tqdm(range(int(RECORD_COUNT)), ncols = 100, desc ="File Conversion"): 
                    sleep(0.0001)

                for line in csv_reader:
                    with open(newfile, 'a') as new_txt:
                        txt_writer = csv.writer(new_txt, delimiter = '\t')
                        txt_writer.writerow(line) 

os.remove("./files/Voter_20191115113037_small.csv")

shutil.make_archive("DC_VRS", 'zip', './files')

os.remove("./files/Voter_20191115113037_small.txt")




