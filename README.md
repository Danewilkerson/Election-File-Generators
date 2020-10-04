<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



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

Python 3
* pip
```sh
pip install python3
```

### Installation

1. Install Python 3
2. Clone the repo
```sh
git clone https://github.com/Danewilkerson/Election-File-Generators.git
```
3. Install Pandas packages
```sh
pip install pandas
```
4. install faker
```sh
pip install Faker;
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
5. The Voter files will be located in the "Files folder of the file generator"

<!-- ROADMAP -->
## Roadmap

Will include voter files which are zipped(including multiple data files). 


<!-- CONTRIBUTING -->
## Contributing

The interet which allows me to continue learning every single day.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
