# Encrypted by Abir Hossain 
#Thank's for the help Abir Hossain vaiya

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))