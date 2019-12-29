class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        if len(logs) == 0:
            return logs
        logStrings = []
        logNos = []
        outString = []
        for log in logs:
            idStr = log.split(" ", 1)
            if(idStr[1][0] in ["0","1","2","3","4","5","6","7","8","9"]):
                logNos.append(log)
            else:
                logStrings.append([idStr[1], idStr[0]])
        logStrings.sort()
        for i in range(len(logStrings)):
            outString.append(logStrings[i][1] + " " + logStrings[i][0])
        for i in range(len(logNos)):
            outString.append(logNos[i])
        return(outString)
