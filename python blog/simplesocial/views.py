from django.views.generic import TemplateView

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = 'index.html'

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
"""bot = ChatBot("Ron Obvious")"""
"""bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)"""
"""trainer = ListTrainer(bot)"""

chatbot = ChatBot(
    'Ron Obvious'
)
chatbot.set_trainer(ListTrainer)
# Train based on the english corpus

#Already trained and it's supposed to be persistent
#chatbot.train("chatterbot.corpus.english")
<<<<<<< HEAD
"""for files in os.listdir('F:\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/'):
    data = open('F:\chatterbot-corpus-master\chatterbot-corpus-master\chatterbot_corpus\data\english/' + files ,'r',encoding='utf-8').readlines()
    chatbot.train(data)
"""
=======
for files in os.listdir(r'C:\Users\Bourne\Desktop\chat\python-learning-blog-master\chats/'):
    data = open(r'C:\Users\Bourne\Desktop\chat\python-learning-blog-master\chats/' + files ,'r',encoding='utf-8').readlines()
    chatbot.train(data)
>>>>>>> 9f74951c1bcea5533304edaa156ab4bf5c0cd082
@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':

		data = json.loads(request.body)
		message = data['message']


		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)


def home(request, template_name="home.html"):
	context = {'title': 'Chatbot Version 1.0'}
	return render_to_response(template_name, context)
