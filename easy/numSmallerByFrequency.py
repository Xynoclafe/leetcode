class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(s):
            fs = sorted(s)
            count = 1
            for i in range(1, len(s)):
                if fs[i - 1] != fs[i]:
                    break
                else:
                    count += 1
                    
            return count
        
        answer = [0 for _ in range(len(queries))]
        
        counts = []
        
        for word in words:
            counts.append(f(word))
            
        counts.sort(reverse = True)
        
        
        for i in range(len(queries)):
            count = 0
            fQuery = f(queries[i])
            for wordCount in counts:
                if fQuery < wordCount:
                    count += 1
                else:
                    break
                    
            answer[i] = count
        
        return answer