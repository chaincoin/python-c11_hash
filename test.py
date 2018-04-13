import c11_hash
from binascii import unhexlify, hexlify

import unittest

# chaincoin block #1
# noo@b1:~/.chaincoin$ chaincoin-cli getblockhash 1
# 00000012f1c40ff12a9e6b0e9076fe4fa7ad27012e256a5ad7bcb80dc02c0409
# noo@b1:~/.chaincoin$ chaincoin-cli getblockheader 00000012f1c40ff12a9e6b0e9076fe4fa7ad27012e256a5ad7bcb80dc02c0409
#{
#  "hash": "00000012f1c40ff12a9e6b0e9076fe4fa7ad27012e256a5ad7bcb80dc02c0409",
#  "confirmations": 1451145,
#  "height": 1,
#  "version": 2,
#  "versionHex": "00000002",
#  "merkleroot": "aa2b2e9e7e1056211f51f12b5a6cfe5db99309b7e0eb6208316f366ae93d2879",
#  "time": 1390102807,
#  "mediantime": 1390102807,
#  "nonce": 133097,
#  "bits": "1e0fffff",
#  "difficulty": 0.0002441371325370145,
#  "chainwork": "0000000000000000000000000000000000000000000000000000000000200002",
#  "previousblockhash": "00000f639db5734b2b861ef8dbccc33aebd7de44d13de000a12d093bcc866c64",
#  "nextblockhash": "00000ace4e8ce1056cc5fafcd047f5de8bf4ee9e8cc579480bb4e672b6fdd9df"
#}

header_hex = ("02000000"+
    "646c86cc3b092da100e03dd144ded7eb3ac3ccdbf81e862b4b73b59d630f0000" +
    "79283de96a366f310862ebe0b70993b95dfe6c5a2bf1511f2156107e9e2e2baa" +
    "1749db52" +
    "ffff0f1e" +
    "e9070200")

best_hash = '09042cc00db8bcd75a6a252e0127ada74ffe76900e6b9e2af10fc4f112000000'

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_c11_hash(self):
        self.pow_hash = hexlify(c11_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash, self.best_hash)


if __name__ == '__main__':
    unittest.main()

