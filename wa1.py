import http.client
import json

conn = http.client.HTTPSConnection("d9edjv.api.infobip.com")

payload = json.dumps(
    {
        "messages": [
            {
                "from": "447860099299",  # Replace with your registered WhatsApp number
                "to": "916383579334",  # Recipient's number in international format
                "content": {
                    "templateName": "simple_text_message",  # Use your template name
                    "templateData": {
                        "body": {
                            "placeholders": ["Good Morning! This is a simple message."]
                        }
                    },
                    "language": "en",
                },
            }
        ]
    }
)

}

conn.request("POST", "/whatsapp/1/message/template", payload, headers)

res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
