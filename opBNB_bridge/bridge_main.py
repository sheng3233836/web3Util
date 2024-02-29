import random
from utils import accounts, sleeping
from loguru import logger
from config import value,transfer_private_key
from models import BSC
from client import Client
from opBNB_bridge import Bridge
from web3.middleware import geth_poa_middleware

def deposit():
    max_acconts = len(accounts)
    i = 0
    for account in accounts:
        logger.info(f'deposit: {i+1}/{max_acconts}')
        client = Client(private_key=account, network=BSC)
        client.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
        bridge_instance = Bridge(client=client)
        bridge_instance.bridge_to_opBNB(value=value)
        i += 1
        sleeping()
        
def transfer():
    max_acconts = len(accounts)
    client = Client(private_key=transfer_private_key, network=BSC)
    client.w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    i = 0
    for account in accounts:
        logger.info(f'transfer: {i+1}/{max_acconts}')
        bridge_instance = Bridge(client=client)
        bridge_instance.transfer_to_opBNB(address=account, value=value)
        i += 1
        sleeping()
transfer()