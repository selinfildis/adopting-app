import datetime
from sqlalchemy import Column, Boolean, Float, Integer, String, ForeignKey
from sqlalchemy.types import Date, DateTime
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String, unique=True)
    created_at: Column(DateTime, default=datetime.datetime.utcnow)
    date_of_birth: Column(DateTime)
    phone_number: Column(String)
    email_address: Column(String)
    address = relationship("Address", backref="address")
    work = relationship("Work", backref="work")

    # form_id
    # int[ref: < form.id]
    # work_info_id
    # int[ref: - work.id]


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="user")
    address_line_1 = Column(String)
    address_line_2 = Column(String)
    postcode = Column(String)
    city = Column(String)
    apartment_type = Column(String)
    area_type = Column(String)


class Work(Base):
    __tablename__ = 'work'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="user")
    working_hours_start = Column(String)  # enforce time on schema
    working_hours_end = Column(String)  # enforce time on schema
    working_days = Column(String)  # determine enforcement
    how_many_hours_away_from_home = Column(Float)
    job_title = Column(String)
    employer = Column(String)


class Form(Base):
    __tablename__ = 'forms'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", back_populates="user")
    created = Column(DateTime, nullable=False)
    animal_type = Column(String)
    meeting_point_preferred = Column(Boolean, nullable=False)
    landlord_agrees = Column(Boolean, nullable=False)
    number_of_people_in_the_house = Column(Integer, nullable=False)
    number_of_children = Column(Integer, nullable=False)
    can_children_care_for_dog = Column(Boolean, nullable=False)
    allergies = Column(String, default=None)
    all_members_want_to_adopt = Column(Boolean, nullable=False)
    previous_dog_care_years = Column(Float)
    where_the_dog_will_be_kept = Column(String)
    possible_contact_with_other_pets = Column(Boolean)
    number_of_walks_per_day = Column(Integer)
    avg_duration_of_single_walk = Column(Integer)  # in mins
    sports_with_dog = Column(Boolean)
    which_sports_with_dog = Column(String)
    expectations_from_pet = Column(String)
    vacation_options = Column(String)
    vet_costs_accepted = Column(Boolean)
    higher_vet_costs = Column(Boolean)
    extra_fees = Column(Boolean)
    in_case_of_unforseen_event = Column(String)
    dog_action_not_allowed = Column(String)
    comments = Column(String)
    gdpr_accepted = Column(String)


class Pet(Base):
    pass


class Organisation(Base):
    pass

class OrganisationUser(User):
    pass
