# Copyright (c) 2018-Present Energyparty Developers
# Distributed under the AGPL 3.0 with the OpenSSL exception, see the
# accompanying file LICENSE or <https://github.com/energyparty/sendtokens/>.

import json, csv, sys, requests
requests.packages.urllib3.disable_warnings()

testNet = True
xURL = 'https://testnet.energywallet.eu/_api/'

with open("wallet.json", "r") as wallet:
     dataJ = json.load(wallet)
     eURL = 'http://'+dataJ["rpcuser"]+':'+dataJ["rpcpassword"]+'@localhost'+':'+str(dataJ["rpcport"])
     testNet = dataJ["testnet"]

if not testNet:
   xURL = 'https://wallet.energywallet.eu/_api/'

def cmd(method, params, url):
    headers = {'content-type': 'application/json'}
    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers, verify=False).json()
    return response['result']

def send(source, destination, asset, quantity):
    getSrc = cmd('validateaddress', [source], eURL)
    getDest = cmd('validateaddress', [destination], eURL)
    assert getSrc['isvalid'] and getSrc['ismine'] and getDest['isvalid'] and quantity!=0 and asset!=''
    rawTx = cmd("proxy_to_counterpartyd", {"method":'create_send',"params":{'source':source,'destination':destination,'asset': asset,'quantity':quantity,'pubkey':getSrc['pubkey'],'allow_unconfirmed_inputs':'true'}}, xURL)
    Tx = cmd('signrawtransaction', [rawTx], eURL)['hex']
    txid = cmd('sendrawtransaction', [Tx], eURL)
    return txid

with open(sys.argv[1], 'r') as readFile:
    readLines = csv.reader(readFile)
    for line in readLines:
        if len(line)!=4: continue
        source, destination, asset, quantity = line
        try:
             txid = send(source, destination, asset, int(quantity))
             print('line {} | {} | txid:{}'.format(readLines.line_num, ','.join(line), txid))
        except Exception as e:
             txid = str(e)

