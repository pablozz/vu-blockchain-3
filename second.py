from bitcoin.rpc import RawProxy
import sys
import getopt
import hashlib

# Function for converting from big-endian to little-endian


def endianConversion(input1):
    ba = bytearray.fromhex(input1)
    ba.reverse()
    result = ''.join(format(x, '02x') for x in ba)
    return result


p = RawProxy()

# Write down basic block informaction
blockID = str(sys.argv[1])

try:
    blockHeader = p.getblockheader(blockID)
    # Gets the full header information in hex format
    fullHeader = (endianConversion(blockHeader['versionHex']) + endianConversion(blockHeader['previousblockhash'])
                  + endianConversion(blockHeader['merkleroot']) +
                  endianConversion('{:02x}'.format(blockHeader['time']))
                  + endianConversion(blockHeader['bits']) + endianConversion('{:02x}'.format(blockHeader['nonce'])))

    binHeader = fullHeader.decode('hex')

    # Calculates the hash based on the header information
    calculatedHash = hashlib.sha256(
        hashlib.sha256(binHeader).digest()).digest()

    if calculatedHash[::-1].encode('hex_codec') == blockHeader['hash']:
        print("Block hash is correct")
    else:
        print("Block hash is incorrect")
except:
    print("Block hash is incorrect")
