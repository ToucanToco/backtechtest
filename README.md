# Backend test for technical interview.

Your objective is to build a short API that will allow Toucan app
developpers to get data from a mongo database. The queries are
stored in the backend and given an id which the front end uses to
get data.

Toucan app developpers configure their apps in large CSON files, they
want to add mongo queries to these files. The config files contains many
informations which are not relevant to the backend. All the queries will
be stored behind keys called `query` throughout the file.

```cson
...
chartOption:
  chartType: waterfall
  query:
    domain: waterfall_data
    qty: $gt : 4
...
```

The client side Toucan software will use this configuration to render a
waterfall type of chart using data coming from the following query:

```json
db.collection.find( { "domain": "waterfall_data", "qty": { "$gt": 4 } } )
```

For security reasons, we can't let the client send queries to the
backend, so the backend will record and map all the queries to ids that the
front end will use instead of raw query test to get data. Here is an
example of the front configuration from above with its query replaced
by an id:

```cson
chartOption:
  chartType: waterfall
  query: sPgH45F
```

And on the backend we have a mapping from this ID to the original query:

```python
{'sPgH45F': {'domain': 'waterfall_data', 'qty': {'$gt': 4}}}
```

## Exercice
We expect the server to read the `config.cson` configuration file provided
here, extract all the queries and associate them a unique id.

This id will be used in 2 functionalities :
  * list all the ids of the mongo queries stored in the `config.cson`
  * get the result of one mongo query given the id and required parameters interpolated.

For the sake of testing we provide a docker image, which starts the database and insert
some fixtures needed for the **first** query. All the other queries could be executed
but shouldn't return any result as the needed fixtures aren't available.

For example, if you decide to implement a REST API, this could work like
this:
```bash
curl -X GET localhost:5000/queries
["ec8ca", "429f6", "3f2d9", "07ea2", "cd505", "329b8", ...]

curl -X POST -H "Content-Type: application/json" -d '{"my_filter":"2017"}' localhost:5000/query/ec8ca
[
  {}, // all the docs in the query results
]
```

Of course you are free to implement any type of API (GraphQL, SOAP...) and any framework you want !

## What we are going to look at
The exercice section above is the project requirements. But we are interested to see how you would adress
the following points either in code or in comments :
  * authentification
  * performance
  * tests
  * doc (a good README is more than enough)
  * portability (easy to install)
  * `postprocess` functionality (cf. the `config.cson` file)

Of course we don't expect you to do everything. It is up to you to choose what seems the most relevant for the beta release !
