class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        frequency = [0]*26
        result_dict = {}
        result = []
        for i in strs:
            for j in i:
                frequency[ord(j)-97] +=1
            freq_tuple = tuple(frequency)
            if freq_tuple not in result_dict:
                    result_dict[freq_tuple] = []
            result_dict[freq_tuple].append(i)
            frequency = [0]*26

        for i in result_dict.values():
                result.append(i)
        
        return result