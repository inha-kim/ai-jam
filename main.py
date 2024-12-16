from llama_manager import LlamaManager
from level import Level, loadLevel

def constructConditionCheck(prompt, level, difficulty):
    conditionCheck = "Does the following prompt: \"" + prompt + "\" satisfy the following conditions? "
    for i in range(0, difficulty + 1):
        conditionCheck += str(i) + ". " + level.conditions[i]
    conditionCheck += " The response I'm looking for is a binary string where 1 represents true and 0 represents false in respective order of the conditions. Give the answer only as the binary string and nothing else."
    return conditionCheck

llama = LlamaManager()

# load the first level
currLevel = 1
difficulty = 0
level = loadLevel(currLevel)
print(level.introPrompt)

questionStart = "Now answer this question:"

newLevel = True
newDifficulty = True
conditionsFulfilled = [ False ]
inputStr = ""

while (inputStr != "q"):
    # get user input
    inputStr = input(level.questionPrompt + " ")

    # construct query prefix
    queryPrefix = level.identity
    for i in range(0, difficulty):
        if (not conditionsFulfilled[i + 1]):
            queryPrefix += " " + level.barriers[i]
    
    # get llama response
    queryStr = queryPrefix + " " + questionStart + " " + inputStr
    llmResponse = llama.query(queryStr)
    print(llmResponse)

    # check if response matches any conditions
    conditionCheck = constructConditionCheck(llmResponse, level, difficulty)
    conditionResponse = llama.query(conditionCheck)
    for i in range(0, difficulty + 1):
        if (conditionResponse[i] == '1'):
            conditionsFulfilled[i] = True
    
    
    # check if the user won
    if (conditionsFulfilled[0]):
        difficulty += 1
        if (difficulty > len(level.barriers)):
            conditionsFulfilled = [ False ]
            print("Congratulations, you have completed this level!")
            continueStr = input("Would you like to continue? (y/n)")
            if (continueStr == "y"):
                newLevel = True
                difficulty = 0
            else:
                exit()
        else:
            print("Congratulations, you have completed this difficulty!")
            conditionsFulfilled = [ False ]
            for i in range(0, difficulty):
                conditionsFulfilled.append(False)
            newDifficulty = True
