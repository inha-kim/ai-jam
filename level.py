import json

class Level:
    def __init__(self, identity, barriers, conditions, introPrompt, questionPrompt):
        self.identity = identity
        self.barriers = barriers
        self.conditions = conditions
        self.introPrompt = introPrompt
        self.questionPrompt = questionPrompt

def loadLevel(level):
    filename = "level" + str(level) + ".json"
    with open(filename) as levelJson:
        j = json.load(levelJson)
        retVal = Level(j["identity"], j["barriers"], j["conditions"], j["introPrompt"], j["questionPrompt"])
        return retVal
