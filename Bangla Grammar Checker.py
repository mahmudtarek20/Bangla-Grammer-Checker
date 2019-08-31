import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class RuleBased():


    subject = False
    verb = False
    def __init__(self):
        self.aseSentenceList = self.fileOpen("ase")
        self.chaiSentenceList = self.fileOpen("chai")
        self.choriSentenceList = self.fileOpen("chori")
        self.foodSentenceList = self.fileOpen("food")
        self.goriSentenceList = self.fileOpen("gori")
        self.koriSentenceList = self.fileOpen("kori")
        self.paiSentenceList = self.fileOpen("Pai")
        self.pariSentenceList = self.fileOpen("PAri")
        self.placeSentenceList = self.fileOpen("Place")
        self.universalTruthSentenceList = self.fileOpen("universal_truth")
        self.test = self.fileOpen("test")

    def fileOpen(self, str):
        file = open(".\\rule\\"+str+".txt", "rb")
        readFile = (file.read()).decode()
        sentenceList = readFile.split("\r\n")
        sentenceList[0] = sentenceList[0].replace("\ufeff", "")
        return sentenceList

    def startSentence(self, sentence, *person):
            pl = len(person[0])
           # print("subject= %s"%self.subject)
           # print(self.subject)

            if pl == 1:
                if sentence.startswith(person[0][0]):
                    self.subject = True
                    return True
            elif pl == 2:
                if sentence.startswith(person[0][0]) or sentence.startswith(person[0][1]):
                    self.subject = True
                    return True
            elif pl == 3:
                if sentence.startswith(person[0][0]) or sentence.startswith(person[0][1]) or sentence.startswith(person[0][2]):
                    self.subject = True
                    return True
            elif pl == 4:
                if sentence.startswith(person[0][0]) or sentence.startswith(person[0][1]) or sentence.startswith(person[0][2]) or sentence.startswith(person[0][3]):
                    self.subject = True
                    return True
            elif pl == 5:
                if sentence.startswith(person[0][0]) or sentence.startswith(person[0][1]) or sentence.startswith(person[0][2]) or sentence.startswith(person[0][3]) or sentence.startswith(person[0][4]):
                    self.subject = True
                    return True
            return False

    def endSentence(self, sentence, *verb):
            pl = len(verb[0])
           # print(pl)
            if pl == 1:
                if sentence.endswith(verb[0][0]):
                    self.verb = True
                    return True
            elif pl == 2:
                if sentence.endswith(verb[0][0]) or sentence.endswith(verb[0][1]):
                    self.verb = True
                    return True
            elif pl == 3:
                if sentence.endswith(verb[0][0]) or sentence.endswith(verb[0][1]) or sentence.endswith(verb[0][2]):
                    self.verb = True
                    return True
            elif pl == 4:
                if sentence.endswith(verb[0][0]) or sentence.endswith(verb[0][1]) or sentence.endswith(
                        verb[0][2]) or sentence.endswith(verb[0][3]):
                    self.verb = True
                    return True
            elif pl == 5:
                if sentence.endswith(verb[0][0]) or sentence.endswith(verb[0][1]) or sentence.endswith(
                        verb[0][2]) or sentence.endswith(verb[0][3]) or sentence.endswith(verb[0][4]):
                    self.verb = True
                    return True
            return False

    def checkFind(self, wordList, list):
        validcheck = False
        ld = len(wordList)
        list_to_string = ''.join(list)
        listMake = list_to_string.split('\n')
        print(listMake)
        for ci in listMake:
            t = ci.strip()
            print(t)
            if ld == 3:
                if t == wordList[- 2]:
                    validcheck = True
                    break
            else:
                pt = wordList[-3] + " " + wordList[-2]
                if t == pt:
                    validcheck = True
                    break
        return validcheck

    def khaiMethod(self, wordList, qstion,sentence):
        validcheck = False
        #print(qstion)
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence, ['খাই', 'খেয়েছিলাম', 'খাব'])) or \
                (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['খাও', 'খেয়েছিলে'])) or \
                (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['খায়', 'খেয়েছিল'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence, ['খান', 'খাবেন', 'খেয়েছেন'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence, ['খাবে'])):

            sentenceFoodList = ''.join(self.foodSentenceList)
            foodList = sentenceFoodList.split("\n")
            if wordList[-2] in foodList:
                validcheck = True

            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                        validcheck = True
       # print(validcheck)
        return validcheck

    def gaiMethod(self, wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence,
                                                                                 ['গাই', 'গেয়েছিলাম', 'গাব'])) or \
             (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['গাও', 'গেয়েছিলে'])) or \
             (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['গায়', 'গেয়েছিলো'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                 ['গান', 'গাবেন',
                                                                                                  'গেয়েছেন'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence, ['গাবে'])):

            if "গান" == wordList[- 2]:
                validcheck =  True
            else:
                validcheck = False
            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                    validcheck = True

        return validcheck

    def chaiMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence,
                                                                                 ['চাই', 'চেয়েছিলাম', 'চাব'])) or \
             (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['চাও', 'চেয়েছিলে'])) or \
             (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['চায়', 'চেয়েছিলো'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                 ['চান', 'চাবেন',
                                                                                                  'চেয়েছেন'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence, ['চাবে'])):
            validcheck =  self.checkFind(wordList, self.chaiSentenceList)
            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                    validcheck = True
        return validcheck

    def paiMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence,
                                                                                 ['পাই', 'পেয়েছিলাম', 'গাব'])) or \
             (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['পাও', 'পেয়েছিলে'])) or \
             (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['পায়', 'পেয়েছিলো'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                 ['পান', 'পাবেন',
                                                                                                  'পেয়েছেন'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence, ['পাবে'])):
             validcheck =self.checkFind(wordList, self.paiSentenceList)
             if qstion:
                 validcheck = False
                 if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                     validcheck = True

        return validcheck

    def jaiMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence,
                                                                                 ['যাই', 'গিয়েছিলাম', 'যাব'])) or \
             (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['যাও', 'গিয়েছিলে'])) or \
             (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['যায়', 'গিয়েছিলো'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                 ['যান', 'যাবেন',
                                                                                                  'গিয়েছেন'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence, ['যাবে'])):
                validcheck =  self.checkFind(wordList, self.placeSentenceList)
                if qstion:
                    validcheck = False
                    if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                        validcheck = True

        return validcheck

    def kheliMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence,
                                                                                 ['খেলি', 'খেলেছিলাম', 'খেলব'])) or \
             (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['খেলো', 'খেলেছিলে'])) or \
             (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['খেলে', 'খেলেছিল'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                 ['খেলেন', 'খেলতেন',
                                                                                                  'খেলেছিলেন'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence, ['খেলবে'])):
                print("yes")
                if qstion:
                    validcheck = False
                    if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                        validcheck = True

        return validcheck

    def valobasaiMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence, ['ভালোবাসি', 'ভালোবেসেছিলাম',
                                                                                            'ভালোবাসবো'])) or \
             (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence,
                                                                                   ['ভালোবাসো', 'ভালোবেসেছিলে'])) or \
             (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence,
                                                                                ['ভালোবাসে', 'ভালোবেসেছিল'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence, ['ভালোবাসেন',
                                                                                                            'ভালোবেসেছেন',
                                                                                                            'ভালোবেসেছিলেন'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence,
                                                                                                 ['ভালোবাসবে'])):
                print("yes")
                if qstion:
                    validcheck = False
                    if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                        validcheck = True

        return validcheck

    def pariMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence,
                                                                                 ['পারি', 'পেরেছিলাম', 'পারব'])) or \
             (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['পারো', 'পেরেছিলে'])) or \
             (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['পারে', 'পেরেছিলো'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                 ['পারেন', 'পারবেন',
                                                                                                  'পেরেছেন'])) or \
             (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence, ['পারবে'])):
            validcheck = self.checkFind(wordList, self.pariSentenceList)
            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                    validcheck = True

        return validcheck

    def koriMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence, ['করি', 'করেছিলাম', 'করব'])) or \
                (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['কর', 'করেছিলে'])) or \
                (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['করে', 'করেছিলো'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                    ['করেন', 'করবেন',
                                                                                                     'করেছেন'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence,
                                                                                                    ['করবে'])):
            validcheck = self.checkFind(wordList, self.koriSentenceList)
            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                    validcheck = True

        return validcheck

    def goriMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence, ['গড়ি', 'গড়েছিলাম', 'গড়ব'])) or \
                (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['গড়ো', 'গড়েছিলে'])) or \
                (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['গড়ে', 'গড়েছিলো'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                    ['গড়েন', 'গড়বেন',
                                                                                                     'গড়েছেন'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence,
                                                                                                    ['গড়বে'])):
           validcheck =self.checkFind(wordList, self.goriSentenceList)
           if qstion:
               validcheck = False
               if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                   validcheck = True

        return validcheck

    def choriMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence, ['চড়ি', 'চড়েছিলাম', 'চড়ব'])) or \
                (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['চড়ো', 'চড়েছিলে'])) or \
                (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['চড়ে', 'চড়েছিলো'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                    ['চড়েন', 'চড়বেন',
                                                                                                     'চড়েছেন'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence,
                                                                                                    ['চড়বে'])):
            validcheck =  self.checkFind(wordList, self.choriSentenceList)
            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                    validcheck = True

        return validcheck

    def asechiMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence,
                                                                               ['এসেছি', 'এসেছিলাম', 'আসব'])) or \
                (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['এসেছ', 'এসেছিলে'])) or \
                (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['এসেছে', 'এসেছিলো'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence,
                                                                                                    ['আসবেন', 'আসেন',
                                                                                                     'এসেছেন'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence,
                                                                                                    ['আসবে'])):
            validcheck =  self.checkFind(wordList, self.placeSentenceList)
            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                    validcheck = True

        return validcheck

    def aschiMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence, ['আছি', 'ছিলাম', 'থাকব'])) or \
                (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['আছো', 'ছিলে'])) or \
                (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['আছে', 'ছিলো'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence,
                                                                                                    ['থাকবে'])):
            print("yes")
            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                    validcheck = True

        return validcheck
    def achenMethod(self,wordList, qstion,sentence):
        validcheck = False
        if (self.startSentence(sentence, ['আমার', 'আমাদের', 'তোমার', 'তোমাদের']) and self.endSentence(sentence,
                                                                                                      ['আছে', 'ছিল',
                                                                                                       'থাকবে',
                                                                                                       'নাই'])) or \
                (self.startSentence(sentence, ['তার', 'তাদের্‌', 'আপনার', 'আপনাদের']) and self.endSentence(sentence,
                                                                                                           ['আছে',
                                                                                                            'ছিল',
                                                                                                            'থাকবে',
                                                                                                            'নাই'])):
            print("yes")
            if qstion:
                validcheck = False
                if (wordList[1] or wordList[-3]) == ("কি" or "কেন" or "কিভাবে" or "কোথায়"):
                    validcheck = True

        return validcheck

    def sentenceValidity(self, wordList, sentence, qstion):
        if self.khaiMethod(wordList, qstion,sentence) or self.gaiMethod(wordList, qstion,sentence) or self.chaiMethod(wordList, qstion,sentence) or self.paiMethod(wordList, qstion,sentence) or self.jaiMethod(wordList, qstion,sentence) \
                    or self.pariMethod(wordList, qstion,sentence)  or self.goriMethod(wordList, qstion,sentence)or self.koriMethod(wordList, qstion,sentence) or self.choriMethod(wordList, qstion,sentence) or self.achenMethod(wordList, qstion,sentence) \
                    or self.asechiMethod(wordList, qstion,sentence)or self.kheliMethod(wordList, qstion,sentence)  or self.valobasaiMethod(wordList, qstion,sentence) or self.aschiMethod(wordList, qstion,sentence):
            return True
        return False


    def sentenceChange(self,sentence):
        sentence = sentence.strip()
        wordlist = sentence.split(" ")
        p = ''
        if len(wordlist) > 1:
            wordlist[0] = 'সে'
            print("changed list: %s"%wordlist)
            for d in wordlist:
                p += d + " "
            p.strip()
        print(p)
        return p

    def rule(self, sentence):
        validcheck = False
        sentence = sentence.strip()
        print("Rule based: " +sentence)
        if sentence.endswith("।") or sentence.endswith("?"):
            qstion = False
            if sentence.endswith('না।'):
                sentence = sentence.replace(" না।", "")
            if sentence.endswith('না?'):
                sentence = sentence.replace(" না?", "")
                qstion = True
            if sentence.endswith('নাই।'):
                sentence = sentence.replace(" নাই।", "আছে")
            if sentence.endswith("।"):
                sentence = sentence.replace("।", "")
            if sentence.endswith("?"):
                sentence = sentence.replace("?", "")
                qstion = True
            wordList = sentence.split(' ')
            if self.sentenceValidity(wordList, sentence, qstion):
                validcheck = True
            elif qstion:
                if len(wordList) == 1:
                    if wordList[0] == ('কি'or'কে'or'কেন'or'কিভাবে'or'কখন' or 'কারা'):
                        validcheck = True
                else:
                    if self.startSentence(sentence, ['কে']) and self.endSentence(sentence,['আপনি', 'তুমি', 'সে', 'তিনি', 'আমি']):
                        validcheck = True
                    else:
                        p = 'আমি ' + sentence
                        pwordList = p.split(' ')
                        q = 'তুমি ' + sentence
                        qwordList = q.split(' ')
                        r = 'সে ' + sentence
                        rwordList = r.split(' ')
                        if self.sentenceValidity(pwordList, p, qstion):
                            validcheck = True
                        elif  self.sentenceValidity(qwordList, q, qstion):
                            validcheck = True
                        elif  self.sentenceValidity(rwordList, r, qstion):
                            validcheck = True
            else:
                for pt in self.universalTruthSentenceList:
                    if pt == sentence:
                        validcheck = True
        return validcheck



class Suggetion():
    senteceX = senteceY = None
    def __init__(self, window):
        self.button = QtWidgets.QToolButton(window)
        self.button.setPopupMode(QtWidgets.QToolButton.MenuButtonPopup)
        self.button.setMenu(QtWidgets.QMenu(self.button))
        self.menu = QtWidgets.QMenu(window)
        action = QtWidgets.QWidgetAction(self.button)
        action.setDefaultWidget(self.menu)
        self.button.menu().addAction(action)
        self.button.setVisible(False)
        self.rulebase = RuleBased()


    def positionSetup(self,x, y):
        self.button.setGeometry(QtCore.QRect(x, y, 10, 15))
    def newMenu(self, menuValue):
        for p in menuValue:
            self.menu.addMenu(p)
        #dr = self.menu.addMenu(menuValue)
        #dr.mouseReleaseEvent = self.mouseReleaseEvent

    def findSubject(self, sentence):
        subject = False
        verb = False
        print("find: %s"%sentence)
        if sentence.endswith('।'):
            sentence = sentence.replace('।', '')
        sentence = sentence.strip()
        wordList = sentence.split(' ')
        for dt in range (len(wordList)):
            if wordList[dt] == ('আমি' or 'আমরা' or 'তুমি' or 'তোমরা' or 'সে' or 'তিনি' or'তারা' or 'আপনি' or'আপনরা' or 'তাদের' or'আপনার'):
                wordList[0], wordList[dt] = wordList[dt], wordList[0]
                subject = True
                break
        print("seu: %s"%subject)
        if subject:
            if wordList[0] == ('আমি' or 'আমরা'):
                #print("yes")
                for dt in range(len(wordList)):
                    print(wordList[dt])
                    if wordList[dt] == (
                            'খাই' or 'খেয়েছিলাম' or 'খাব' or 'গাই' or 'গেয়েছিলাম' or 'গাব' or 'চাই' or 'চেয়েছিলাম' or 'চাব' or
                    'পাই'or'পেয়েছিলাম'or'পাব'or'যাই'or'গিয়েছিলাম'or'যাব'or'পারি'or'পেরেছিলাম'or'পারব'or'করি'or'করেছিলাম'or'করব'or'গড়ি'or'গড়েছিলাম'or'গড়ব'or'চড়ি'or'চড়েছিলাম'or'চড়ব'or'এসেছি'or'এসেছিলাম'or'আসব'or'খেলি'or'খেলেছিলাম'or'খেলব'or'ভালোবাসি'or'ভালোবেসেছিলাম'or'ভালবাসবো'):
                        wordList[-1], wordList[dt] = wordList[dt], wordList[-1]
                        print("yse %s"%wordList)
                        verb = True
            if wordList[0] == ('তুমি' or 'তোমরা'):
                for dt in range(len(wordList)):
                    if wordList[dt] == (
                            'খাও' or 'খেয়েছিলে' or 'খাবে' or 'গাও' or 'গেয়েছিলে' or 'গাবে' or 'চাও' or 'চেয়েছিলে' or 'চাবে' or
                    'পাও' or 'পেয়েছিলে' or 'পাবে' or 'যাও' or 'গিয়েছিলে'or'যাবে'or'পারো'or'পেরেছিলে'or'পারবে'or'কর'or'করেছিলে'or'করবে'or'গড়ো'or'গড়েছিলে'or'গড়বে'or'চড়ো'or'চড়েছিলে'or'চড়বে'or'এসেছো'or'এসেছিলে'or'আসবে'or'খেলো'or'খেলেছিলে'or'খেলবে'or'ভালোবাসো'or'ভালোবেসেছিলে'or'ভালবাসবে'):
                        wordList[-1], wordList[dt] = wordList[dt], wordList[-1]
                        verb = True
            if wordList[0] == ('সে' or 'তারা'):
                for dt in range(len(wordList)):
                    if wordList[dt] == (
                            'খায়' or 'খেয়েছিল' or 'খাবে' or 'গায়' or 'গেয়েছিল' or 'গাবে' or 'চায়' or 'চেয়েছিল' or 'চাবে' or
                    'পায়'or'পেয়েছিল'or'পাবে'or'যায়'or'গিয়েছিল'or'যাবে'or'পারে'or'পেরেছিল'or'পারবে'or'করে'or'করেছিল'or'করবে'or'গড়ে'or'গড়েছিল'or'গড়বে'or'চড়ি'or'চড়েছিল'or'চড়বে'or'এসেছে'or'এসেছিল'or'আসবে'or'খেলি'or'খেলেছিল'or'খেলবে'or'ভালোবাসে'or'ভালোবেসেছিল'or'ভালবাসবে'):
                        wordList[-1], wordList[dt] = wordList[dt], wordList[-1]
                        verb = True
            if wordList[0] == ('তিনি' or 'সে' or 'আপনি'or 'আপনরা'or'তারা'):
                for dt in range(len(wordList)):
                    if wordList[dt] == (
                                'খেয়েছেন' or 'খেয়েছিলেন' or 'খাবেন' or 'গেয়েছেন' or 'গেয়েছিলেন' or 'গাবেন' or 'চেয়েছেন' or 'চেয়েছিলেন' or 'চাবেন' or
                        'পেয়েছেন'or'পেয়েছিলেন'or'পাবেন'or'গিয়েছেন'or'গিয়েছিলেন'or'যাবেন'or'পারেছেন'or'পেরেছিলেন'or'পারবেন'or'করেছেন'or'করেছিলেন'or'করবেন'or
                                'গড়েছেন'or'গড়েছিলেন'or'গড়বেন'or'চড়েছেন'or'চড়েছিলেন'or'চড়বেন'or'এসেছেন'or'এসেছিলেন'or'আসবেন'or'খেলেছেন'or'খেলেছিলেন'or'খেলবেন'or'ভালোবাসেন'or'ভালোবেসেছিলেন'or'ভালবাসবেন'):
                        wordList[-1], wordList[dt] = wordList[dt], wordList[-1]
                        verb = True
            if wordList[0] == ('আমার' or 'তার' or 'তাদের' or 'আমাদের' or 'আপনর' or 'আপনাদের'):
                for dt in range(len(wordList)):
                    if wordList[dt] == (
                            'আছে' or 'ছিল' or 'থাকবে'):
                        wordList[-1], wordList[dt] = wordList[dt], wordList[-1]
                        verb = True
        print(wordList)
        v = None
        if (not subject) and verb:
            for dt in wordList:
                if dt == ('যায়' or 'যাবে'):
                    v = dt
                    wordList[-1], dt = dt, wordList[-1]
                    break
            if v == ('যায়' or 'যাবে'):
                for dt in wordList:
                    for ct in self.rulebase.placeSentenceList:
                        if ct == dt:
                            dt, wordList[-2] = wordList[-2], dt
                            break
        sen = ''
        print(wordList)
        for d in wordList:
            sen += d +" "
        sen.strip()
        sen += '।'
        #print("word list: %s" %wordList)
        return sen

    #def mouseReleaseEvent(self, event):
     #   if event.b

    def se(self, wordlist, rule):
        d  = {1,2}
        d.clear()
        for t in rule.test:
            t = t.strip()
            pt = t.split(" ")
            print()
            if len(pt) == len(wordlist):
                for g in range(0, len(wordlist)):
                    if pt[g] == wordlist[g]:
                        d.add(t)
                        break
        return d


class N_Gram_Checker:
    predictValue = 1.0
    predictBool = None
    sentenceList2 = None
    sentenceList3 = None
    sentenceList4 = None
    sentenceList5 = None
    def __init__(self):
        file = open(".\\main-dataset.txt", "rb")
        readFile = (file.read()).decode()
        sentenceList = readFile.split("\r\n")
        sentenceList[0] = sentenceList[0].replace("\ufeff", "")
        self.sentenceList2 = self.modifySentence(sentenceList.copy(), 2)
        self.sentenceList3 = self.modifySentence(sentenceList.copy(), 3)
        self.sentenceList4 = self.modifySentence(sentenceList.copy(), 4)
        self.sentenceList5 = self.modifySentence(sentenceList.copy(), 5)


    def sentenceValidity(self, predict, wlen):
        predict = predict.strip()
        self.predictBool = False
        predict2 = self.modifyPredict(predict, 2)
        predict3 = self.modifyPredict(predict, 3)
        predict4 = self.modifyPredict(predict, 4)
        predict5 = self.modifyPredict(predict, 5)
        print(predict)
        predictValue2 = self.nGram(self.sentenceList2, predict2, 2)
        predictValue3 = self.nGram(self.sentenceList3, predict3, 3)
        predictValue4 = self.nGram(self.sentenceList4, predict4, 4)
        predictValue5 = self.nGram(self.sentenceList5, predict5, 5)
        print("Bigram: %f"%predictValue2)
        print("Trigram: %f"%predictValue3)
        print("Forth-gram: %f"%predictValue4)
        print("Fifth-gram: %f"%predictValue5)
        if wlen == 1:
            self.predictBool = True
        elif wlen == 2:
           if predictValue2 >= 0.000015 and predictValue2 <= 0.0032:
            self.predictBool = True
        elif wlen == 3:
            if predictValue2 >= 0.000015 and predictValue2 <= 0.0032:
                self.predictBool = True
            self.predictBool = self.valueCheck(0.00012, 0.0033, self.predictBool, predictValue3)
        elif wlen == 4:
            if predictValue2 >= 0.0000018001 and predictValue2 <= 0.0032:
                self.predictBool = True
            self.predictBool = self.valueCheck(0.00021, 0.0033, self.predictBool, predictValue3)
            self.predictBool = self.valueCheck(0.00021, 0.0033, self.predictBool, predictValue4)

        elif wlen == 5:
            if predictValue2 >= 0.000001001 and predictValue2 <= 0.0032:
                self.predictBool = True
            self.predictBool = self.valueCheck(0.00021, 0.0033, self.predictBool, predictValue3)
            self.predictBool = self.valueCheck(0.00021, 0.0033, self.predictBool, predictValue4)
            self.predictBool = self.valueCheck(0.00021, 0.0033, self.predictBool, predictValue5)
        elif wlen > 5:
            if predictValue2 >= 0.0001001 and predictValue2 <= 0.0032:
                 self.predictBool = True
            self.predictBool = self.valueCheck(0.000031, 0.0033, self.predictBool, predictValue3)
            self.predictBool = self.valueCheck(0.000031, 0.0033, self.predictBool, predictValue4)
            self.predictBool = self.valueCheck(0.000031, 0.0033, self.predictBool, predictValue5)

        return self.predictBool

    def valueCheck(self, start, end, predictBool, predictValue):
        # print(predictValue)
         if predictBool:
                if predictValue >= start and predictValue <= end:
                    return True
                else:
                    return False
         return predictBool

    def countValue(self, sentenceList, InputSentence):
        count = 0
        for sentence in sentenceList:
            found = sentence.find(InputSentence, 0, len(sentence))
            if found != -1:
                count = count + 1
        return count

    def modifySentence(self, sentenceList, number):
        number = number - 1
        start = ""
        end = ""
        for i in range(number):
            start += "START "
            end += " END"
        for index in range(len(sentenceList)):
            sentenceList[index] = start + sentenceList[index] + end
        return sentenceList

    def modifyPredict(self, sentence, number):
        number = number - 1
        start = ""
        end = ""
        for i in range(number):
            start += "START "
            end += " END"
        sentence = start + sentence + end
        return sentence

    def nGram(self, sentenceList, predict, number):
        test = predict.split()
        probability = 1.0
        for i in range(0, len(test) - number):
            predict_upper = test[i]
            predict_lower = test[i]
            for j in range(i + 1, i + number - 1):
                predict_lower += " " + test[j]
            for j in range(i + 1, i + number):
                predict_upper += " " + test[j]
            upperCount = self.countValue(sentenceList, predict_upper)
            lowerCount = self.countValue(sentenceList, predict_lower)
            if upperCount == 0 or lowerCount == 0:
                upperCount += 1
                lowerCount += 1
            probability *= (upperCount / lowerCount)
        return probability

    def wordlen(self,predict):
        word = predict.split(' ')
        return len(word)


class Ui_Dialog(object):
    v = N_Gram_Checker()
    rulebased = RuleBased()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(3, 0, 800, 581))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Bengali, QtCore.QLocale.Bangladesh))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit.setMouseTracking(True)
        self.textEdit.setStyleSheet("font-size: 12pt;")
        self.textEdit.keyReleaseEvent = self.keyReleaseEvent

        self.suggestionArray = []
        for t in range(100):
            self.suggestionArray.append(Suggetion(MainWindow))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "বাংলা ব্যাকরণ নিরীক্ষক"))
        Dialog.setWindowIcon(QtGui.QIcon(".\\Image\\images icon.jpg"))






    def ke(self, e):
        print(e.key())

    def keyReleaseEvent(self,e):
        #print(e.key())
        if e.key() == QtCore.Qt.Key_Space or e.key() == 16777220:
            r = self.textEdit.toPlainText()
            newsen = r.split('।')
            sen = r.split(' ')
           # print(sen)
            self.textEdit.clear()
            countNumber = 1
            wordNumber = 0
            ps = ""
            senten = 0
            runChecker = False
            qst = 0
            op = False
            qstion = False
            qTos = False
            ds = None
            ne = False
            for sugg in self.suggestionArray:
                sugg.button.setVisible(False)
           # print(newsen)
            for q in sen:
                t = q.split("\n")
                if len(t) > 1:
                    q = t[0]
                    ne = True
                else:
                    ne = False
                if q.endswith('।'):
                    runChecker = True
                    op = True
                    qst = 0

                else:
                    op = False
                #print(ne)
                qstion = False
                if q.endswith('?'):
                    runChecker = True
                    qstion = True
                    ds = newsen[senten].split('?')
                if countNumber == len(sen):
                    runChecker = True
                wordNumber += 1
                ps += q + " "
                if runChecker:
                    snt = ps
                    if op:
                        snt = newsen[senten]+"।"
                    if qstion :
                        snt = ds[qst]+"?"
                    elif qTos:
                        snt = ds[-1]+"।"
                    validSentence = self.v.sentenceValidity(snt, wordNumber)

                    self.rulebased.subject = False
                    self.rulebased.verb = False
                    rulebaseBool = self.rulebased.rule(snt)

                    print("Rule Result: %s"%rulebaseBool)
                    if (not rulebaseBool) and (not self.rulebased.subject):
                                rulebaseBool = self.rulebased.rule(self.rulebased.sentenceChange(snt))
                                print("Changed Rule Result: %s" % rulebaseBool)
                    if  rulebaseBool:
                        self.textEdit.setTextColor(QtGui.QColor("Black"))
                    else:
                        self.textEdit.setTextColor(QtGui.QColor("Red"))
                    print("Rule Result: %s"%rulebaseBool)
                    print("Subject: %s" % self.rulebased.subject)
                    print("verb: %s" % self.rulebased.verb)
                    if qstion :
                        self.textEdit.insertPlainText(ds[qst]+"?")
                        qst += 1
                        qTos = True
                    else:
                        if qTos:
                            self.textEdit.insertPlainText(ds[-1])
                            qTos = False
                            senten += 1
                        else:
                            self.textEdit.insertPlainText(newsen[senten])
                            #print(newsen[senten])
                            senten += 1
                        if op:
                            self.textEdit.insertPlainText("।")


                            txtln = len(self.textEdit.toPlainText())
                            #print(txtln)
                        if ne and countNumber == len(sen):
                            self.textEdit.insertPlainText("\n")



                    runChecker = False
                    wordNumber = 0
                    ps = ""
                #print(op)
                #if op or qstion:
                    #print(validSentence)
                    #if not (validSentence and rulebaseBool):
                        #print(snt)
                        #for sug in self.suggestionArray:
                            #if not sug.button.isVisible():
                                #newsnt = sug.se(snt.strip(), self.rulebased)
                                #sug.newMenu(newsnt)
                                #sug.button.setVisible(True)
                                #sug.positionSetup(len(self.textEdit.toPlainText()) * 7 + 2 * (countNumber), 6)
                                #break

                countNumber += 1





if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

