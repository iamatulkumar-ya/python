import language_tool_python


# setting language

tool = language_tool_python.LanguageTool('en-US')


class ValidateGrammer:

    def checkGrammar(self, text):
        # matches is a list
        matches = tool.check(text)
        if (len(matches) > 0): 
            suggestedText = tool.correct(text)
            return self.formatOutput(matches, suggestedText) # returning list here
         
        else: 
            return(["No Matches Found!"])
        
        tool.close()


    def formatOutput(self, macthesList, suggestedText):

        matchList = [] 
        for i in range(len(macthesList)):
            matchDict = {}
            matchDict["ruleId"] = macthesList[i].ruleId
            matchDict["message"] = macthesList[i].message
            matchDict["replacements"] = macthesList[i].replacements
            matchDict["offsetInContext"] = macthesList[i].offsetInContext
            matchDict["context"] = macthesList[i].context
            matchDict["offset"] = macthesList[i].offset
            matchDict["errorLength"] = macthesList[i].errorLength
            matchDict["category"] = macthesList[i].category
            matchDict["ruleIssueType"] = macthesList[i].ruleIssueType
            matchDict["sentence"] = macthesList[i].sentence

            matchDict["suggestedText"] = suggestedText

            matchList.append(matchDict)
        
        return matchList
