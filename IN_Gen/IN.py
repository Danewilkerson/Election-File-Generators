import csv
import os
import random
from time import time
from faker import Faker

RECORD_COUNT = int(input("How many voters for INDIANA PASER Election File?"))
fake = Faker()

def create_csv_file():
    with open('./IN_files/IN_Voter_File.csv', 'w', newline='') as csvfile:
        fieldnames = ['PERSON_UID','PRECINCT_UID','PRECINCTNAME','PRECINCT_SPLIT_UID','SUBPRECINCTNAME','REGISTRATION_UID', 'REGISTRATION_SIGNATURE_UID', 'FIRST_NAME', 'LAST_NAME', 'MIDDLE_NAME', 'SUFFIX','DOB', 'SSN4',
                      'DLN', 'IDENTIFICATIONNUMBER','VOTERIDTYPECODENAME','VOTERSTATUS','AFFIRMATIONOFRESIDENCYREQUIREDFLAG',
                       'PROOFOFRESIDENCYREQUIREDFLAG','SIGNATUREREQUIREDFLAG','OVER18FLAG', 'ABSENTEEBALLOTSTATUS', 'ADDRESSLINE1', 
                       'ADDRESSLINE2', 'ADDRESSLINE3', 'CITY', 'STATE','ZIP', 'COUNTRY', 'LOCALITY_UID', 'LOCALITYNAME']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'PERSON_UID': fake.random_int(min=0000000000, max=9999999999),
                    'PRECINCT_UID': fake.random_int(min=0000000000, max=9999999999),
                    'PRECINCTNAME': random.choice('PrecinctA PrecinctB'.split()),
                    'PRECINCT_SPLIT_UID': fake.random_int(min=0000000000, max=9999999999),
                    'SUBPRECINCTNAME': random.choice('SpitA SplitB'.split()),
                    'REGISTRATION_UID': fake.random_int(min=0000000000, max=9999999999),
                    'REGISTRATION_SIGNATURE_UID': fake.random_int(min=0000000000, max=9999999999),
                    'FIRST_NAME': fake.first_name(),
                    'LAST_NAME': fake.last_name(),
                    'MIDDLE_NAME': fake.first_name(),
                    'SUFFIX': random.choice('Dr,PhD,MD,,,,,'.split(',')),
                    'DOB': '01-01-1970 0:00',
                    'SSN4': fake.random_int(min=1001, max=9999),
                    'DLN': fake.random_int(min=0000000000, max=9999999999),
                    'IDENTIFICATIONNUMBER': '',
                    'VOTERIDTYPECODENAME': random.choice('DLN DOBSSN DOBGEN'.split()),
                    'VOTERSTATUS': random.choice('Active Inactive'.split()),
                    'AFFIRMATIONOFRESIDENCYREQUIREDFLAG': fake.boolean(chance_of_getting_true=65),
                    'PROOFOFRESIDENCYREQUIREDFLAG': fake.boolean(chance_of_getting_true=10),
                    'SIGNATUREREQUIREDFLAG': fake.boolean(chance_of_getting_true=10),
                    'OVER18FLAG': '1',
                    'ABSENTEEBALLOTSTATUS': '',
                    'ADDRESSLINE1': fake.street_address(),
                    'ADDRESSLINE2': '',
                    'ADDRESSLINE3': '',
                    'CITY': 'ZIONSVILLE',
                    'STATE': 'IN',
                    'ZIP': '460775850',
                    'COUNTRY': 'US',
                    'LOCALITY_UID': 'b9c154d9-a4b1-49b5-a324-c25a53543477',
                    'LOCALITYNAME': 'Boone',
                }
            )

if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))

    ### create a ballot file generator to go with  the voter files setup. precinct name, split.