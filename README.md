# Simple build and run command
sudo bash rund.sh

# Swap between deployment command
sudo bash config.sh

# Check service
http://localhost:8000/debug

# Environment
TELEBOT_ALLOWED_HOSTS is allowed hosts URLs or IPs for deployment
TELEBOT_WEBHOOK_HOST is URL of deploy server
TELEBOT_SECRET_KEY is Django secret key for a security feature
TELEBOT_API_TOKEN is Telegram API Token from the @BotFather
TELEBOT_KNOWN_SERVICES are urls of deeppavlov.ai services
TELEBOT_KNOWN_SERVICES_NAMES are services names

# Example
TELEBOT_ALLOWED_HOSTS=0.0.0.0,127.0.0.1,localhost
TELEBOT_WEBHOOK_HOST=deeppavlov1.herokuapp.com
TELEBOT_SECRET_KEY=cpMc1yf3jucvj5/hIaW47xRFI8VemFxT3iAkxKHqoFA=
TELEBOT_API_TOKEN=5781893081:AAHfbx1v2m-v4cA_6XLh4IbbJox6cVqzExM
TELEBOT_KNOWN_SERVICES=http://dream.deeppavlov.ai:8018/badlisted_words,http://dream.deeppavlov.ai:8006/respond
TELEBOT_KNOWN_SERVICES_NAMES=badlisted_words,spacy_nounphrases
