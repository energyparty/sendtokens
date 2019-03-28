# sendtokens integration/staging tree

Copyright (c) 2018-Present Energyparty Developers. All rights reserved.

This is a script for sending Energyparty tokens, written in Python 3.

Tested on Python 3.5

This program is experimental, and some aspects may not work correctly or as expected. Use it at your own risk.

This program is for advanced users only. For non-advanced users, they should send tokens using our official web-wallet instead.


### Instructions and Steps

1. You need a local wallet running and containing an address as payment source, which holds tokens you want to send and sufficient ENRG to pay for transaction fees. You may download [EnergyCoin Core client](https://mega.nz/#F!uc0XmCra!73JBKfnmbdImd_9H_nXtRQ) if necessary.

2. Make sure your EnergyCoin.conf contains the following 6 lines:

   listen=1<br />
   server=1<br />
   daemon=1<br />
   rpcport=YourRpcPort<br />
   rpcuser=YourRpcUserName<br />
   rpcpassword=YourRpcPassword


   YourRpcPort: the default rpcport for EnergyCoin is 32705 for testnet, and 22705 for mainnet.<br />
   YourRpcUserName/YourRpcPassword: your own rpc username and password.

3. To prevent your wallet from staking, you should specify a reservebalance value equal to or larger than your total wallet balance. Run this console command:

   `reservebalance true <value>`

4. You have to fully unlock your wallet if it is encrypted. Run this console command:

   `walletpassphrase <YourPassPhrase> <timeout>`

5. Download this program [here](https://github.com/energyparty/sendtokens/archive/master.zip).

   And then unzip it.

6. Edit the file `wallet.json`.

   The default network is testnet. You shall use testnet coins to get familiar with this script first, before actually using it on mainnet.

   If you want to send mainnet tokens, you should change the testnet parameter to false. Please note that the acceptable json format in this field is either **`true` or `false`**. Anything else such as `"true"`, `"false"`, `True` or `False` (be careful about the extra quotes and capital letter) will not work.

   The parameters rpcport, rpcuser and rpcpassword must match with your own EnergyCoin.conf

7. Create a new text file similar to our `sample.txt`, which contains 4 parameters in the following order separated by comma for each line:

   **source,destination,asset,quantity**

   source: your ENRG address holding coins in the wallet you are running in the step 1.<br />
   destination: ENRG address to receive tokens.<br />
   asset: asset name to send, eg: XEP.<br />
   quantity: amount of asset to send. Only integers are accepted. For example, if you want to send 1 XEP, you have to specify it as 1000000.

8. This script requires importing 4 packages: json, csv, sys, requests

   If you miss any of them in your system, [install](https://docs.python.org/3/installing) first.

9. This script makes use of the API from the energywallet.eu server. Therefore, before running the script, check if the server status is ONLINE [here](https://energywallet.eu)

10. Assuming the text file you created in the step 7 is `send.txt`, run in terminal:<br />
   `python3 sendTokens.py send.txt`


License
-------
This sendtokens program is licensed under the AGPL 3.0 with the OpenSSL exception,
see the accompanying file LICENSE or <https://github.com/energyparty/sendtokens/>.

For other licensing possibilities, contact the main developer: [Peter](https://github.com/coin1hub)


Support Development by Donation: ePvnQvX5RbzDCzt3qSB5TmBz89BJMvpG46
