import hashlib

def getSecretData():
    with open("secrets.txt", "r") as secrets:
        info = secrets.read().split("\n")
        secretsDict = {
            'APP_SECRET_KEY': info[0],
            'EMAIL_ADDRESS': info[1],
            'EMAIL_PASSWORD': info[2],
            'PROJECT_URL': info[3]
        }
        return secretsDict

def validate():
    return 'user' and 'verified' in session

def hash( value ):
    return hashlib.sha256(value).hexdigest()
