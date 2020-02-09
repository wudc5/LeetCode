class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = list()
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    for r in range(1, 4):
                        if i + j + k + r == len(s):
                            num1 = int(s[0:i])
                            num2 = int(s[i:i + j])
                            num3 = int(s[i + j:i + j + k])
                            num4 = int(s[i + j + k:])
                            if num1 <= 255 and num2 <= 255 and num3 <= 255 and num4 <= 255:
                                tmp = "{0}.{1}.{2}.{3}".format(str(num1), str(num2), str(num3), str(num4))
                                if len(tmp) == len(s) + 3:
                                    result.append("{0}.{1}.{2}.{3}".format(num1, num2, num3, num4))
        return result

