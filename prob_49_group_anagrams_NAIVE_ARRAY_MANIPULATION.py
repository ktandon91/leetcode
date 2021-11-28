class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited = [0]*len(strs)
        group = 1
        
        def get_dictionary_of_characters(s):
            d = {}
            for c in s:
                if c in d:
                    d[c]+=1
                else:
                    d[c]=1
            return d
        
        for s in range(len(strs)): ##########  n --- times
            if visited[s] != 0: 
                continue
            characters_s = get_dictionary_of_characters(strs[s])
            for s1 in range(s, len(strs)): ####### n --- times
                if visited[s1] != 0:
                    continue
                if (len(strs[s]) == len(strs[s1])): 
                    characters_s1 = get_dictionary_of_characters(strs[s1])
                    if characters_s == characters_s1:
                        visited[s1] = group
            visited[s] = group
            group+=1

        result = []
        
        for i in range(group-1):
            result.append([])
        
        for i in range(len(visited)):
            print(f"i = {i}, visited[i] - 1= {visited[i]-1}, strs[i]= {strs[i]}")
            result[visited[i]-1].append(strs[i])
            print(result)
        
        return result
