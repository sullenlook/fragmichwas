#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib2, urllib
import json
from plugin import *
from plugin import __criteria_key__
from siriObjects.uiObjects import AddViews
from siriObjects.answerObjects import AnswerSnippet, AnswerObject, AnswerObjectLine
import pprint
from random import randint
import os, random

mps = {
	'ps':
	{	1:"Grammatik",
		2:"Aussprache",
		3:"Schaetzen",
		4:"Matematik",
		5:"Arsch und Titten",
		6:"Umgangssprache",
		7:"Zitate"
	},
	'qs':
	{ 
	1:"Wie ist die korrekte Schreibweise '':\n1: Misissippi\n2: Mississippi\n3: Missisippi\n4: Mississipi",
	2:"Wie ist die richtige Aussprache von 'Meme': 1, 2, 3 or 4",
	3:"Welches ist das meistgefahrene Auto in Deutschland, \n1: Opel\n2: BMW\n3: Mercedes-Benz\n4: Volkswagen",
	4:"7 x 25 + 180 - 72 + 25 x 25 :\n1: 908\n2: 890\n3: 980\n4: 809",
	5:"Wer ist die Geilste Frau der Welt?",
	6:"Was sagt man auch wenn es 24:00 Uhr ist?",
	7:"Was hat Roger gesagt:\n1: Rotze-Kuchen-Dumm\n2: Rotze-Kuchen-Hohl\n3: Rotze-Kuchen-Doof\n4: Geiler als Rotze-Kuchen"
	},
	'sqs':
	{ 
	1:"Welche ist die korrekte Schreibweise von Mississippi: 1, 2, 3 oder 4?",
	2:"Welche ist die richtige Aussprache des Wortes: 1: may may. 2: me me. 3: meme oder 4: my my?",
	3:"Welches ist das meistgefahrene Auto in Deutschland, 1, Opel. 2, BMW. 3, Mercedes-Benz oder 4, Volkswagen?",
	4:"Was ist sieben mal fuenfundzwanzig plus hundertachzig minus zweiundsiebzig plus fuenfundzwanzig plus fuenfundzwanzig: 1, neunhundertacht. 2, achthundertneunzig. 3, neunhundertachzig oder 4, achthundertneun?",
	5:"Wie heisst die Geilste Frau auf der ganzen Welt?",
	6:"Was sagt man auch wenn es zwoelf uhr ist?",
	7:"Was hat Roger gesagt:\n1: Alle Weiber sind Rotze-Kuchen-Dumm\n2: Alle Weiber sind Rotze-Kuchen-Hohl\n3: Alle Weiber sind Rotze-Kuchen-Doof\n4: Jedes Weib ist Geiler als'n Rotze-Kuchen?"
	},
	'ans':
	{
	1:"2",
	2:"3",
	3:"4",
	4:"1",
	5:"hilton",
	6:"mitternacht",
	7:"2"
	}
}

class priv(Plugin):
	@register("de-DE", "test frage")
	def authtest(self, speech, language, regex):
		if self.assistant_id() == "[6CF4E775-2DB0-4C99-A5D8-DB1B35EEDE00":
			self.say("Zugelassen!")
		else:
			self.say("Netter Versuch, Newfag...","Netter Versuch Newfag.")
			ans = self.ask(u"  ▲\n▲ ▲","Ich wette, Du schaffst es nicht").lower()
			if ans != "op ist eine Schwuchtel" and ans != "new fag" and ans != "newfag":
				view = AddViews(self.refId, dialogPhase="Completion")
				ImageAnswer = AnswerObject(title=str("Trolololololololololololololololololololololololololololol"),lines=[AnswerObjectLine(image="http://harryj.co.uk/t.gif")])
				view1 = AnswerSnippet(answers=[ImageAnswer])
				view.views = [view1]
				self.sendRequestWithoutAnswer(view)
				answer = None
				filename = "./plugins/priv/cat.txt"
				file = open(filename, 'r')
				file_size = os.stat(filename)[6]
				while answer != "Yes" and answer != "Yeah":
					lnum = random.randint(0, file_size-1)
					file.seek((file.tell()+lnum)%file_size)
					file.readline()
					line=file.readline()
					self.say("Cat fact number "+str(lnum)+":\n"+str(line).rstrip('\n'))
					answer = self.ask("Did you know that?")
			view = AddViews(self.refId, dialogPhase="Completion")
			ImageAnswer = AnswerObject(title=str(""),lines=[AnswerObjectLine(image="http://harryj.co.uk/b.gif")])
			view1 = AnswerSnippet(answers=[ImageAnswer])
			view.views = [view1]
			self.sendRequestWithoutAnswer(view)
		self.complete_request()

	@register("de-DE",".*(Frag mich was|Frang mich was|Spiel mit mir|Ich will spielen)(.*(?P<level>[1-9]))?")
	def memequiz(self,speech,language,regex):
		gameDone = False
		if regex.group('level'):
			level = int(regex.group('level'))
		else:
			level = 1
		if level != 1:
			passwordAttempt = self.ask("Die naechste Frage kommt aus dem Bereich "+str(level)+"?")
			while passwordAttempt.lower() != mps['ps'][level]:
				self.say("Incorrect.")
				passwordAttempt = self.ask("Wie lautet das Passwort fuer Level "+str(level)+"?")
		self.say(u"Starte level "+str(level))
		ans = "NONE"
		while gameDone == False:
			while ans.lower() != mps['ans'][level]:
				ans = self.ask(mps['qs'][level],mps['sqs'][level])
			self.say("Korrekt!")
			if level != 1: self.say("Der Code wird auf dieses level zurueck gesetzt '"+str(mps['ps'][level])+"'")
			ans = "NONE"
			level = level +1
			if level >7:
				self.say("Du hast Gewonnen!!!!")
				gameDone = True
		self.complete_request()

