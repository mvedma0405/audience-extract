# Audience Statistics Export Tool

Project built with 
[![Python Version](https://img.shields.io/badge/python-3.8-green.svg)](python.org/dev/peps/pep-0569/)



## Getting Started

These instructions will help you run this script on your local environment and generate a CSV file. After the script
runs successfully, a CSV file with the current UNIX timestamp is created in the root directory of the script.

### Installing

step-by-step instructions to get you up and running


Git clone

```commandline
git clone https://github.com/mvedma0405/audience-extract.git
```

Install the requirements 

```commandline
pip install -r requirements.txt
```

Fetch API credentials from the mParticle console

```text
https://docs.mparticle.com/developers/credential-management#creating-new-credentials
```

Account ID

```text
Account ID is displayed on the pop-up when setting up the API credentials 
```

Replace the placeholder credentials in the script with the credentials from the console on the last line of the script, then run 

```commandline
python3 script.py
```