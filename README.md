# ExamKill
[![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/) [![License](https://img.shields.io/badge/license-GPLv3-red.svg)](https://raw.githubusercontent.com/ttycelery/f609-brute/master/LICENSE)

ExamKill is a Python script used to monitor if ExamBrowser (exambrowser.exe) and Google Chrome (chrome.exe) are running and kill ExamBrowser process in order to bypass its restriction. 
## Software Used
1. ExamBrowser (17.0428) -> older version maybe affected, newer version should fix the problem
2. Google Chrome (64.0.3282.186) -> I think this doesn't matter

## Main Idea
When I was doing an exam using ExamBrowser, the ExamBrowser (exambrowser.exe) then suddenly stopped working but the started browser (Google Chrome / chrome.exe) still running. However, the restrictions created by exambrowser are also "stopped working".

## ExamBrowser Restriction
As far as I know, below is the restrictions created by ExamBrowser:
1. Blocks all keyboard keys except when toggling "Interlock Keys" or Hard Reset (CTRL+ALT+DEL)
2. Blocks mouse right click
3. Blocks Task Manager (taskmgr.exe) to be opened
4. And maybe more undiscovered restriction

