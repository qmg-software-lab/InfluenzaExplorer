
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime



app = FastAPI()




# flumart api endpoint query
flumart_endpoint_qry_csv = 'https://xmart-api-public.who.int/FLUMART/VIW_FID?$format=csv'

# models
class influenza_infection_count:
    uuid: str
    geolocation: str


    def __init__(self, influenza_infection_count):