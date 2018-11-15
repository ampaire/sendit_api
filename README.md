# SendIt

[![Build Status](https://travis-ci.org/ampaire/sendit_api.svg?branch=develop)](https://travis-ci.org/ampaire/sendit_api)
[![Coverage Status](https://coveralls.io/repos/github/ampaire/sendit_api/badge.svg)](https://coveralls.io/github/ampaire/sendit_api)

SendIt is a platform where people can make parcel delivery orders and have them delivered for them.


## Getting Started

Clone the project using the [link](https://github.com/ampaire/SendIt_api).

### Prerequisites

A browser with the access to the internet.

### Features

* Create a delivery order
* Get one delivery order
* Get all delivery orders
* Cancel a delivery order
* Modify an order
* Get users 


| REQUEST | ROUTE | FUNCTIONALITY |
| ------- | ----- | ------------- |
| POST | /api/v1/auth/login | Logs in a user |
| POST | api/v1/auth/logout | Logs out a user |
| POST | api/v1/auth/register | Register a new user |
| GET | api/v1/parcels | Retrieves all parcels |
| POST | api/v1/parcels | Creates a new parcel order |
| DELETE | api/v1/parcels/&lt;parcelId&gt; | Delete a parcel order |
| GET | api/v1/parcels/&lt;parcelId&gt; | Get a parcel order by id |
| PUT | api/v1/parcels/&lt;parcelId&gt; | Update a specific parcel order  |
| GET | api/v1/parcels/&lt;parcelId&gt;/reviews | Get reviews of a parcel order |
| POST | ap1/v1/parcels/&lt;parcelId&gt;/reviews | Post a review about a parcel order|

## BUILT WITH

* Flask - Python Framework used

## SETTING UP APPLICATION

1. Create a folder sendit_api and clone repository to the folder

    **```git clone https://github.com/ampaire/sendit_api.git```**

2. Create a virtual environment that you are going to use while running the application locally

    **```$ virtualenv venv```**

    **```$ source venv/bin/activate```**

**NB: [More Information on setting up Virtual environments here](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)**

3. Install all project dependencies using

    **```pip3 install -r requirements.txt```**

4. Set up a secret key for security purposes of your application

    **```SECRET_KEY = '<your_secret_key>'```**

## RUNNING APPLICATION

1.  To launch the application, run the following command in your terminal

    **```python run.py```**


2. To run tests on the application, run the following command in your terminal

    **```pytest -v```**



### Tools Used
* [PIP](https://pip.pypa.io/en/stable/) - Python package installer.
* [Flask](http://flask.pocoo.org/) - Web microframework for Python.
* [Virtual Environment](https://virtualenv.pypa.io/en/stable/) - Used to create isolated Python environments



### Authors

Ampaire Phemia