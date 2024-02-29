# opBNB_bridge

main.py进行运行，
- deposit() 为多账号从BNB提款到opBNB，accounts.txt需要填入提款钱包的私钥
- transfer() 为一对多转账，从BNB提款到多个opBNB，accounts.txt需要填入转账的钱包地址，config.py的transfer_private_key填入转出钱包的私钥。

config.py的value为每次操作金额。