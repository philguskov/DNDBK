from telegram import *

updater = Updater(token="554767023:AAFSn7jxojOoNeoN8-FfGHwAg2Wz7UmOxF4")
dispatcher = updater.dispatcher

characterList = []
playerIndex = 0
DM = None

attributes = False

class Character(object):
    playerName = None
    characterName = None
    race = None
    _class = None
    inventory = {}
    stats = {'strength': 0, 'dexterity': 0, 'wisdom': 0, "intelligence": 0, "constitution": 0, "charisma": 0, "health": 0}
    def __init__(self, playerName, characterName):
        self.playerName = playerName
        self.characterName = characterName.lower()

    def updateStats(self, race, _class):
        #Race Stats for Human
        if self.race == 'human':
            self.stats['strength'] = 5
            self.stats['dexterity'] = 5
            self.stats['wisdom'] = 5
            self.stats['intelligence'] = 5
            self.stats['constitution'] = 5
            self.stats['charisma'] = 5
            if self.stats ['constitution'] == 5:
                self.stats['health']= 18
        #Race Stats for Dwarf
        elif self.race == 'dwarf':
            self.stats['strength'] = 6
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 3
            self.stats['intelligence'] = 3
            self.stats['constitution'] = 7
            self.stats['charisma'] = 3
            if self.stats ['constitution'] == 7:
                self.stats['health']= 20
        #Race Stats for Elf
        elif self.race == 'elf':
            self.stats['strength'] = 3
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 8
            self.stats['intelligence'] = 7
            self.stats['constitution'] = 3
            self.stats['charisma'] = 6
            if self.stats ['constitution'] ==3:
                self.stats['health']= 16
        #Race Stats for Ogre
        elif self.race == 'ogre':
            self.stats['strength'] = 10
            self.stats['dexterity'] = 3
            self.stats['wisdom'] = 3
            self.stats['intelligence'] = 3
            self.stats['constitution'] = 8
            self.stats['charisma'] = 3
            if self.stats ['constitution'] ==8:
                self.stats['health']= 21
        #Race Stats for Merman
        elif self.race == 'merman':
            self.stats['strength'] = 7
            self.stats['dexterity'] = 5
            self.stats['wisdom'] = 6
            self.stats['intelligence'] = 5
            self.stats['constitution'] = 4
            self.stats['charisma'] = 3
            if self.stats ['constitution'] ==4:
                self.stats['health']= 17
        #Class Stats for Fighter
        if self._class == 'fighter':
            self.stats['strength'] = self.stats['strength'] + 2
            self.stats['dexterity'] = self.stats['dexterity']
            self.stats['wisdom'] = self.stats['wisdom'] - 1
            self.stats['intelligence'] = self.stats['intelligence'] - 2
            self.stats['constitution'] = self.stats['constitution'] + 2
            self.stats['charisma'] = self.stats['charisma'] - 1
            self.stats['gold'] = 50
            self.stats['experience'] = 0

        #Class Stats for Mage
        elif self._class == 'mage':
            self.stats['strength'] = self.stats['strength'] - 2
            self.stats['dexterity'] = self.stats['dexterity']
            self.stats['wisdom'] = self.stats['wisdom'] + 2
            self.stats['intelligence'] = self.stats['intelligence'] + 2
            self.stats['constitution'] = self.stats['constitution'] - 1
            self.stats['charisma'] = self.stats['charisma'] - 1
            self.stats['gold'] = 100
        #Class Stats for Priest
        elif self._class == 'priest':
            self.stats['strength'] = self.stats['strength'] - 2
            self.stats['dexterity'] = self.stats['dexterity']
            self.stats['wisdom'] = self.stats['wisdom'] + 3
            self.stats['intelligence'] = self.stats['intelligence'] + 1
            self.stats['constitution'] = self.stats['constitution'] - 1
            self.stats['charisma'] = self.stats['charisma'] - 1
            self.stats['gold'] = 250
            self.stats['experience'] = 0
        #Class Stats for Thief
        elif self._class == 'thief':
            self.stats['strength'] = self.stats['strength'] - 1
            self.stats['dexterity'] = self.stats['dexterity'] + 2
            self.stats['wisdom'] = self.stats['wisdom'] -2
            self.stats['intelligence'] = self.stats['intelligence']
            self.stats['constitution'] = self.stats['constitution'] -1
            self.stats['charisma'] = self.stats['charisma'] + 2
            self.stats['gold'] = 200
            self.stats['experience'] = 0
        #Class Stats for Ranger
        elif self._class == 'ranger':
            self.stats['strength'] = self.stats['strength'] - 1
            self.stats['dexterity'] = self.stats['dexterity'] + 3
            self.stats['wisdom'] = self.stats['wisdom'] -1
            self.stats['intelligence'] = self.stats['intelligence']
            self.stats['constitution'] = self.stats['constitution'] -2
            self.stats['charisma'] = self.stats['charisma'] + 1
            self.stats['gold'] = 200
            self.stats['experience'] = 0

def start(bot, update):
    #Displays "Welcome to Dungeons and Dragons.")
    bot.sendMessage(chat_id = update.message.chat_id, text = "Welcome to Dungeons and Dragons.")

def setDM(bot, update):
    global DM
    if DM == None:
        DM = update.message.from_user.first_name
        bot.sendMessage(chat_id = update.message.chat_id, text = DM + " has been set as Dungeon Master")
    else:
        bot.sendMessage(chat_id = update.message.chat_id, text = "DM " + DM + " has already been set!")

def createCharacter(bot, update):
    global playerIndex
    if findCharacterIndex(update.message.from_user.first_name) != -1:
        bot.sendMessage(chat_id = update.message.chat_id, text = "@" + update.message.from_user.first_name + " already has a character")
        return None
    characterName = update.message.text[17:].lower()
    playerName = update.message.from_user.first_name
    characterList.append(Character(playerName, characterName))
    #Displays "Character [Character] has been created [Player]"
    bot.sendMessage(chat_id = update.message.chat_id, text = "Character " + characterList[playerIndex].characterName + " has been created by " + characterList[playerIndex].playerName)
    playerIndex += 1
    #Displays "@[Player] Please enter your character's attributes in the format of [Race] [Class]"
    bot.sendMessage(chat_id = update.message.chat_id, text = "@" + playerName + " Please enter your character's Race & Class in the format: [Race] [Class]")
    global attributes
    attributes = True

def incomingMessages(bot, update):
    global attributes
    if attributes == True:
        attributesInput = update.message.text.lower()
        attributesInput = attributesInput.split()
        i = findCharacterIndex(update.message.from_user.first_name)
        characterList[i].race = attributesInput[0]
        characterList[i]._class = attributesInput[1]
        #Display "@[Player] [Character]'s race is [Race] and [Character]'s class is [Class]
        bot.sendMessage(chat_id = update.message.chat_id, text = "@" + characterList[i].playerName + " " + characterList[i].characterName + "'s race is " + characterList[i].race + " and " + characterList[i].characterName + "'s class is "+ characterList[i]._class + ".")
        characterList[i].updateStats(characterList[i].race, characterList[i]._class)
        statsheet = (str(characterList[i].characterName) + "\n Created by: "
                     + str(characterList[i].playerName)
                    +"\n ----------------------------"
                    + "\n Strength: " + str(characterList[i].stats['strength'])
                    + "\n Dexterity: " + str(characterList[i].stats['dexterity'])
                    + "\n Wisdom: " + str(characterList[i].stats['wisdom'])
                    + "\n Intelligence: " + str(characterList[i].stats['intelligence'])
                    + "\n Constitution: " + str(characterList[i].stats['constitution'])
                    + "\n Charisma: " + str(characterList[i].stats['charisma'])
                    + "\n ----------------------------"
                    + "\n Health: " + str(characterList[i].stats['health'])
                    + "\n Gold: " + str(characterList[i].stats['gold'])
                    + "\n Experience: " + str(characterList[i].stats['experience']))
        bot.sendMessage(chat_id = update.message.chat_id, text = statsheet)
        attributes = False

def printCharacterStats(bot, update):
    # /printcharacterstats CHARACTER_NAME
    userInput = parseInput(update.message.text, 2)
    i = getIndexFromCharacter(userInput[1])
    statsheet = (str(characterList[i].characterName) + "\n Created by: "
        + str(characterList[i].playerName)
        + "\n ----------------------------"
        + "\n Strength: " + str(characterList[i].stats['strength'])
        + "\n Dexterity: " + str(characterList[i].stats['dexterity'])
        + "\n Wisdom: " + str(characterList[i].stats['wisdom'])
        + "\n Intelligence: " + str(characterList[i].stats['intelligence'])
        + "\n Constitution: " + str(characterList[i].stats['constitution'])
        + "\n Charisma: " + str(characterList[i].stats['charisma'])
        + "\n ----------------------------"
        + "\n Health: " + str(characterList[i].stats['health'])
        + "\n Gold: " + str(characterList[i].stats['gold'])
        + "\n Experience: " + str(characterList[i].stats['experience']))
    bot.sendMessage(chat_id = update.message.chat_id, text = statsheet)

def findCharacterIndex(first_name):
    for i in range(len(characterList)):
        if characterList[i].playerName == first_name:
            return i
    return -1

def alterHealth(bot, update):
    #/changehealth charactername value
    user = update.message.from_user.first_name
    if user != DM:
        bot.sendMessage(chat_id = update.message.chat_id, text = "You're not authorised to use this command!")
    else:
        userInput = parseInput(update.message.text, 3)
        i = getIndexFromCharacter(userInput[1])
        value = int(userInput[2])
        characterList[i].stats['health'] += value
        bot.sendMessage(chat_id = update.message.chat_id, text = characterList[i].characterName + "'s health has been changed " + userInput[2] + " to " + str(characterList[i].stats['health']))

def inventoryUpdate(bot, update):
    user = update.message.from_user.first_name
    if user != DM:
        bot.sendMessage(chat_id = update.message.chat_id, text = "You're not authorised to use this command!")
    else:
        inventoryInput = parseInput(update.message.text, 5)
        i = getIndexFromCharacter(inventoryInput[1])
        print (inventoryInput[1] + characterList[i].playerName)
        if inventoryInput[2] == "remove":
            if inventoryInput[3] not in characterList[i].inventory:
                bot.sendMessage(chat_id = update.message.chat_id, text = "@" + characterList[i].playerName + " You don't have %s in your inventory!" % (inventoryInput[3]))
            elif inventoryInput[3] in characterList[i].inventory:
                if int(inventoryInput[4]) > characterList[i].inventory[inventoryInput[3]]:
                    bot.sendMessage(chat_id = update.message.chat_id, text = "@" + characterList[i].playerName + " You don't have enough " + inventoryInput[3] + "!")
                elif int(inventoryInput[4]) == characterList[i].inventory[inventoryInput[3]]:
                    del characterList[i].inventory[inventoryInput[3]]
                elif int(inventoryInput[4]) < characterList[i].inventory[inventoryInput[3]]:
                    characterList[i].inventory[inventoryInput[3]] = characterList[i].inventory[inventoryInput[3]] - int(inventoryInput[4])
        elif inventoryInput[2] == "add":
            if inventoryInput[3] not in characterList[i].inventory:
                characterList[i].inventory[inventoryInput[3]] = int(inventoryInput[4])
            elif inventoryInput[3] in characterList[i].inventory:
                characterList[i].inventory[inventoryInput[3]] = characterList[i].inventory[inventoryInput[3]] + int(inventoryInput[4])
        print (characterList[i].inventory)
        items = characterList[i].inventory.items()
        text = characterList[i].characterName + "'s Inventory \n"
        for item in items:
            text += item[0] + ": " + str(item[1]) + "\n"
        bot.sendMessage(chat_id = update.message.chat_id, text = text)

def printInventory(bot, update):
    inventoryInput = update.message.text
    inventoryInput = inventoryInput.split()
    name = inventoryInput[1]
    i = getIndexFromCharacter(name)
    items = characterList[i].inventory.items()
    text = characterList[i].characterName + "'s Inventory \n"
    for item in items:
        text += item[0] + ": " + str(item[1]) + "\n"
    bot.sendMessage(chat_id = update.message.chat_id, text = text)

def alterGold(bot, update):
    #/changehealth charactername value
    user = update.message.from_user.first_name
    if user != DM:
        bot.sendMessage(chat_id = update.message.chat_id, text = "You're not authorised to use this command!")
    else:
        userInput = parseInput(update.message.text, 3)
        characterName = userInput[1]
        value = int(userInput[2])
        i = getIndexFromCharacter(characterName)
        characterList[i].stats['gold'] += value
        bot.sendMessage(chat_id = update.message.chat_id, text = characterList[i].characterName + "'s gold has been changed by" + userInput[2] + " to " + str(characterList[i].stats['gold']))

def alterExperience(bot, update):
    #/changeXP characterName value
    user = update.message.from_user.first_name
    if user != DM:
        bot.sendMessage(chat_id = update.message.chat_id, text = "You're not authorised to use this command!")
    else:
        userInput = parseInput(update.message.text, 3)
        characterName = userInput[1]
        value = int(userInput[2])
        i = getIndexFromCharacter(characterName)
        characterList[i].stats['experience'] += value
        bot.sendMessage(chat_id = update.message.chat_id, text = characterList[i].characterName + "'s XP has been changed by" + userInput[2] + " to " + str(characterList[i].stats['experience']))

def parseInput(words, no):
    words = words.split()
    a = len(words) - no
    oup = words[1]
    for i in range(2, 2 + a):
        oup += words[i]
    outt = []
    outt.append(words[0].lower())
    outt.append(oup.lower())
    for i in range(2, no):
        outt.append(words[a + i].lower())
    return outt

def getIndexFromCharacter(name):
    for i in range(len(characterList)):
        if characterList[i].characterName == name:
            return i

dispatcher.addTelegramMessageHandler(incomingMessages)
dispatcher.addTelegramCommandHandler('start', start)
dispatcher.addTelegramCommandHandler('setdm', setDM)
dispatcher.addTelegramCommandHandler('changehealth', alterHealth)
dispatcher.addTelegramCommandHandler('createcharacter', createCharacter)
dispatcher.addTelegramCommandHandler('printcharacterstats', printCharacterStats)
dispatcher.addTelegramCommandHandler('updateinventory', inventoryUpdate)
dispatcher.addTelegramCommandHandler('printinventory', printInventory)
dispatcher.addTelegramCommandHandler('changegold',alterGold)
dispatcher.addTelegramCommandHandler('changexp',alterExperience)

updater.start_polling()
