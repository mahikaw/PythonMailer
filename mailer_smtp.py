from marrow.mailer import Mailer, Message,logger
import logging
mailer_config = {
            'transport': {
                'use': 'smtp',
                'host': 'smtp.gmail.com',
                'username': '<xyz>@gmail.com',
                'password': '<password>',
                'port': '587',
            }
        }
payload = {
            'to': '<recepient>@<domain>.com',
            'from': '<xyz>@gmail.com',
            'subject': '<your subject>',
            'message': '<email body>',
            'attachment': '<path to attachment>',
            'tls': 'tls',
        }
logging.basicConfig(level=logging.INFO)
mailer = Mailer(mailer_config)
mailer.start()
message = Message(author=payload['from'], to=payload['to'])
message.attach('/Users/tgit/Desktop/mail.py', data=None,maintype=None, subtype=None, inline=False)
message.subject = payload['subject']
message.plain = "<message>"
mailer.send(message)
mailer.stop()