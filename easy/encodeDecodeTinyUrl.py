import hashlib
from collections import defaultdict
class Codec:
    
    def __init__(self):
        self.lookup = defaultdict(lambda: "")

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash_object = hashlib.sha1(longUrl.encode('utf-8'))
        hex_dig = hash_object.hexdigest()
        self.lookup[hex_dig] = longUrl
        return "https://tinyurl.com/" + hex_dig
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl[-40:]
        return self.lookup[key]
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))