# Titanic_API_BeCode

## Description
This API is linked to this kaggle competition : https://www.kaggle.com/c/titanic
## Routes

### GET http://127.0.0.1:5000/state

Return a string that says if the server is running
### GET http://127.0.0.1:5000/state

Return a string that says "hello"

### POST http://127.0.0.1:5000/prediction

#### Make a prediction from a csv
You can send to this route a form-data's file, it will make a prediction from the csv sended.
But the key needs to be "file", elsewhere, you will have a error
#### Make a prediction from json object
You can send a json array in the body of the request to make a prediction out of it.
Example of payload : 

```
[{
  "PassengerId": 30,
  "Pclass": 2,
  "Name": "Peter, Master. Michael J",
  "Sex": "male",
  "Age": 23,
  "SibSp": 1,
  "Parch": 1,
  "Ticket": 330911,
  "Fare": 7,
  "Cabin": "",
  "Embarked": "Q"
  }]
```
### GET http://127.0.0.1:5000/state
This route returns "Running" if the server is working.
### POST http://127.0.0.1:5000/passengers
This route allows the creation of the database from a csv.
You need to send the file by a form-data with "file" as key
### GET http://127.0.0.1:5000/train
This route make a model from the database, and save it to used in the prediction route.
## How to run it
1) Git clone the repository
2) Go in the folder
3) Run in cmd : ```docker build .```
4) Run in cmd :  ```docker run  -p 5000:5000 -e URI="{postgresDatabaseURI}" -e PORT=5000  {imageId}```
5) Run in cmd : ```python run.py```
6) Make a post request to the passengers route with the train's csv inside a formdata under the key "file" to create a database
7) Make a get request to the train route to generate a model
8) You can now call the prediction route
There is also a python virtualenvironment included
