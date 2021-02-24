import pbot

dialog = pbot.Dialog('User777', 'MrCreepTon')

while True:
    v = input('You: ')
    print('Bot: ' + dialog.sendMessage(v))