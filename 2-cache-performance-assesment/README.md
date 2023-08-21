# Backend test for technical interview

Toucan app builders provide queries to feed data to their apps.
Toucan users will use a browser-based client to get the result of these queries via an HTTP API.
These queries can be executed each time someone visits the app, we call this "live data".
We support a quite wide range of system through connectors. Typically, we expect app builders to target their (analytics) database.

Your objective will be to build a very short prototype of this API, and to assess different cache options that we can provide

## Preliminary questions
What databases or systems do you think our customers would want data from?
What could happened if the queried system has a cost per query?
And if we have many concurrent users?

## First exercise
To create a very simple Proof of Concept of this query API, we'd like a simple HTTP endpoint, that would return data in a predefined format, from an input query.
You can choose any underlying system you'd like to query. We advise to run it in a separate container and load a sample dataset.

A simple versification could look like this:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"table": "world_country_list"}' localhost:5000/query
```
This should return the query results, in a format you find adequate.

## Second exercise
To diminish the workload of the underlying system, we'd like to introduce a cache.

Let's say we'll store results on disk. We'd like to assess the performance of different file formats, so the queries that hit the cache are fast.

We'd like to see a code file, notebook, or whatever else to reproduce the results, that tests different options and enables a data-driven decision.


## Further discussion
We are interested to see how you would address the following points either in code or in comments:
  * metadata
  * security
  * tests
  * doc (a good README is more than enough)
  * portability (easy to install and run)
  * scaling

We are interested in knowing _how_ you would implement it.
**We don't expect you to implement all this.** We really don't.
