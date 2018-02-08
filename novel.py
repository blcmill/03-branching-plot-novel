#!/usr/bin/python3
#Blake Miller
#Branching plot novel
#Fulfills the requirement for ILS-Z399 Game Programming Branching Plot Novel
#This game's goal is to study...or not!
import sys

assert sys.version_info >= (3,4), 'This script requires at least Python 3.4'
#My data structure goes like this:
# world
#   area
#       Area descriptions
#       Displayed Options
#           Option 1
#           Option 2
#           Option 3
#       Results
#           Result 1
#           Result 2
#           Result 3
#   The game will keep track of how long it takes the player to study.

world = {
    "sitting":{"description":"You are standing at a desk.",
             "options":["Open Laptop", 
                        "Open Notebook",
                        "Sit there"],
             "results":["laptop", #laptop done
                        "notebook", #notebook done
                        "sitting"] #sitting done
                        }
    ,
    "laptop":{"description":"Your laptop is open.",
              "options":["Open a game",
                         "Open Canvas",
                         "Close laptop"],
              "results":["gaming", #gaming done
                         "canvas", #canvas done
                         "sitting"]} #sitting done
    ,
    "gaming": {"description":"You are playing a game.", 
               "options":["Keep playing the game",
                          "Stop playing the game"],
               "results":["gaming", #gaming done
                          "laptop"]} #laptop done
    , 
    "canvas": {"description":"You are on Canvas.",
               "options":["Check assignments",
                          "Check another website",
                          "Close Canvas"],
               "results":["assignments", #assignments done
                          "website", #website done
                          "laptop"]} #laptop done
    ,
    "assignments": {"description": "You are looking at your assignments.",
                    "options":["Study for your test",
                               "Check another website",
                               "Close Canvas"],
                    "results":["victory", #victory done
                               "website",
                               "laptop"]} #laptop done
    ,
    "victory": {"description": "Congratulations! You won.",
                "options": [], #nothing to do here
                "results": []} #nothing to do here
    ,
    "website": {"description":"You are browsing a website.",
                "options": ["Continue browsing the site",
                            "Go to Canvas",
                            "Close laptop"],
                "results": ["website", #website done
                            "canvas", #canvas done
                            "sitting"], #sitting done
                }
    ,
    "notebook": {"description":"You have your notebook open.",
                 "options":["Doodle",
                            "Study for your exam",
                            "Close your notebook"],
                 "results": ["doodle",  #doodle done
                             "victory", #victory done
                             "sitting"]} #sitting done
    ,
    "doodle": {"description":"You are doodling.",
               "options":["Keep doodling",
                          "Stop doodling",
                          "Close notebook"],
               "results":["doodle", #doodle done
                          "notebook", #notebook done
                          "sitting"]} #sitting done
                
                    
    }

losses = {"quit": "Thanks for playing!", #this is my differentiating factor
          "sitting":"You lose. You fell asleep, unable to commit to studying.",
          "laptop":"You lose. You stared at your screen, but didn't study.",
          "gaming":"You lose. Maybe you won the game, but you lost this one.",
          "canvas":"You lose. The sight of Canvas can be intimidating.",
          "assignments":"You lose. Just one click away, maybe?",
          "victory":"You won, just in time!",
          "website":"You lose. You were too busy browsing to study.",
          "notebook":"You lose. Those lined pages didn't help you study.",
          "doodle":"You lose. Maybe you drew a pretty picture, though."}
global numberSteps
numberSteps = 0

def mainGame(spot):
    global numberSteps
    #initialize variables based on dictionary
    status = world[spot]
    description = status["description"]
    options = status["options"]
    results = status["results"]
    print(description)
    numberSteps += 1
    if numberSteps >= 8:
        print(losses[spot]) #shows a losing message and quits
    elif status == "victory":
        print("You won!")
    elif (len(options) != 0):
        for i in range(len(options)):
            print(str(i+1) , options[i])        
        choice =(int(input("Choose an option. Type 0 to quit.")) - 1)
        if choice == -1:
            print(losses["quit"]) #lose quit is basically not a move
        elif ((choice >= 0) and ( choice < len(results))):
            mainGame(results[choice]) #move to the next thing
        else:
            mainGame(spot) #if they try something else, just repeat



mainGame("sitting")
    
            
        
    
