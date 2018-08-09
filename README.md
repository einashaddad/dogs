To install:

`pip install -r requirements.txt`

`psql -c 'create database adoptadog' postgres`

`alembic upgrade head`

To run tests:

`python -m unittest`

Development plan:

* Add a column in DB whether or not seen
* Add an api to set personal preferances on age/breed/gender
* Send a weekly digest on all dogs you would potentially like
** only send dogs that use would like and has not seen
** link through our api then forward to the actual dog to know if they've seen
