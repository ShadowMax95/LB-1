import requests
import json
import matplotlib.pyplot as plt

reply = requests.get("https://bank.gov.ua/NBU_Exchange/exchange_site?start=20240930&end=20241006&valcode=usd&json")

reply_json = json.loads(reply.text)

output_dict = {}
for item in reply_json:
    output_dict[item['exchangedate']] = item['rate']
print(output_dict)

ax = plt.subplot()
ax.plot(output_dict.keys(), output_dict.values())
plt.show()