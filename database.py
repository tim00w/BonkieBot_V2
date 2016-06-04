import dataset
import sqlalchemy

# CONSTANTS
SYSADMIN = 'sysadmin'
ADMIN = 'admin'
TRAINER = 'trainer'
GEBRUIKER = 'gebruiker'

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

# CREATE DATABASE

dbName = 'TestBonkieBot.db'

db = dataset.connect('sqlite:///{}'.format(dbName))

# CREATE TABLES

db.create_table(TRAINING_TABLE_NAME, primary_id='row_id', primary_type='Integer')
training = db[TRAINING_TABLE_NAME]

db.create_table(GEBRUIKERS_TABLE_NAME, primary_id='row_id', primary_type='Integer')
gebruikers = db['gebruikers']

db.create_table(FITNESS_TABLE_NAME, primary_id='row_id', primary_type='Integer')
fitness = db[FITNESS_TABLE_NAME]

db.create_table(SCHEMA_TABLE_NAME, primary_id='row_id', primary_type='Integer')
schema = db[SCHEMA_TABLE_NAME]

# CREATE COLUMNS FOR EACH TABLE

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
fitness.create_column(FITNESS_WAARDE, sqlalchemy.BLOB)  # no (or large) limit on string length

schema.create_column(GEBRUIKER_ID, sqlalchemy.String)
schema.create_column(DATUMTIJD, sqlalchemy.DateTime)
schema.create_column(SCHEMA_NAAM, sqlalchemy.String)
schema.create_column(SCHEMA_ID, sqlalchemy.String)
schema.create_column(SCHEMA_WAARDE, sqlalchemy.BLOB)