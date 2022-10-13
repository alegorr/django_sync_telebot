# sync version
import telebot
from telebot import TeleBot
from telebot.types import Update
from service1 import settings
from core.models import User, Service, Transaction
from core import constants
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse
from django.shortcuts import render
import requests

##########
# Init bot
##########
bot = TeleBot(settings.TELEBOT_API_TOKEN)

if settings.WEBHOOK_URL:
    try:
        bot.remove_webhook()
    except:
        pass
    try:
        bot.set_webhook(url=settings.WEBHOOK_URL)
    except Exception as err:
        print("Can not set Telebot webhook: ", err)


###################
# Register services
###################
for service_address, service_name in settings.TELEBOT_KNOWN_SERVICES:
    try:
        Service.objects.create(name=service_name, address=service_address)
    except Exception as err:
        try:
            service = Service.objects.get(address=service_address)
            print("service address already in use: ", service.address)
        except:
            print("service registering error: ", err)

##################
# Helper functions
##################
def get_user(message):
    u = message.from_user
    user = None
    try:
        user = User.objects.get(id=u.id)
    except Exception as err:
        print("user object not found: ", err)
        try:
            user = User.objects.create(id=u.id, username=u.username)
        except Exception as err:
            print("object creation error: ", err)
    return user

def get_service(name):
    service = None
    try:
        service = Service.objects.get(name=name)
    except Exception as err:
        print("can't find service ", name)
    return service

def get_help_message():
    services_info = ""
    try:
        for service in Service.objects.all():
            services_info += service.name + "\n"
    except:
        services_info = "None"
    return constants.BOT_HELP_MESSAGE + services_info

def choose_service(user, service):
    if service:
        user.service = service
        user.save()
        bot.send_message(chat_id=message.chat.id, text=constants.BOT_SERVICE_MESSAGE.format(user.service.name))

def make_transaction(message):
    try:
        user = get_user(message)
        if user.service:
            transaction = Transaction.objects.create(user=user, service=user.service, input=message.text)
            service_address = user.service.address
            result = requests.post(service_address, json={"sentences": message.text.split(",")})
            if result.status_code == 200:
                text = str(result.json())
                bot.send_message(chat_id=message.chat.id, text=text)
                transaction.output=text
                transaction.complete=True
                transaction.save()
                print("transaction succeeded +", transaction.id)
            else:
                err_msg = constants.BOT_ERROR_MESSAGE % str(result.status_code)
                bot.send_message(chat_id=message.chat.id, text=err_msg)
                print("transaction error {}".format(result.status_code), transaction.id)
    except Exception as err:
        print("error process message: ", err)

##################
# Message handlers
##################
@bot.message_handler(commands=['start'])
def show_start_help(message):
    bot.send_message(chat_id=message.chat.id, text=constants.BOT_START_MESSAGE)

@bot.message_handler(commands=['help'])
def show_help(message):
    bot.send_message(chat_id=message.chat.id, text=get_help_message())

@bot.message_handler(commands=['bad'])
def choose_badlist_service(message):
    choose_service(get_user(message), get_service('badlisted_words'))

@bot.message_handler(commands=['spacy'])
def choose_badlist_service(message):
    choose_service(get_user(message), get_service('spacy_nounphrases'))

@bot.message_handler(func=lambda message: message.text not in constants.BOT_KNOWN_COMMANDS, content_types=['text'])
def process_message(message):
    make_transaction(message=message)

#######################
# Process webhook calls
#######################
@csrf_exempt
@require_POST
def pull_messages(request):
    print(request.body.decode("utf-8"))
    updates = Update.de_json(request.body.decode("utf-8"))
    bot.process_new_updates([updates])
    return HttpResponse(status=200)

#############
# Debug views
#############
@require_GET
def view_data(request):
    return render(request, "debug/view_data.html", { 'users': User.objects.all(), 'transactions': Transaction.objects.all(), 'services': Service.objects.all()})
