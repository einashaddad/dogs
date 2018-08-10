To install:

`pip install -r requirements.txt`

`psql -c 'create database adoptadog' postgres`

`alembic upgrade head`

To run tests:

`python -m unittest`

Development plan:

* Add a users table with column in DB whether or not seen
* Add an api to set personal preferances on age/breed/gender
* Link through our api then forward to the actual dog to know if they've seen
* Mutex lock on two people trying to adopt same dog
* Send weekly digest of dogs you haven't seen
