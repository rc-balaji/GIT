import http.client
import json

conn = http.client.HTTPSConnection("d9edjv.api.infobip.com")
payload = json.dumps(
    {
        "messages": [
            {
                "from": "447860099299",
                "to": "916383579334",
                "messageId": "841090f7-7eab-4b46-948d-1302fbbff8e6",
                "content": {
                    "templateName": "test_whatsapp_template_en",
                    "templateData": {"body": {"placeholders": ["RC"]}},
                    "language": "en",
                },
            }
        ]
    }
)
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
conn.request("POST", "/whatsapp/1/message/template", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
