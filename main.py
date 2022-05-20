import os
import random

def setLanguage(i):
	global LanguageList
	global ShowText_Choose
	global ShowText_MakeSentenceBase
	global ShowText_MakeSentencePro
	global ShowText_MakeArticle
	global ShowText_Plenty
	global ShowText_Finish
	global ShowText_NoDivided
	LLst = i
	UILanguageFile = open("./resources/"+LanguageList[i]+"/UILanguage.txt","r",encoding='UTF-8')
	UILanguageFileContent = UILanguageFile.readlines()
	for i in UILanguageFileContent:
		i = i.split("=")
		if i[0] == "ShowText_Choose":
			ShowText_Choose = i[1].replace("\n","")
		elif i[0] == "ShowText_MakeSentenceBase":
			ShowText_MakeSentenceBase = i[1].replace("\n","")
		elif i[0] == "ShowText_MakeSentencePro":
			ShowText_MakeSentencePro = i[1].replace("\n","")
		elif i[0] == "ShowText_MakeSentenceBase":
			ShowText_MakeSentenceBase = i[1].replace("\n","")
		elif i[0] == "ShowText_MakeArticle":
			ShowText_MakeArticle = i[1].replace("\n","")
		elif i[0] == "ShowText_Plenty":
			ShowText_Plenty = i[1].replace("\n","")
		elif i[0] == "ShowText_Finish":
			ShowText_Finish = i[1].replace("\n","")
		elif i[0] == "ShowText_NoDivided":
			ShowText_NoDivided = i[1].replace("\n","")
	UILanguageFile.close()
	InitialisationOperation(LLst)

def MakePhrase(Gramma):
	global MixedList
	global NounList
	global PersonList
	global NoDivided
	Pattern = Gramma.split(";")
	a = 0
	OutSentence = []
	if NoDivided == "1":
		for i in Pattern:
			if i == "WRUB.Noun":
				OutSentence.append(MixedList[random.randint(0,len(MixedList)-1)])
			elif i == "WRUB.Person":
				OutSentence.append(MixedList[random.randint(0,len(MixedList)-1)])
			else:
				OutSentence.append(i)
	else:
		for i in Pattern:
			if i == "WRUB.Noun":
				OutSentence.append(NounList[random.randint(0,len(NounList)-1)])
			elif i == "WRUB.Person":
				OutSentence.append(PersonList[random.randint(0,len(PersonList)-1)])
			else:
				OutSentence.append(i)
	Out = ""
	for i in OutSentence:
		Out = Out + str(i)
	return Out

def MakeSentenceBase():
	global GrammaList
	global NounList
	global PersonList
	global SentenceBaseList
	global MixedList
	global NoDivided
	global TimeList
	global LocationList
	global AdverbList
	Pattern = SentenceBaseList[random.randint(0,len(SentenceBaseList)-1)].split(";")
	OutSentence = []
	for i in Pattern:
		if i == "WRUB.Noun":
			OutSentence.append(NounList[random.randint(0,len(NounList)-1)])
		elif i == "WRUB.Verb":
			OutSentence.append(MakePhrase(GrammaList[random.randint(0,len(GrammaList)-1)]))
		elif i == "WRUB.Time":
			OutSentence.append(TimeList[random.randint(0,len(TimeList)-1)])
		elif i == "WRUB.Location":
			OutSentence.append(LocationList[random.randint(0,len(LocationList)-1)])
		elif i == "WRUB.Adverb":
			OutSentence.append(AdverbList[random.randint(0,len(AdverbList)-1)])
		else:
			OutSentence.append(i)
	Out = ""
	for i in OutSentence:
		Out = Out + str(i)
	return Out

def MakeSentencePro():
	global GrammaList
	global NounList
	global PersonList
	global SentenceProList
	global MixedList
	global NoDivided
	global TimeList
	global LocationList
	global AdverbList
	OutSentence = []
	Pattern = SentenceProList[random.randint(0,len(SentenceProList)-1)].split(";")
	OutSentence = []
	for i in Pattern:
		if i == "WRUB.Noum":
			OutSentence.append(NounList[random.randint(0,len(NounList)-1)])
		elif i == "WRUB.Verb":
			OutSentence.append(MakePhrase(GrammaList[random.randint(0,len(GrammaList)-1)]))
		elif i == "WRUB.Time":
			OutSentence.append(TimeList[random.randint(0,len(TimeList)-1)])
		elif i == "WRUB.Location":
			OutSentence.append(LocationList[random.randint(0,len(LocationList)-1)])
		elif i == "WRUB.Adverb":
			OutSentence.append(AdverbList[random.randint(0,len(AdverbList)-1)])
		else:
			OutSentence.append(i)
	Out = ""
	for i in OutSentence:
		Out = Out + str(i)
	return Out

def MakeArticle():
	global NoDivided
	Times = int(input(ShowText_Plenty))
	NoDivided = input(ShowText_NoDivided)
	Out = ""
	for i in range(0,Times):
		if i == random.randint(0,1):
			Out = Out + MakeSentencePro()
		else:
			Out = Out + MakeSentenceBase()
	print(Out)

def InitialisationOperation(LLst):
	global GrammaList
	global LanguageList
	global SentenceProList
	global SentenceBaseList
	global PersonList
	global NounList
	global MixedList
	global TimeList
	global LocationList
	global AdverbList
	GrammaList = []
	SentenceBaseList = []
	SentenceProList = []
	PersonList = []
	NounList = []
	TimeList = []
	LocationList = []
	AdverbList = []
	GrammaFile = open("./resources/"+LanguageList[LLst]+"/Gramma.txt","r",encoding='UTF-8')
	GrammaFileContent = GrammaFile.readlines()
	for i in GrammaFileContent:
		GrammaList.append(i.replace("\n",""))
	GrammaFile.close()
	SentenceProFile = open("./resources/"+LanguageList[LLst]+"/SentencePro.txt","r",encoding='UTF-8')
	SentenceProFileContent = SentenceProFile.readlines()
	for i in SentenceProFileContent:
		SentenceProList.append(i.replace("\n",""))
	SentenceProFile.close()
	SentenceBaseFile = open("./resources/"+LanguageList[LLst]+"/SentenceBase.txt","r",encoding='UTF-8')
	SentenceBaseFileContent = SentenceBaseFile.readlines()
	for i in SentenceBaseFileContent:
		SentenceBaseList.append(i.replace("\n",""))
	SentenceBaseFile.close()
	NounFile = open("./resources/"+LanguageList[LLst]+"/Noun.txt","r",encoding='UTF-8')
	NounFileContent = NounFile.readlines()
	for i in NounFileContent:
		NounList.append(i.replace("\n",""))
	NounFile.close()
	PersonFile = open("./resources/"+LanguageList[LLst]+"/Person.txt","r",encoding='UTF-8')
	PersonFileContent = PersonFile.readlines()
	for i in PersonFileContent:
		PersonList.append(i.replace("\n",""))
	PersonFile.close()
	ModifierFile = open("./resources/"+LanguageList[LLst]+"/Modifier.txt","r",encoding='UTF-8')
	ModifierFileContent = ModifierFile.readlines()
	for i in ModifierFileContent:
		i = i.split("=")
		if i[0] == "Time":
			TimeList.append(i[1].replace("\n",""))
		elif i[0] == "Location":
			LocationList.append(i[1].replace("\n",""))
		elif i[0] == "Adverb":
			AdverbList.append(i[1].replace("\n",""))
	ModifierFile.close()
	MixedList = []
	for i in NounList:
		MixedList.append(i)
	for i in PersonList:
		MixedList.append(i)


LanguageList = os.listdir("./resources/")
print("Choose your language\n=====")
i = 0
for i in range(0,len(LanguageList)):
	print(str(i)+" "+LanguageList[i])
	i=i+1
setLanguage(int(input("=====\nLanguage: ")))
print(ShowText_Finish)
while True:
	print("====="+ShowText_Choose+"\n=====\n1)"+ShowText_MakeSentenceBase+"\n2)"+ShowText_MakeSentencePro+"\n3)"+ShowText_MakeArticle+"\n=====")
	Choose = int(input(ShowText_Choose+": "))
	if Choose == 1:
		NoDivided = input(ShowText_NoDivided)
		print(MakeSentenceBase())
	elif Choose == 2:
		NoDivided = input(ShowText_NoDivided)
		print(MakeSentencePro())
	elif Choose == 3:
		MakeArticle()
	else:
		print("None")
