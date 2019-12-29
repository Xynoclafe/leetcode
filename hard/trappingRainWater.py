class Solution:
    def calc(self, height, fp, sp):
        vol = 0
        nfp = fp
        lim = min(height[nfp], height[sp])
        nfp += 1
        while(nfp < sp):
            sum = lim - height[nfp]
            if(sum > 0):
                vol += sum
            nfp += 1
        return vol
            
    def trap(self, height: List[int]) -> int:
        if(len(height) in [0,1,2]):
            return 0
        sp = 1
        ascent = False
        descent = False
        peak = [0]
        for i in range(1, len(height)):
            sp = i
            if(height[sp - 1] <= height[sp]):
                if(ascent or descent):
                    ascent = True
                    descent = False
                else:
                    peak = [sp]
            elif(height[sp - 1] > height[sp]):
                descent = True
                if(ascent):
                    ascent = False
                    peak.append(sp-1)
        if(ascent):
            peak.append(sp)
        print(peak)
        vol = 0
        change = False
        while(True):
            i = 1
            while i in range(1, len(peak) - 1):
                if(height[peak[i]] <= height[peak[i + 1]] and height[peak[i]] <= height[peak[i - 1]]):
                    peak.pop(i)
                    change = True
                else:
                    i += 1
            if(change == False):
                break
            change = False
        print("final", peak)
        for i in range(len(peak) - 1):
            vol += self.calc(height, peak[i], peak[i+1])
        return vol
