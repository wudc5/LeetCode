#codint=utf-8
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        result = ['0'] * (len1 + len2)
        for i in range(len2 - 1, -1, -1):
            for j in range(len1 - 1, -1, -1):
                tmp = int(num2[i]) * int(num1[j]) + int(result[i+j+1])
                result[i+j+1] = str(tmp % 10)
                result[i+j] = str(int(result[i+j]) + tmp / 10)
        for i in range(len1 + len2):
            if result[i] != '0':
                return "".join(result[i:])
        return '0'


