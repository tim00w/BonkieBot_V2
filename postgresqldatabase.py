import dataset
import sqlalchemy
# from sqlalchemy.dialects import postgresql
# TODO: replace sqlalchemy standard variable definition with postgresql compatible definitions

# CONSTANTS

ACCOUNTS = dict(SYSADMIN = 50,
                ADMIN = 30,
                TRAINER = 20,
                GEBRUIKER = 10)

TRAINING_TABLE_NAME = 'training'
GEBRUIKERS_TABLE_NAME = 'gebruikers'
FITNESS_TABLE_NAME = 'fitness'
SCHEMA_TABLE_NAME = 'schema'

GEBRUIKER_ID = 'gebruiker_id'
TRAINING_ID = 'training_id'
OEFENING_ID = 'oefening_id'
DATUM = 'datum'
TIJD = 'tijd'
DATUMTIJD = 'datumtijd'
TIJDZONE = 'tijdzone'
OEFENING_NAAM = 'oefening_naam'
OEFENING_TEMPO = 'oefening_tempo'
OEFENING_REPS = 'oefening_reps'
OEFENING_GEWICHT = 'oefening_gewicht'
GEWICHT_EENHEID = 'gewicht_eenheid'
OPMERKING = 'opmerking'
TELEGRAM_CODE = 'telegram_code'
VOORNAAM = 'voornaam'
ACHTERNAAM = 'achternaam'
TUSSENVOEGSEL = 'tussenvoegsel'
GEBOORTEDATUM = 'geboortedatum'
GESLACHT = 'geslacht'
FITNESS_ID = 'fitness_id'
FITNESS_WAARDE = 'fitness_waarde'
SCHEMA_ID = 'schema_id'
SCHEMA_NAAM = 'schema_naam'
SCHEMA_WAARDE = 'schema_waarde'
ACCOUNT = 'account'

# FUNCTIONS  # TODO: create functions to handle database access

# CREATE DATABASE  #TODO: make it possible to import database creation from other file (function? class?)

# dialect+driver://username:password@host:port/database

dialect = 'postgresql'
driver = 'pg8000'
username = 'sysadmin'
password = 'flipper'
host = 'localhost'
port = '5432'
database = 'kenamju'
baseStr = "{}+{}://{}:{}@{}:{}/{}"
engineStr = baseStr.format(dialect, driver, username, password, host, port, database)

if __name__ is '__main__':
    db = dataset.connect(engineStr)

    # CREATE TABLES  # TODO: create logs/ errors tables

    db.create_table(TRAINING_TABLE_NAME, primary_id='id', primary_type='Integer')
    db.create_table(GEBRUIKERS_TABLE_NAME, primary_id='id', primary_type='Integer')
    db.create_table(FITNESS_TABLE_NAME, primary_id='id', primary_type='Integer')
    db.create_table(SCHEMA_TABLE_NAME, primary_id='id', primary_type='Integer')

    training = db[TRAINING_TABLE_NAME]
    gebruikers = db[GEBRUIKERS_TABLE_NAME]
    fitness = db[FITNESS_TABLE_NAME]
    schema = db[SCHEMA_TABLE_NAME]

    # CREATE COLUMNS FOR EACH TABLE

    training.create_column(GEBRUIKER_ID, sqlalchemy.String)
    training.create_column(TRAINING_ID, sqlalchemy.String)
    training.create_column(SCHEMA_ID, sqlalchemy.String)
    training.create_column(OEFENING_ID, sqlalchemy.String)
    training.create_column(DATUMTIJD, sqlalchemy.DateTime)
    training.create_column(TIJDZONE, sqlalchemy.String)
    training.create_column(OEFENING_NAAM, sqlalchemy.String)
    training.create_column(OEFENING_TEMPO, sqlalchemy.String)
    training.create_column(OEFENING_REPS, sqlalchemy.INT)
    training.create_column(OEFENING_GEWICHT, sqlalchemy.FLOAT)
    training.create_column(GEWICHT_EENHEID, sqlalchemy.String)
    training.create_column(OPMERKING, sqlalchemy.String)

    gebruikers.create_column(GEBRUIKER_ID, sqlalchemy.String)
    gebruikers.create_column(TELEGRAM_CODE, sqlalchemy.String)
    gebruikers.create_column(VOORNAAM, sqlalchemy.String)
    gebruikers.create_column(ACHTERNAAM, sqlalchemy.String)
    gebruikers.create_column(TUSSENVOEGSEL, sqlalchemy.String)
    gebruikers.create_column(DATUMTIJD, sqlalchemy.DateTime)
    gebruikers.create_column(GEBOORTEDATUM, sqlalchemy.DateTime)
    gebruikers.create_column(GESLACHT, sqlalchemy.String)
    gebruikers.create_column(TIJDZONE, sqlalchemy.String)
    gebruikers.create_column(GEWICHT_EENHEID, sqlalchemy.String)
    gebruikers.create_column(ACCOUNT, sqlalchemy.String)  # standard is GEBRUIKER, only SYSADMIN can change
    # TODO: add column for current weight (and update whenever 'weight' is entered in fitness table!)
    # TODO: add column for current length
    # TODO: add column for length units (metric units or different)

    fitness.create_column(GEBRUIKER_ID, sqlalchemy.String)
    fitness.create_column(DATUMTIJD, sqlalchemy.DateTime)  # if i'm correct, this works with datetime.datetime
    fitness.create_column(FITNESS_ID, sqlalchemy.String)
    fitness.create_column(FITNESS_WAARDE, sqlalchemy.String)  # no (or large) limit on string length

    schema.create_column(GEBRUIKER_ID, sqlalchemy.String)
    schema.create_column(DATUMTIJD, sqlalchemy.DateTime)
    schema.create_column(SCHEMA_NAAM, sqlalchemy.String)
    schema.create_column(SCHEMA_ID, sqlalchemy.String)
    schema.create_column(SCHEMA_WAARDE, sqlalchemy.String)
