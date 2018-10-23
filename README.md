# StoreManager-API
Store Manager api is a simple flask api that powers  a web application that helps store owners manage sales and product inventory records.

##Badges

[![Coverage Status](https://coveralls.io/repos/github/KOKULEBA/StoreManager-API/badge.svg?branch=develop)](https://coveralls.io/github/KOKULEBA/StoreManager-API?branch=develop)
[![Build Status](https://travis-ci.org/KOKULEBA/StoreManager-API.svg?branch=develop)](https://travis-ci.org/KOKULEBA/StoreManager-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/99eca7f702122678178d/maintainability)](https://codeclimate.com/github/KOKULEBA/StoreManager-API/maintainability)

Store Manager api is a simple flask api that powers  a web application that helps store owners manage sales and product inventory records.
### Available Endpoints:
|  Method |  Route |  Functionality |
| :---         |     :---       |          :--- |
| POST   | /api/v1/auth/register     | Creates a user account    |
| POST     | /api/v1/auth/login      | Login a user      |
| POST     | /api/v1/products        | Add a product      |
| GET     | /api/v1/products       | View all products     |
| GET     | /api/v1/products/<product_id>       | Retrieve a single product by id     |
| POST     | /api/v1/sales        | Add a sales record      |
| GET     | /api/v1/sales       | Retrieve all sales records    |


### Requirements
```
  * pip
  * virtualenv
  * python 3 or python 2.7
```

### Setting up

* clone the repo

``` 
git clone https://github.com/KOKULEBA/StoreManager-API.git

```

* Change working directory
```

cd StoreManager-API

```
* Create a virtual environment

```
virtualenv <env_name>

```

* Activate the environment:

```
$source <env_name>/bin/activate

```
* Install dependencies:

```
$pip install -r requirements.txt

```

* Run the app:

```
python run.py

```
### Running the tests
* From terminal run:

```
pytest --cov=app

```
### Deployment

Click [here](#) to view app on heroku

