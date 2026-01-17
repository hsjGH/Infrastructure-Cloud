#!/bin/bash

# DM1 – Docker Management Experiment
# Doel: leren inspecteren, logs bekijken, netwerken beheren, en cleanup uitvoeren

echo "Stap 1: Maak tijdelijke werkdirectory"
mkdir -p lab_dm1
cd lab_dm1 || exit 1

echo "Stap 2: Creëer een eenvoudige Dockerfile (Alpine) voor experiment"
cat << 'EOF' > Dockerfile.alpine
FROM alpine:3.18
# Container blijft actief en print elke 3 seconden
CMD ["sh", "-c", "while true; do echo 'DM1 Container actief'; sleep 3; done"]
EOF

echo "Stap 3: Bouw Docker image"
docker build -t dm1_image -f Dockerfile.alpine .

echo "Stap 4: Start meerdere containers"
docker run -d --name dm1_cont1 dm1_image
docker run -d --name dm1_cont2 dm1_image
docker run -d --name dm1_cont3 dm1_image

echo "Stap 5: Bekijk alle actieve containers"
docker ps -a

echo "Stap 6: Inspecteer een container en network details"
docker inspect dm1_cont1

echo "Stap 7: Bekijk logs van een container (laatste 10 regels)"
docker logs --tail 10 dm1_cont1

echo "Stap 8: Open shell in een container om interactief te kijken"
echo "Tip: type 'exit' om terug te gaan"
docker exec -it dm1_cont1 sh

echo "Stap 9: Maak een custom network aan"
docker network create dm1_net

echo "Stap 10: Verbind containers met het network"
docker network connect dm1_net dm1_cont1
docker network connect dm1_net dm1_cont2

echo "Stap 11: Inspecteer het netwerk"
docker network inspect dm1_net

echo "Stap 12: Test ping tussen containers binnen network"
docker exec dm1_cont1 ping -c 2 dm1_cont2

echo "Stap 13: Stop en verwijder containers"
docker stop dm1_cont1 dm1_cont2 dm1_cont3
docker rm dm1_cont1 dm1_cont2 dm1_cont3

echo "Stap 14: Verwijder network en image"
docker network rm dm1_net
docker rmi dm1_image

echo "DM1 Experiment klaar!"
