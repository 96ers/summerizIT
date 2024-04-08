import enum

#Enum for the environment
class Environment(str, enum.Enum):
    DEVELOPMENT: str = "DEV"
    PRODUCTION: str = "PROD"
    STAGING: str = "STAGE"