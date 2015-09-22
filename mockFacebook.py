import json

def mockFriends():
   print json.dumps({
  "data": [
    {
      "name": "Robby Peters",
      "id": "10152008625831835"
    },
    {
      "name": "Eliot Mestre",
      "id": "645316989"
    },
    {
      "name": "Mark Pero",
      "id": "1053218584"
    },
    {
      "name": "Dominic Albertoni",
      "id": "1663833995"
    },
    {
      "name": "TJ Reed",
      "id": "100000869799557"
    },
    {
      "name": "Robert Long",
      "id": "100004021068837"
    }
  ],
  "paging": {
    "next": "https://graph.facebook.com/v2.4/10204597002818058/friends?format=json&access_token=CAACEdEose0cBAIuM03q9tq8PZCFTfRhWmbqCJ2dsIIRZAlk7kCetgbtMr6LTQbOhWNGKLYo3rcp84LDAyBwUFrTUDPH9qdVLFAIaPwLCefG1yTHTUig7ZAuZBZB8YZBzerbpCrSAGRSZBidc9mOhbs3eNZBwrr5JDpU5citkII8sVsumBbdWzZBnkiumhnmPls8ZCDzHDvMI6U2x624tLIQnQ3&limit=25&offset=25&__after_id=enc_AdDEDc16Sju5ImU4K5cUVIZCj8hPBKbZAHkaBt8wLa9NOBACazTGwmbNF4JPnlgq6PownSm2ZAwdVFHkzAyyZCYHosnE"
  },
  "summary": {
    "total_count": 1274
  },
})
