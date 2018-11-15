# SendIt

[![Build Status](https://travis-ci.org/ampaire/sendit_api.svg?branch=develop)](https://travis-ci.org/ampaire/sendit_api)
[![Coverage Status](https://coveralls.io/repos/github/ampaire/sendit_api/badge.svg)](https://coveralls.io/github/ampaire/sendit_api)

SendIt is a platform where people can make delivery orders and have them delivered for them.


## Getting Started

Clone the project using the [link](https://github.com/ampaire/SendIt_api).

### Prerequisites

A browser with the access to the internet.

### Installing

* Clone the project to your local machine
```
git clone https://github.com/ampaire/SendIt_api.git
```

### Features

* Create a delivery order
* Get one delivery order
* Get all delivery orders
* Cancel a delivery order
* Modify an order
* Get users 


### Endpoints

HTTP Method|Endpoint|Functionality
-----------|--------|-------------
POST|api/v1/parcels|Create a parcel
GET|api/v1/parcels/parcelId|Fetch a specific parcel
GET|api/v1/parcels|Fetch all parcels
GET|api/v1/users| Fetct all users
POST|api/v1/parcels/parcelId|Add a parcel delivery order
DELETE|api/v1/parcels/parcelId| Delete a parcel delivery order

### Tools Used
* [PIP](https://pip.pypa.io/en/stable/) - Python package installer.
* [Flask](http://flask.pocoo.org/) - Web microframework for Python.
* [Virtual Environment](https://virtualenv.pypa.io/en/stable/) - Used to create isolated Python environments


### Built With

* Python/Flask

### Authors

Ampaire Phemia