# Facebook Crawler
<br>
<p align="center">
  <img src="https://www.bestproxyreviews.com/wp-content/uploads/2020/05/Facebook-Scrapers.jpg" width="500" title="hover text">
</p>
<hr>
<h2 align="center">
  Software that <b>scrape & collect</b> users data like posts, photos, info from <a target="_blank", href="https://www.facebook.com/"> Facebook</a> .
</h2>
<hr>

## Installation
Install from source
```
$ git clone https://github.com/ghanmi-hamza/Facebook_Scraper.git
$ python setup.py install
```
Facebook Crawler requires Webdriver to run. So Please make sure that Firefox is installed + geckodriver :
- 1) Download  geckodriver from this link [geckodriver](https://github.com/mozilla/geckodriver/releases) and extract it.
- 2) Place the path of geckodriver.exe in `myclass.py` in the `executable_path` variable.
  
To download data in the specific path don't forget to change it in `main.py` `save_data(dic,dic["name"],data_path")` else a folder will be created like the path that i used.

<hr>

## Usage

### Command Line : 

```
$ cd Crawler
$ python __main.py__ --url= --n= --pubs= --nb_images= --download=
```

### Options :
- ````--url```` <a>string</a> : Full Url of the profile you want to scrape .
- ````--n```` <a>int</a> : number of pages .
- ````--pubs```` <a>bool</a> : get publication or not .
- ````--nb_images```` <a>int</a> : number of profile images to scrape .
- ````--download```` <a>bool</a> : download data or not .

### Example : 

```
$ python __main.py__ --url="https://www.gamespot.com/profile/airdoggo/" --pubs="False" --nb_images=10 --download="True"
```
<hr>

## Data Extracted 
- user_info
  - Name
  - Intro
  - Friends
  - Gender
  - Birthday
- Events
  
- Images
- Pubs
  - Date
  - Contenu
  - Comments{user,date,comment}

<hr>

- If you liked the repo then kindly support it by giving it a star ⭐
- If there is any bug in the code or if you want any improvement don't hesitate to contact me.
<hr>

## Please Check the test Folder to see the some examples...


<h2 align="left">🌐 Connect</h2>
<p align="left">
  <a href="https://www.linkedin.com/in/hamza-ghanmi-b8a125183/"><img title="Follow on LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
  <a href="mailto:hamza.ghanmi56@gmail.com"><img title="Email" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white"/></a>


</p>
<hr>

License
----
MIT
