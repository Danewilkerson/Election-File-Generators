

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Danewilkerson/Election-File-Generators">
    <img src="images/logo.png" alt="Logo" width="100" height="100">
  </a>

  <h3 align="center">Voter File Generators</h3>

  <p align="center">
    Quickly create Test Data that utilizes all fields to ensure import is working as expected.
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
  * [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Being able to use fake data to represent actual data is always the safest route to prevent actual people's personal information from being exposed.  These are still being updated not only for cleaner more efficient code, but to include more features in the near future which will include full zip voter file packages which include multiple files.   


### Built With
* [Python3](https://docs.python-guide.org/starting/install3/osx/)
* [Pandas](https://pandas.pydata.org/)
* [Faker](https://pypi.org/project/Faker/)


### Prerequisites

* [Python3](https://www.python.org/downloads/)

### Installation

1. Install Python 3
```sh
pip install python3
```
2. Install Pandas
```sh
pip install pandas
```
3. install faker
```sh
pip install Faker
```
4. Clone the repo
```sh
git clone https://github.com/Danewilkerson/Election-File-Generators.git
```


<!-- USAGE EXAMPLES -->
## Usage

To create elections files for testing parsers and regression testing which includes creating new election. 

1. Open up your repo directory in terminal
2. Now run the .py file with python3
```sh
python3 IN.py 
```
3. Enter how many voters you would like in your election.
4. Hit [ENTER] on the keyboard to create.
5. The Voter files will be located in the "Files folder" of the file generator you're using.

<!-- ROADMAP -->
## Roadmap

Will include voter files which are zipped(including multiple data files). 


<!-- CONTRIBUTING -->
## Contributing

The interet which allows me to continue learning every single day.


[product-screenshot]: images/screenshot.png
