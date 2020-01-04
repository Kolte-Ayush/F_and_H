import urllib.request
import urllib.parse
import random

class Otp_validate:
    def __init__(self):
        self.api_key = ''

    def send_sms(self, numbers, sender, message):
        data = urllib.parse.urlencode({'apikey': self.api_key, 'numbers': numbers,
                                       'message': message, 'sender': sender})
        data = data.encode('utf-8')
        request = urllib.request.Request("https://api.textlocal.in/send/?")
        f = urllib.request.urlopen(request, data)
        fr = f.read()
        return fr

    def send_otp(self, numbers, sender, message):
        otp = random.randrange(111111, 999999)
        otp_res = self.send_otp()
        if otp_res == '':
            pass
        else

    def check_sms_status(self, responce):
        pass
#     check otp responce and return true false based on the responce.



