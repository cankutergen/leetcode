class Solution:
    def decodeString(self, s: str) -> str:
        counts = []
        result = []
        
        res = ""
        index = 0
        while index < len(s):
            if s[index].isdigit():
                count = 0
                while s[index].isdigit():
                    count = 10 * count + int(s[index])
                    index += 1
                counts.append(count)
            elif s[index] == "[":
                result.append(res)
                res = ""
                index += 1
            elif s[index] == "]":
                temp = result.pop()
                times = counts.pop()
                for i in range(times):
                    temp += res
                res = temp
                index += 1
            else:
                res += s[index]
                index += 1
                
        return res
        
