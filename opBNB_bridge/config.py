import os
import random

PAUSA_MAX = 30
PAUSA_MIN = 10

ABIS_DIR = 'opBNB_bridge/abis'

TOKEN_ABI = os.path.join(ABIS_DIR, 'token.json')
BRIDGE_ABI = os.path.join(ABIS_DIR, 'bridge.json')

# 转账金额
value = random.uniform(0.0005, 0.0015)

# 转账的主账号私钥
transfer_private_key = ''