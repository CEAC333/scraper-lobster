# scraper-lobster

## Installation Requirements in Ubuntu
```
##### Step 1 – Prerequisites

sudo apt-get update
sudo apt-get install -y unzip xvfb libxi6 libgconf-2-4

##### Install Oracle Java 9 or OpenJDK

sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo apt-get install oracle-java8-set-default

OR

sudo apt-get install openjdk-9-jdk

##### Step 2 – Install Google Chrome

sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
sudo apt-get -y update
sudo apt-get -y install google-chrome-stable

##### Step 3 – Install ChromeDriver 

wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip
unzip chromedriver_linux64.zip

sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver

##### Step 4 – Download Required Jar Files

wget https://selenium-release.storage.googleapis.com/3.9/selenium-server-standalone-3.9.1.jar

wget http://www.java2s.com/Code/JarDownload/testng/testng-6.0.1.jar.zip
unzip testng-6.0.1.jar.zip

##### Step 5 – Start Chrome via Selenium Server

xvfb-run java -Dwebdriver.chrome.driver=/usr/bin/chromedriver -jar selenium-server-standalone-3.9.1.jar

##### INSTALL PHANTOMJS

cd /usr/local/share 
sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
sudo tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2  
sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/share/phantomjs 
sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs 
sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs 
which phantomjs 
phantomjs --version
```
## Creating a venv and installing requirements for project
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running Script
```
source venv/bin/activate
python run.py
```
