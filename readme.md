# Restaurantapi
## _quick answer for your restaurant!_


REST API used to register, edit and delete recipes, search by recipe name chef name or recipe group name, your team only cares about serving the food in how much the application provides the data.

- Register, edit and delete chefs.
- Register, edit and delete recipe groups.
- Register, edit and delete recipes.
- Search recipes by recipe name, chef name and group name
- Using django-rest-swagger for documentation


### Sumary

- [Aplication](#application)
  - [Features](#features)
  - [Installation](#installation)
- [EndPoints](#end-points)
  - [POST](#post) 
  - [PUT](#put)
  - [DELETE](#delete)
  - [GET](#get)

# Application
application developed using Django REST framework. 

![Build Status](https://www.django-rest-framework.org/img/logo.png)

[Django REST framework](https://www.django-rest-framework.org/ "Django REST framework")

# Dependencies
_

| Dependency | Version |
| ------ | ------ |
|[Python](https://www.python.org/ "Python")|3.9.5|
| [Django](https://www.djangoproject.com/ "Django") |3.2.8 |
| [djangorestframework](https://www.django-rest-framework.org/ "djangorestframework") | 3.12.4 |
| [sqlparse](https://pypi.org/project/sqlparse/ "sqlparse") | 0.4.2 |
| [django-rest-swagger](https://django-rest-swagger.readthedocs.io/en/latest/ "django-rest-swagger") | 2.2.0 |


# Features
- Grouping of urls.
- Unitary tests.
- Creating, editing and deleting chefs
- Creating, editing and deleting recipe groups
- Creating, editing and deleting recipes
- Search recipes by recipe name, chef name and group name

The application urls were grouped by app for better organization and tracking,
so each app has a urls.py file so that all returns from that app
are made by this file.
The unit tests were done thinking about possible failure scenarios and how it is
expected the application to work.
parameter search is used to list results if any, no parameters
is passed the listing will return all results. 

# Installation

>It is recommended to use  [virtualenv](https://virtualenv.pypa.io/en/latest/ "virtualenv") to run the project under development

After creating the virtualenv and active
run:
```sh
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py test
python manage.py collectstatic
python manage.py runserver
```

>you can access the application on port 8000

		http://localhost:8000/


# End-points
the endpoints:
recipes, groups and chefs list, create and delete
to do this, just pass pk(id) as each method has its field structure and must be respected according to the example.
the searchrecipes endpoint searches by parameters just pass the desired parameters for the search and the results are returned.

## accessing the endpoint detailed documentation of all endpoints is provided.
>doc/
_CODE: 200_


# POST
_CODE: 201_
>api/chefs/
>>to create it is necessary to inform the fields.

```sh
{
  "name": "string"
}
```
>api/group/
>>to create it is necessary to inform the fields.
```sh
{
  "name": "string"
}
```
>api/recipes/
>>to create it is necessary to inform the fields.
```sh
{
  "name": "string",
  "details": "string",
  "ingredients": "string",
  "method_of_preparation": "string",
  "time": 0,
  "chef_put": 0,
  "group_put": 0
}
```
# PUT
_CODE: 200_
>api/chefs/
>>to update it is necessary to inform the fields

```sh
{
  "name": "string"
}
```
>api/group/
>>to update it is necessary to inform the fields
```sh
{
  "name": "string"
}
```
>api/recipes/
>>to update it is necessary to inform the fields
```sh
{
  "name": "string",
  "details": "string",
  "ingredients": "string",
  "method_of_preparation": "string",
  "time": 0,
  "chef_put": 0,
  "group_put": 0
}
```

# GET
>api/chefs/{id}/
>>running this method without the id will receive the set of all results, informing the id will receive the specific result.

```sh
[
  {
    "id": 1,
    "name": "Use1"
  },
  {
    "id": 2,
    "name": "User2"
  }
]
```
>api/group/{id}/
>>running this method without the id will receive the set of all results, informing the id will receive the specific result.
```sh
[
  {
    "id": 1,
    "name": "group1"
  },
  {
    "id": 3,
    "name": "group 2"
  }
]
```
>api/recipes/{id}/
>>running this method without the id will receive the set of all results, informing the id will receive the specific result.
```sh
[
  {
    "id": 1,
    "name": "recipe name1",
    "details": "description1",
    "ingredients": "ingredients1",
    "method_of_preparation": "method of preparation1",
    "time": 1,
    "chef": {
      "id": 1,
      "name": "use1"
    },
    "group": {
      "id": 1,
      "name": "group1"
    }
  },
  {
    "id": 2,
    "name": "recipe name2",
    "details": "detail2",
    "ingredients": "ingredients2",
    "method_of_preparation": "method of preparation2",
    "time": 2,
    "chef": {
      "id": 2,
      "name": "user2"
    },
    "group": {
      "id": 3,
      "name": "group 2"
    }
  }
]
```
>api/searchrecipes/?name=name&chefname=chefname&groupname=groupname
>>endpoint fetch values ​​by name just type the parameter
params:
>>- name: recipe name
>>- chefname: chef name
>>- groupname: group name
```sh
[
  {
    "id": 1,
    "name": "recipe name1",
    "details": "description1",
    "ingredients": "ingredients1",
    "method_of_preparation": "method of preparation1",
    "time": 1,
    "chef": {
      "id": 1,
      "name": "use1"
    },
    "group": {
      "id": 1,
      "name": "group1"
    }
  },
  {
    "id": 2,
    "name": "recipe name2",
    "details": "detail2",
    "ingredients": "ingredients2",
    "method_of_preparation": "method of preparation2",
    "time": 2,
    "chef": {
      "id": 2,
      "name": "user2"
    },
    "group": {
      "id": 3,
      "name": "group 2"
    }
  }
]
```
# DELETE
_CODE: 204_
>api/chefs/
>>to delete inform the id

>api/group/
>>to delete inform the id

>api/recipes/
>>to delete inform the id


