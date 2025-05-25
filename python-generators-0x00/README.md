# Task 0: Database Seeding - Airbnb Clone API

## Overview

This script sets up the initial database structure for the Airbnb Clone API project. It connects to a local MySQL server, creates the `ALX_prodev` database if it does not exist, creates a `user_data` table with the required schema, and populates it using data from `user_data.csv`.

## Features

- Connects to MySQL server
- Creates a `user_data` table with:
  - `user_id`: UUID (Primary key and indexed)
  - `name`: VARCHAR
  - `email`: VARCHAR
  - `age`: DECIMAL
- Inserts user data from a CSV file into the table

## Setup

### Requirements

- Python 3.x
- MySQL Server
- `mysql-connector-python` package

### Installation

```bash
pip install mysql-connector-python
