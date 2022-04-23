from collections import defaultdict
from random import random

class Codec:
    codeDB, urlDB = defaultdict(), defaultdict()
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890"
    
    def getCodec(self):
        code = "".join(random.choice(self.chars) for i in range(6))
        return "http://tin.ly/" + code
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.urlDB: 
            return self.urlDB(longUrl)
        code = self.getCodec()
        while code in self.codeDB:
            code = self.getCodec()
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code
            

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.codeDB[shortUrl]