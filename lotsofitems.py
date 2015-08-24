# Import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Categories, Items

# Connect to database and create session
engine = create_engine('sqlite:///catalogitems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a dummy user.
user1 = Users(name="Bob Smith", email="bob.smith@bobsmith.com")
session.add(user1)
session.commit()

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

# Movie Category
category2 = Categories(user_id=1, name="Movies", image="https://upload.wikimedia.org/wikipedia/en/1/13/Drive2011Poster.jpg", description="They are movies...!")
session.add(category2)
session.commit()

item6 = Items(user_id=1, category_id=2, name="Drive", image="https://upload.wikimedia.org/wikipedia/en/1/13/Drive2011Poster.jpg", description="Ryan Gosling stars as a Los Angeles wheelman for hire, \
                     stunt driving for movie productions by day and steering \
                     getaway vehicles for armed heists by night.")
session.add(item6)
session.commit()

item7 = Items(user_id=1, category_id=2, name="Burn After Reading", image="https://upload.wikimedia.org/wikipedia/en/a/ae/Burn_After_Reading.jpg", description="At the headquarters of the Central \
                                 Intelligence Agency in Arlington, Va., \
                                 analyst Osborne Cox arrives for a top-secret \
                                 meeting.")
session.add(item7)
session.commit()

item8 = Items(user_id=1, category_id=2, name="Ex Machina", image="http://t3.gstatic.com/images?q=tbn:ANd9GcQe8L-1PTMlUf-si2Oy6BTd9ZtbWH7BSRSF5k5JGNATxOHzyIdg", description="A programmer at an internet-search giant, wins a \
                         competition to spend a week at the private mountain \
                         estate of the company\'s brilliant and reclusive CEO.")
session.add(item8)
session.commit()

item9 = Items(user_id=1, category_id=2, name="Interstellar", image="http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB", description="With our time on Earth coming to an end, a team of \
                           explorers undertakes the most important mission in \
                           human history; traveling beyond this galaxy to \
                           discover whether mankind has a future among the \
                           stars.")
session.add(item9)
session.commit()

item10 = Items(user_id=1, category_id=2, name="Kingsman", image="http://t3.gstatic.com/images?q=tbn:ANd9GcTn2E6bqcLehK92h215qFnUpCYFqt02Iuwg-N4gVBmixzAXvGf", description="A super-secret spy organization that recruits an \
                       unrefined but promising street kid into the agency\'s \
                       ultra-competitive training program just as a global \
                       threat emerges from a twisted tech genius.")
session.add(item10)
session.commit()
