#!/bin/bash

APP_NAME="flask-signup-app"
NUM_CONTAINERS=2
BASE_PORT=5000
DB_FILE="$(pwd)/user.db"  # pad naar bestaande database

# 1. Maak requirements.txt en html templates 
cat <<EOL > requirements.txt
Flask==2.3.3
EOL

mkdir -p templates
cat <<EOL > templates/signup.html
<form method="POST" action="/signup/v2">
  <input name="username">
  <input name="password" type="password">
  <button>Submit</button>
</form>
EOL

# 2. Maak Dockerfile
cat <<'EOL' > Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "flask_app_signup.py"]
EOL

# 3. Build docker image
docker build -t $APP_NAME .

# 4. Run meerdere containers met bestaande user.db
for ((i=0; i<NUM_CONTAINERS; i++))
do
    PORT=$((BASE_PORT + i))
    CONTAINER_NAME="${APP_NAME}_$PORT"
    echo "Starting container $CONTAINER_NAME on port $PORT"
    docker run -t -d --name $CONTAINER_NAME \
        -p $PORT:5000 \
        -v "$(pwd)":/app \
        $APP_NAME
done

echo "Done. Containers running on ports $BASE_PORT to $((BASE_PORT + NUM_CONTAINERS - 1)) using existing user.db"
