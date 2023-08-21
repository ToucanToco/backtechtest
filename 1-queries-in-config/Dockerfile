FROM mongo

RUN echo '[{"domain": "test_domain", "my_key": 1234 }, {"domain": "test_domain", "my_key": 5678}]' > init.json

RUN echo 'mongod &' > run.sh
RUN echo 'sleep 2' >> run.sh
RUN echo 'mongoimport --db mytest --collection mycoll --file init.json --jsonArray' >> run.sh
RUN echo 'sleep 986400' >> run.sh
RUN chmod +x run.sh

CMD ["/run.sh"]
