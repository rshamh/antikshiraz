from kavenegar import KavenegarAPI

api = KavenegarAPI('3775653230552F6C616D6B773748787165333146566F693842725231793539704A323245702B535A5238553D')

params = {
        'sender': '1000596446',
        'receptor' : '09177003408',
        'message' : "سلام"
    }   
response = api.sms_send(params)
print(response)