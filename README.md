First of all from what we need to start - import library!

`import pbot`

Now we can initialize Dialog!

`dialog = pbot.Dialog(dialogId, name)`

dialogId is unique id from which bot will identify that you - it's you. It can be any string variable.
name is a name of user. In some moments bot can say this name to you.
Dialog class contains system functions of library. But firstly let`s look at sendMessage method!

`response = dialog.sendMessage("hello")`

In argument of this function may be any string variable. It will be your message to bot!

Response contains string variable with answer from bot.

A litle example (see in repository example.py):

![kek](https://i.imgur.com/ZlFN7vd.png)
