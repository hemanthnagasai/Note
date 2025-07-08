# notes/utils.py

import requests

def send_emailjs_reminder(user_email, user_name):
    service_id = 'service_iqc9bfa'
    template_id = 'template_qhmegoo'
    public_key = 'aBn1OF--ERQU4zQFh'

    payload = {
        "service_id": service_id,
        "template_id": template_id,
        "user_id": public_key,
        "template_params": {
            "user_email": user_email,
            "user_name": user_name
        }
    }

    response = requests.post('https://api.emailjs.com/api/v1.0/email/send', json=payload)
    return response.status_code == 200
