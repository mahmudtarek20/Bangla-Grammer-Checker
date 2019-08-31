
class RuleBased():
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

    def fileOpen(self, str):
        file = open(".\\rule\\"+str+".txt", "rb")
        readFile = (file.read()).decode()
        sentenceList = readFile.split("\r\n")
        sentenceList[0] = sentenceList[0].replace("\ufeff", "")
        return sentenceList

    def startSentence(self, sentence, *person):
            pl = len(person[0])
            if pl == 1:
                if sentence.startswith(person[0][0]):
                    return True
            elif pl == 2:
                if sentence.startswith(person[0][0]) or sentence.startswith(person[0][1]):
                    return True
            elif pl == 3:
                if sentence.startswith(person[0][0]) or sentence.startswith(person[0][1]) or sentence.startswith(person[0][2]):
                    return True
            elif pl == 4:
                if sentence.startswith(person[0][0]) or sentence.startswith(person[0][1]) or sentence.startswith(person[0][2]) or sentence.startswith(person[0][3]):
                    return True
            elif pl == 5:
                if sentence.startswith(person[0][0]) or sentence.startswith(person[0][1]) or sentence.startswith(person[0][2]) or sentence.startswith(person[0][3]) or sentence.startswith(person[0][4]):
                    return True
            return False

    def endSentence(self, sentence, *verb):
            pl = len(verb[0])
           # print(pl)
            if pl == 1:
                if sentence.endswith(verb[0][0]):
                    return True
            elif pl == 2:
                if sentence.endswith(verb[0][0]) or sentence.endswith(verb[0][1]):
                    return True
            elif pl == 3:
                if sentence.endswith(verb[0][0]) or sentence.endswith(verb[0][1]) or sentence.endswith(verb[0][2]):
                    return True
            elif pl == 4:
                if sentence.endswith(verb[0][0]) or sentence.endswith(verb[0][1]) or sentence.endswith(
                        verb[0][2]) or sentence.endswith(verb[0][3]):
                    return True
            elif pl == 5:
                if sentence.endswith(verb[0][0]) or sentence.endswith(verb[0][1]) or sentence.endswith(
                        verb[0][2]) or sentence.endswith(verb[0][3]) or sentence.endswith(verb[0][4]):
                    return True
            return False

    def checkFind(self, wordList, list):
        validcheck = False
        ld = len(wordList)
        for ci in list:

            if ld == 3:
                if ci == wordList[len(wordList) - 2]:
                    validcheck = True
                    break
            else:
                pt = wordList[ld - 3] + " " + wordList[ld - 2]
                if ci == pt:
                    validcheck = True
                    break
        return validcheck

    def khaiMethod(self, wordList, qstion,sentence):
        validcheck = False
        #print(qstion)
        if (self.startSentence(sentence, ['আমি', 'আমরা']) and self.endSentence(sentence, ['খাই', 'খেয়েছিলাম', 'খাব'])) or \
                (self.startSentence(sentence, ['তুমি', 'তোমরা']) and self.endSentence(sentence, ['খাও', 'খেয়েছিলে'])) or \
                (self.startSentence(sentence, ['সে', 'তারা']) and self.endSentence(sentence, ['খায়', 'খেয়েছিলো'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'আপনি', 'আপনরা']) and self.endSentence(sentence, ['খান', 'খাবেন', 'খেয়েছেন'])) or \
                (self.startSentence(sentence, ['সে', 'তারা', 'তুমি', 'তোমরা']) and self.endSentence(sentence, ['খাবে'])):
            for fd in self.foodSentenceList:
                if fd == wordList[-2]:
                    validcheck = True
                    break
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
                print("yes")
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
            validcheck =  self.checkFind(wordList, self.placeSentenceListiSentenceList)
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
    def rule(self, sentence):
        validcheck = False
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

if __name__ == "__main__":
    import sys
    rulebased = RuleBased()
    sentence = input()
    print(rulebased.rule(sentence))

