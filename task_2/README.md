# DVC sample usage

This projects implements simple use cases for DVC. 
In order to use the code you need to have dvc installed on your machine

## Pipeline

To run code correctly you should follow steps listed below:
- clone repository to local machine
- open the terminal in the repo folder on your local machine  
- to get initial dataset execute 
```dvc pull``` You need to be sure that you have access
  to the assosiated Google Drive folder
- to reproduce pipeline run ```dvc repro```
- to track metrics run ```dvc metrics show\diff```
