# backtechtest
Back test for technical interview
You're going to implement an API Server in Python exposing data stored in a mongo database. The mongo queries are stored in a configuration file in CSON format `config.cson`. This config file contains many informations, which are not relevant to the backend. All the queries are stored behind keys called `query` throughout the file.

## Exercice
We expect the server to read the configuration file, extract all the queries and associate them a unique id.
This id will be used in 2 functionalities :
  * list all the ids of the mongo queries stored in the `config.cson`
  * get the result of one mongo query given the id and required parameters interpolated.
For the sake of testing we provide a docker image, which starts the database and insert some fixtures needed for the **first** query. All the other queries could be executed but shouldn't return any result as the needed fixtures aren't available.

For example, if you decide to implement a REST API, this could be a route to retrieve all the ids :
```bash
curl -X GET localhost:5000/queries
["ec8ca", "429f6", "3f2d9", "07ea2", "cd505", "329b8", ...]

curl -X POST -H "Content-Type: application/json" -d '{"my_filter":"2017"}' localhost:5000/query/ec8ca?k
[...]
```

Of course you are free to implement any type of API (GraphQL, SOAP...) and any framework you want !

## What we are going to look at
The exercice section is mandatory. But we are interested to see how you would adress the following points either in code
or in comments :
  * authentification
  * performance
  * tests
  * doc (a good README is more than enough)
  * portability (easy to install)
  * postprocess

Of course we don't expect you to do everything. It is up to you to choose what seems the most relevant for the beta release ! :stuck_out_tongue_winking_eye:
