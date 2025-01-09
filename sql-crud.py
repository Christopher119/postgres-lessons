from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instruction from the "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the Programmer table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

#opens an actual session by calling the Session() subclass defined above
session = Session()

#creating the database using declarative_base subclass
base.metadata.create_all(db)

#creating records on our Programmer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "Female",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "Male",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "Female",
    nationality = "American",
    famous_for = "COBOL language"
)

margaret_hamilton = Programmer(
    first_name = "Margaret",
    last_name = "Hamilton",
    gender = "Female",
    nationality = "American",
    famous_for = "Software Engineering"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "Male",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_less = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "Male",
    nationality = "British",
    famous_for = "World Wide Web"
)

tim_nelson = Programmer(
    first_name = "Tim",
    last_name = "Nelson",
    gender = "Male",
    nationality = "Irish-American",
    famous_for = "Code Institute"
)


#add each instace of our programmers to our session
#session.add(ada_lovelace)
#session.add(alan_turing)
#session.add(grace_hopper)
#session.add(margaret_hamilton)
#session.add(bill_gates)
#session.add(tim_berners_less)
#session.add(tim_nelson)

# commit our session to the database
#session.commit()


# updating a single record
#programmer = session.query(Programmer).filter_by(id=7).first()
#programmer.famous_for = "World President"


# updating multiple records
#people = session.query(Programmer)
#for person in people:
#    if person.gender == "Female":
#        person.gender = "F"
#    elif person.gender == "Male":
#        person.gender = "M"
#    else:
#        print("Gender not defined.")
#    
#    session.commit()


# deleting a single record
#fname = input("Enter a first name: ")
#lname = input("Enter a last name: ")
#programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
#defensive programming
#if programmer is not None:
#    print("Programmer Found: ", programmer.first_name + " " + programmer.last_name)
#    confirmation = input("Are you sure you want to delete this record? (y/n) ")
#    if confirmation.lower() == "y":
#        session.delete(programmer)
#        session.commit()
#        print("Programmer has been deleted.")
#    else:
#        print("Programmer has not been deleted.")
#else:
#    print("Programmer Not Found")


# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )