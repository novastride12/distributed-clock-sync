import hmac
import hashlib
import json

SECRET_KEY = b"clock_sync_secret"

def generate_hmac(data):
    message = json.dumps(data).encode()
    signature = hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()
    return signature


def verify_hmac(data, received_signature):
    message = json.dumps(data).encode()
    expected_signature = hmac.new(SECRET_KEY, message, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_signature, received_signature)