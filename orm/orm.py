from sqlalchemy import Date, ForeignKey

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:faraparola22@localhost:1234/cms', echo=True)
Session = sessionmaker(bind=engine)


def get_session_maker():
    return Session


Base = declarative_base()


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    loginName = Column(String)
    password = Column(String)
    email = Column(String)
    affiliation = Column(String)
    webpage = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    phone = Column(String)

    def __init__(self, loginName, password, email, affiliation, webpage, firstName, lastName, phone):
        self.loginName = loginName
        self.password = password
        self.email = email
        self.affiliation = affiliation
        self.webpage = webpage
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone

class PC(Base):
    __tablename__ = 'PC'

    id = Column(Integer, primary_key=True)
    loginName = Column(String)
    password = Column(String)
    email = Column(String)
    affiliation = Column(String)
    webpage = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    phone = Column(String)

    def __init__(self, loginName, password, email, affiliation, webpage, firstName, lastName, phone):
        self.loginName = loginName
        self.password = password
        self.email = email
        self.affiliation = affiliation
        self.webpage = webpage
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone

class Listeners(Base):
    __tablename__ = 'Listeners'

    id = Column(Integer, primary_key=True)
    loginName = Column(String)
    password = Column(String)
    email = Column(String)
    affiliation = Column(String)
    webpage = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    phone = Column(String)

    def __init__(self, loginName, password, email, affiliation, webpage, firstName, lastName, phone):
        self.loginName = loginName
        self.password = password
        self.email = email
        self.affiliation = affiliation
        self.webpage = webpage
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone

class Conferences(Base):
    __tablename__ = 'Conferences'

    id = Column(Integer, primary_key=True)
    conferenceName = Column(String)
    startingDate = Column(String)
    endingDate = Column(String)
    abstractDeadline = Column(String)
    proposalDeadline = Column(String)
    biddingDeadline = Column(String)
    description = Column(String)
    chair = Column(Integer, ForeignKey("PC.id"))

    def __init__(self, conferenceName, startingDate, endingDate, abstractDeadline, proposalDeadline, biddingDeadline, description, chair):
        self.conferenceName = conferenceName
        self.startingDate = startingDate
        self.endingDate = endingDate
        self.abstractDeadline = abstractDeadline
        self.proposalDeadline = proposalDeadline
        self.biddingDeadline = biddingDeadline
        self.description = description
        self.chair = chair

class ConferencesPC(Base):
    __tablename__ = 'ConferencesPC'

    id = Column(Integer, primary_key=True)
    pcId = Column(Integer, ForeignKey("PC.id"))
    conferenceId = Column(Integer, ForeignKey("Conferences.id"))
    chair = Column(Integer)

    def __init__(self, pcId, conferenceId, chair):
        self.pcId = pcId
        self.conferenceId = conferenceId
        self.chair = chair

class Proposals(Base):
    __tablename__ = 'Proposals'

    id = Column(Integer, primary_key=True)
    proposalName = Column(String)
    proposalTopic = Column(String)
    proposalAbstract = Column(String)
    proposalFull = Column(String)
    authorId = Column(Integer, ForeignKey("Users.id"))
    conferenceId = Column(Integer, ForeignKey("Conferences.id"))

    def __init__(self, proposalName, proposalTopic, proposalAbstract, proposalFull, authorId, conferenceId):
        self.proposalName = proposalName
        self.proposalTopic = proposalTopic
        self.proposalAbstract = proposalAbstract
        self.proposalFull = proposalFull
        self.authorId = authorId
        self.conferenceId = conferenceId

class ProposalsKeywords(Base):
    __tablename__ = 'ProposalsKeywords'

    id = Column(Integer, primary_key=True)
    keyword = Column(String)
    proposalId = Column(Integer, ForeignKey("Proposals.id"))

    def __init__(self, keyword, proposalId):
        self.keyword = keyword
        self.proposalId = proposalId


class ProposalsAuthors(Base):
    __tablename__ = 'ProposalsAuthors'

    id = Column(Integer, primary_key=True)
    authorName = Column(String)
    proposalId = Column(Integer, ForeignKey("Proposals.id"))

    def __init__(self, authorName, proposalId):
        self.authorName = authorName
        self.proposalId = proposalId

class BiddingResults(Base):
    __tablename__ = 'BiddingResults'

    id = Column(Integer, primary_key=True)
    pcMemberId = Column(Integer, ForeignKey("PC.id"))
    proposalId = Column(Integer, ForeignKey("Proposals.id"))
    result = Column(Integer)

    def __init__(self, pcMemberId, proposalId, result):
        self.pcMemberId = pcMemberId
        self.proposalId = proposalId
        self.result = result

class PaidFees(Base):
    __tablename__ = 'PaidFees'

    id = Column(Integer, primary_key=True)
    listenerId = Column(Integer, ForeignKey("Listeners.id"))
    conferenceId = Column(Integer, ForeignKey("Conferences.id"))

    def __init__(self, listenerId, conferenceId):
        self.listenerId = listenerId
        self.conferenceId = conferenceId

class ProposalsPc(Base):
    __tablename__ = 'ProposalsPc'
    id = Column(Integer, primary_key=True)
    pcMemberId = Column(Integer, ForeignKey("PC.id"))
    proposalId = Column(Integer, ForeignKey("Proposals.id"))

    def __init__(self, pcMemberId, proposalId):
        self.pcMemberId = pcMemberId
        self.proposalId = proposalId

class ReviewResult(Base):
    __tablename__ = "ReviewResult"
    id = Column(Integer, primary_key=True)
    proposalId = Column(Integer, ForeignKey("Proposals.id"))
    pcId = Column(Integer, ForeignKey("PC.id"))
    result = Column(Integer)
    recommandation = Column(String)

    def __init__(self, proposalId, pcId, result, recommandation):
        self.proposalId = proposalId
        self.pcId = pcId
        self.result = result
        self.recommandation = recommandation

class Sections(Base):
    __tablename__ = "Sections"
    id = Column(Integer, primary_key=True)
    proposalId = Column(Integer, ForeignKey("Proposals.id"))

    def __init__(self, proposalId):
        self.proposalId = proposalId