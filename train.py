print("Ceci est un cours sur Git")

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)
b'witch which has which witches wrist watch'
zlib.crc32(s)