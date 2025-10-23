API_KEY="cisco|7tUq72zasT4sSYQNjrM5GO0KPe0n3SDPeQ6TcnXRAJU"
ID="111111111"
TITLE="Test"
AUTHOR="Tester"
curl -X POST "http://library.demo.local/api/v1/books" \
-H "accept: application/json" \
-H "X-API-KEY: $API_KEY" \
-H "Content-Type: application/json" \
-d "{\"id\":$ID,\"title\":\"$TITLE\",\"author\":\"$AUTHOR\"}"

