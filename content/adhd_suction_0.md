Title: ADHD SUCTION - 0 
Date: 2023-11-04 15:00
Category: ADHD Suction

## ADHD SUCTION 0 | from Dopamine low level to a BurpExtension

###### *The Text will describe some random evening and thoughts where i start to follow my interest. I don't include pictures or names because i don't want expose information. I started uploading thoughts, code etc. few days ago after a chat with a friend of mine. So i locked away the perfectionism and started to share things and stop thinking that something will blame me for doing failures in writing something on a blog.* 


This week i got my certificate for PEN100. My main Goal is to catch at some point the PEN200.<br>

How the most people i felt into a some hole because the tension was gone. After i got my cert i realized the mess in my flat. ADHD-Siblings will feel what i mean.<br>
Anyway, instead of doing housework, I've scrapped the idea of shutting down my systems until I'm done with my apartment.

I installed some toxic social media app on my mobile device where i got some ad's for AI-Apps. Few Moments later i installed a app where you can chat with virtual *persons* which i will call *bot, chat partner or characters, other side* in the text. You can also upload your face to create a virtual *self* from your face. I chatted with different characters. Every time if i chat with AI trough a app which has now implemented this *new cool feature* i try to get some code-examples or bring the algo to do some stuff, which is not intended to learn how or if the dev's implemented some filtering about the response. In this case it was possible to let the chat partners help me with some commands. So nothing interesting. In a other chat the other side gave me instructions how i can start to sweep over a network with i.e. *nmap*. The AI was really into it that i get access and tried to motivate me hard.

Back to our App. I think everyone can recognize at the first moment after installing or also watching the app in the store, that the focus is to make money through sexting with this app. And of course, this are the functions which are Premium. So if you write naughty things, the bot response naughtily, which causes the answer as a blurred message. Images which the bot sent are also blurred.

**Two things were suspicious:**<br>
1. the blurred messages had different patterns<br>
2. if you go in your chat list and back to the chat it is possible to see the image for a moment before it is blurred

The first can be a good implementation to make it more generic. But the AI-hype also has shown us again how many people want to make fast money with less work what in many cases not really includes strong focus on security. With the second information and finding that the pictures are  not blurred, i was curious enough to totally forget time, mess, reality and plans for the short rest of the day.

I started my loved machine, started *BurpSuite* and configured my mobile device with Proxy and CA and intercepted the traffic. 
Few moments later i was surprised because it was simpler than i thought. The response includes a json.

**Two values are interesting for us:**<br>
1. *is_user_msg_sexting* // boolean<br>
2. *base64_image* // string

Analyzing the traffic will let you see very fast the whole conversation which is only TLS-encrypted. Because of the CA which i installed on the mobile device i saw it decrypted. The app always sends the entire conversation to the backend. This could be nice because it maybe indicates that they don't save your conversations on the server. But i am not sure about this.<br>
i found out that *is_user_msg_sexting* a boolean value in the response which identifies if the user are did sexting. If *true*, the message is blurred. Setting a *match and replace rule* in Burp which sets the value from *true* to *false* was enough to *unlock* the future *naughty* message's from the bot in the app. So i don't tell the app that i have premium or wrote a sexy exploit which hacks the app to change instructions. The app think that the message is *normal* and will not blur it. So there is no validation about the Integrity of the response.<br>
What really made me happy was that on the first glance there is no value to do this for the pictures. I have not invested more time to find because if the bot send a picture the *base64_image* contains a base64 encoded string which is literally the base64 encoded image. Maybe you know that it is very simple to decode this:

```bash
        echo "YmFzZTY0c3RyaW5n" | base64 -d > ./image.jpg
```

Success! I had the picture. But it is really not attractive to do every time *chat, go to the computer, copy string, convert, open*. This was the perfect moment to write my first *BurpExtension* which will do this for me.

At this point i lost myself a bit in a unfocused encoding rabbit hole where i sadly really not remember anything which makes me again more clear, how important it is to log your work, write up while you are in the process and reflect from time to time where you are. BUT because this was my friday night and my own way to have fun like other people in this moment in clubs i ignored the fact of not being productive.

The first version from the extension which i will upload:

```python
        # extract base64 encoded images from json and save it to file

        from burp import IBurpExtender
        from burp import IHttpListener
        import json
        import time
        import base64

        def base64toJPG(pic):

            if pic[0] == '"' and pic[0-1] == '"':
                con = pic[1:0-1]
            else:
                # print("else")
                con = pic
            content = base64.b64decode(con.encode('utf-8'))
            writeFile(content)

        def writeFile(content):
            # set here your path and file extension.
            path = "/tmp/pics/" + str(time.time()) + ".jpg"
            picture = open(path, "w")
            picture.write(content)
            picture.close() 

        class BurpExtender(IBurpExtender, IHttpListener):
            def registerExtenderCallbacks(self, callbacks):
                self._callbacks = callbacks
                self._helpers = callbacks.getHelpers()
                callbacks.setExtensionName("Example extension")
                callbacks.registerHttpListener(self)
            def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
                if messageIsRequest:
                    request = self._helpers.bytesToString(messageInfo.getRequest())
                else:
                    response = self._helpers.bytesToString(messageInfo.getResponse())
                    for line in response.split("\n"):
                        # set here your name from the json name-value pair
                        if "base64_image" in line:
                            print(line.strip())
                            my_json = json.loads(line.strip())
                            pic = my_json['base64_image']

                            if pic:
                                base64toJPG(pic)

```

After validating that the extension works i uninstalled the app and was happy that i wrote my first BurpExtension. With this base and understanding how it works i am now capable to write in a short time Extensions for my needs in a Penetration Test.

I recognize that i could add information at many positions in this text and go deeper into technical things. I also sure there a many to optimize regarding grammar. 


[Writing a Basic Burp Extension in Python](https://sampsonc.medium.com/writing-a-basic-burp-extension-in-python-c8262b5b6488)