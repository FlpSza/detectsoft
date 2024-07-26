from pushbullet import Pushbullet

# Substitua 'API_KEY' pela sua chave de API do Pushbullet
pb = Pushbullet("o.rX2ObkoFodCdSf89gQ6V8qq2mFQOTaqK")

def send_notification(title, body):
    pb.push_note(title, body)
