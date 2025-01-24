import http.client
import json

conn = http.client.HTTPSConnection("d9edjv.api.infobip.com")
payload = json.dumps({
    "messages": [
        {
            "destinations": [{"to":"916383579334"}],
            "from": "447491163443",
            "text": "Congratulations on sending your first message. Go ahead and check the delivery report in the next step."
        }
    ]
})
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
conn.request("POST", "/sms/2/text/advanced", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))