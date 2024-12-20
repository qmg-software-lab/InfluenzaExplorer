# Let's tap into the WHO XMart Data Stream for WHO Data Managers
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

# flumart api endpoint query
qry_xmart_csv_endpoint = 'https://xmart-api-public.who.int/FLUMART/VIW_FID?$format=csv'

app = FastAPI()


# models
class ideal_influenza_infection_count:
    uuid: str
    source_db: str
    strata_1: str
    strata_2: str
    strata_3: str
    geolocation_no: str

class european_flu_srv_count:
    WHOREGION: str 
    FLUSEASON: str 
    HEMISPHERE: str 
    ITZ: str 
    COUNTRY_CODE: str 
    COUNTRY_AREA_TERRITORY: str 
    ISO_WEEKSTARTDATE: str 
    ISO_YEAR: str 
    ISO_WEEK: str 
    MMWR_WEEKSTARTDATE: str 
    MMWR_YEAR: str 
    MMWR_WEEK: str 
    ORIGIN_SOURCE: str 
    AGEGROUP_CODE: str 
    CASE_INFO: str 
    REPORTED_CASES: str 
    OUTPATIENTS: str 
    INPATIENTS: str 
    POP_COV: str 
    INF_TESTED: str 
    INF_POS: str 
    INF_NEG: str 
    INF_A: str 
    INF_B: str 
    INF_MIXED: str 
    AH1: str 
    AH1N12009: str 
    AH3: str 
    AH5: str 
    AH7: str 
    ANOTSUBTYPED: str 
    AOTHERTYPES: str 
    BYAMAGATA: str 
    BVICTORIA: str 
    BNOTDETERMINED: str 
    OTHER: str 
    RSV: str 
    ADENO: str 
    PARAINFLUENZA: str 
    INF_RISK: str 
    GEOSPREAD: str 
    IMPACT: str 
    INTENSITY: str 
    TREND: str 
    GEOSPREAD_COMMENTS: str 
    COMMENTS: str 
    NB_SITES: str 
    MORTALITY_ALL: str 
    MORTALITY_PNI: str 
    ISO2: str 
    ISOYW: str 
    MMWRYW: str


