# coding: utf-8
import tweepy
import random
import PhraseGen
import Tags


from Secret import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def twit(): 

	tag = Tags.Tags[random.randint(0, len(Tags.Tags)-1)]
	

	boss_chance = random.randint(0, 10)
	if (boss_chance == 0):
		tag = "Boss"
		phrase = PhraseGen.generate_boss()
	else:
		phrase = PhraseGen.generate_phrase(tag).title()

	phrase += " #%s #%s" % (tag, "Колбаска")
	print("Got phrase %s" % phrase)
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) 
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET) 
	api = tweepy.API(auth)
	api.update_status(status=phrase)


if __name__=="__main__":
	twit()
