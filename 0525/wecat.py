import itchat

# itchat.auto_login()
# itchat.send("hello,world", toUserName='filehelper')
@itchat.msg_register(itchat.content.TEXT)
def text_replay(msg):
    return  msg.text

itchat.auto_login()
itchat.run()