API_KEY="cisco|7tUq72zasT4sSYQNjrM5GO0KPe0n3SDPeQ6TcnXRAJU"
ID="1"

curl -X PUT "http://library.demo.local/api/v1/books/$ID" \
  -H "accept: application/json" \
  -H "X-API-KEY: $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{ \"id\": 0, \"title\": \"string\", \"author\": \"string\" }"