# ExamKill
[![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](https://raw.githubusercontent.com/ttycelery/f609-brute/master/LICENSE)

ExamKill is a Python script used to monitor if ExamBrowser (exambrowser.exe) and Google Chrome (chrome.exe) are running and kill ExamBrowser process in order to bypass its restriction. 

## Software Used
1. ExamBrowser (17.0428): used in Indonesia's 2018 national computer based exam -> older version maybe affected, newer version should fix the problem
2. Google Chrome (64.0.3282.186) -> I think this doesn't matter

## ExamBrowser Restriction
As far as I know, below is the restrictions created by ExamBrowser:
1. Blocks all keyboard keys except when toggling "Interlock Keys" or "Hard Reset Keys" (CTRL+ALT+DEL)
2. Blocks mouse right click
3. Blocks Task Manager (taskmgr.exe) to be opened
4. More undiscovered restriction

## Main Idea
When I was doing an exam using ExamBrowser, the ExamBrowser (exambrowser.exe) then suddenly stopped working because of something unknown but the started browser (Google Chrome / chrome.exe) keeps running. However, the restrictions created by exambrowser are also "stopped working". From that, I can conclude that the started child process (chrome.exe) doesn't get killed even its parent (exambrowser.exe) killed which will allow the users to bypass the restriction created by ExamBrowser (includes some unwanted behavior: like opening calculator, opening book, etc). Finally, I created a simple Python script called ExamKill to monitor if there was ExamBrowser and Chrome Browser are running. If so, it will kill the ExamBrowser, and should bypass ExamBrowser's created restrictions.

## Screenshots


## Usage
Run this script before both ExamBrowser and Google Chrome started. To hide, you can pack it using pyinstaller with ```--noconsole``` argument. You can also use another tool like py2exe or something else. 

## How Does it Work?
After you run the script, it will start to monitor Google Chrome and ExamBrowser processes. When ExamKill reached its expected condition (where both Google Chrome and ExamBrowser are running), it will kill ExamBrowser's process in order to bypass ExamBrowser's created restriction.

## Configuration
You can change process name for Google Chrome or ExamBrowser in case it is different from your situation by editing ```conf``` class in examkill.py.

## Disclaimer
This script is intended only for educational purposes.
