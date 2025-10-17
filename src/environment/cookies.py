import os
from dotenv import load_dotenv


def load_cookies():
    load_dotenv(override=True)

    cookies = {
        "_tt_enable_cookie": os.getenv("TT_ENABLE_COOKIE"),
        "_ttp": os.getenv("TTP"),
        "hubspotutk": os.getenv("HUBSPOTUTK"),
        "_gcl_au": os.getenv("GCL_AU"),
        "_gid": os.getenv("GID"),
        "IR_gbd": os.getenv("IR_GBD"),
        "__hstc": os.getenv("HSTC"),
        "__hssrc": os.getenv("HSSRC"),
        "_ga": os.getenv("GA"),
        "_gat_UA-45526809-2": os.getenv("GAT_UA"),
        "_rdt_uuid": os.getenv("RDT_UUID"),
        "utm": os.getenv("UTM"),
        "_ga_25NB9K2WQX": os.getenv("GA_25NB9K2WQX"),
        "ttcsid": os.getenv("TTCSID"),
        "_uetsid": os.getenv("UETSID"),
        "_uetvid": os.getenv("UETVID"),
        "ttcsid_CMT97QBC77U755R2SMR0": os.getenv("TTCSID_CMT"),
        "IR_13993": os.getenv("IR_13993"),
        "IR_PI": os.getenv("IR_PI"),
        "__hssc": os.getenv("HSSC"),
        "ph_phc_hOfahdCMQ36jsPdmc5pZLYWmqmcNOgcGAFa5RgoTvBR_posthog": os.getenv("POSTHOG")
    }

    return cookies
