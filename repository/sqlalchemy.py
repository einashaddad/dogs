from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# an Engine, which the Session will use for connection
# resources
db_engine = create_engine('postgresql://localhost/adoptadog')

# create a configured "Session" class
Session = sessionmaker(bind=db_engine)

# create a Session
session = Session()
