class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cacheMap = {}
        self.keyList = []
        self.maxLen = capacity;

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value = self.cacheMap.get(key)
        if value != None and self.keyList[0] != key:
            index = self.keyList.index(key)
            self.keyList.pop(index)
            self.keyList.insert(0, key)
        value = value if value != None else -1
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.cacheMap.get(key) != None:
            index = self.keyList.index(key)
            self.cacheMap.pop(key)
            self.keyList.pop(index)

        if len(self.keyList) >= self.maxLen:
            num = self.keyList.pop(self.maxLen - 1)
            self.cacheMap.pop(num)
        self.cacheMap[key] = value
        self.keyList.insert(0, key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
