# Import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Categories, Items

# Connect to database and create session
engine = create_engine('sqlite:///catalogitems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Book Category
category1 = Categories(user_id=1, name="Books", image="http://ecx.images-amazon.com/images/I/515gkVfz2XL._SX369_BO1,204,203,200_.jpg", description="They are books...!")
session.add(category1)
session.commit()

item1 = Items(user_id=1, category_id=1, name="Eat More Better", image="http://ecx.images-amazon.com/images/I/515gkVfz2XL._SX369_BO1,204,203,200_.jpg", description="From the creator of The Sporkful you'll learn how to make every bite more delicious.")
session.add(item1)
session.commit()

item2 = Items(user_id=1, category_id=1, name="One More Thing", image="http://ecx.images-amazon.com/images/I/41UHH8%2BxvjL._SX322_BO1,204,203,200_.jpg", description="A star from the office, B.J. Novak, writes a book and it's hilarious.")
session.add(item2)
session.commit()

item3 = Items(user_id=1, category_id=1, name="More Than This", image="http://ecx.images-amazon.com/images/I/61Iu7%2BpTRlL._SX307_BO1,204,203,200_.jpg", description="Patrick Ness writes a book about the afterlife, or is that what he wants you to think?")
session.add(item3)
session.commit()

item4 = Items(user_id=1, category_id=1, name="You Are A Badass", image="http://ecx.images-amazon.com/images/I/41kxQN5Zq7L._SX314_BO1,204,203,200_.jpg", description="Doesn't everybody want to learn how to be a badass?")
session.add(item4)
session.commit()

item5 = Items(user_id=1, category_id=1, name="The Cairo Affair", image="http://ecx.images-amazon.com/images/I/51wjILOG4vL._SX331_BO1,204,203,200_.jpg", description="Spy mystery novel about an affair in Cairo, as you probably gathered by the cover...")
session.add(item5)
session.commit()
