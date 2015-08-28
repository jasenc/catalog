# Import system-specific parameters and functions for interacting with the
# Python interpreter.
import sys

# From SQLAlchemy import the necessary classes to build our DB.
from sqlalchemy import Column, ForeignKey, Integer, String

# In order to use our ForeignKey we'll have to create relationships.
from sqlalchemy.orm import relationship

# Import the declarative_base to use for class input.
from sqlalchemy.ext.declarative import declarative_base

# Import create_engine so we can communicate with the database.
from sqlalchemy import create_engine

# Import our database variable.
from config import database

# First lets create a local class of declarative_base, this will be used to
# create our tables and indicate to SQLAlchemy that our Tables are in fact
# SQLAlchemy classes.
Base = declarative_base()


# We'll create our first Table, which will be for Users since it will be our
# only table that doesn't have a ForeignKey relationahip, and we will
# instantiate it from the Base class.
class Users(Base):
    # Then we'll start creating our columns, known as mappers.
    # Note: Creating a SERIAL ID in SQLAlchemy is done by creating an integer
    # column and assigning it as the primary_key.
    __tablename__ = 'users'
    # Then we'll start creating our columns.
    # Note: Creating a SERIAL ID in SQLAlchemy is done by creating an integer
    # column and assigning it as the primary_key.
    id = Column(Integer, primary_key=True)
    # The following columns we will want to ensure are included for each entry,
    # we can do this by telling SQLAlchemy that these entries cannot be null.
    # Note: String columns can be set with a maximum value by providing an
    # argument to the String object.
    name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    # However some people might not have a picture, and URLs can get long.
    picture = Column(String(250))


# Next we'll create the Categories class and table
class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    image = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)
    items = relationship("Items", cascade="all, delete-orphan",
                         backref="parent")

    # For this table we will want to provide serialized data for APIs. We can
    # do this by using the property decorator.
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'description': self.description
        }


# Finally we'll create the Items class and table
class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    image = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)
    category_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories, single_parent="true")

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'description': self.description
        }

# With our tables properly set up it's time to connect to the database.
# Create an instance of the create_engine and point it to the database we will
# want to use.
engine = create_engine(database)

# Finally we'll send all of our data that we created above to our database.
Base.metadata.create_all(engine)
