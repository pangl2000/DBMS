# Local Championship SQL DBMS

Creation of SQL database for a local championship and built GUI for interaction with user.

## Table of Contents
- [Local Championship SQL DBMS](#project-name)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)

## Description

This project contains a database file with data for a Local Championship. Data such as teams participating and players competing are recorded along with the matches and the statistics produced. A GUI is 
also created to help both a simple user and an admin interact with those data.

## Features

Simple User features:
-View player ranking based on goals scored
-View team ranking based on goals scored
-View gorups stage and group ranking based on wins
--View matches of groups stage
---View players competing in specific match
-View knockouts stage and the final winner
-View team participating
--View players of each team

Admin features:
ALL USER FEATURES +
-View data from database
-Insert data to database


## Installation

Download the files. If you don't download the Local_Championship.db file, then you need to run first the python file createDB.py. Then you need to install DB browser for SQLite, open the Local_Championship.db
file created by createDB.py, copy the SQL code from insert.sql to the execute SQL tab and run. Afterwards, you can open the modernDatabaseGUI.py and run it.

## Usage

At first you are prompted to login. By entrying admin as username and adminpassword as password you log-in as admin. Otherwise you log-in as user. Then, you can start using the app features described above.
