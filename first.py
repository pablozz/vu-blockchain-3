from bitcoin.rpc import RawProxy
import sys

p = RawProxy()

tx_id = sys.argv[1]
raw_tx = p.getrawtransaction(tx_id)
json_tx = p.decoderawtransaction(raw_tx)

output_val = 0

for output in json_tx['vout']:
    output_val += output['value']

input_val = 0

for input in json_tx['vin']:
    raw_tx = p.getrawtransaction(input['txid'])
    json_tx = p.decoderawtransaction(raw_tx)

    for tx in json_tx['vout']:
        if tx['n'] == input['vout']:
            tx_input_val = tx

    input_val += tx_input_val['value']

print("Transaction Fee: " + str(input_val - output_val))
