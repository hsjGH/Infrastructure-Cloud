#!/bin/bash

# Lab: Run containers experiment
# Doel: leren starten, stoppen, inspecteren en verbinden van containers

# Stap 1: Maak werkdirectory voor experiment
echo "Stap 1: Maak lab map"
mkdir -p lab_run_containers
cd lab_run_containers || exit 1

# Stap 2: Creëer een simpele Dockerfile voor een kleine container (alpine)
echo "Stap 2: Creëer Dockerfile voor Alpine container"
cat << 'EOF' > Dockerfile.alpine
# Gebruik kleine Alpine Linux image
FROM alpine:3.18
# Voeg een commando toe dat de container actief houdt
CMD ["sh", "-c", "while true; do echo 'Container loopt'; sleep 5; done"]
EOF

# Stap 3: Bouw Docker image
echo "Stap 3: Bouw Docker image"
docker build -t runlab_alpine -f Dockerfile.alpine .

# Stap 4: Start meerdere containers
echo "Stap 4: Start 3 containers van dezelfde image"
docker run -d --name container1 runlab_alpine
docker run -d --name container2 runlab_alpine
docker run -d --name container3 runlab_alpine

# Stap 5: Toon alle actieve containers
echo "Stap 5: Toon actieve containers"
docker ps -a

# Stap 6: Inspecteer container details
echo "Stap 6: Inspecteer container1"
docker inspect container1

# Stap 7: Verbinden met container via bash
echo "Stap 7: Open shell in container1"
docker exec -it container1 sh

# (op dit punt kun je in de container dingen uitvoeren, type 'exit' om te verlaten)

# Stap 8: Stop containers
echo "Stap 8: Stop alle containers"
docker stop container1 container2 container3

# Stap 9: Verwijder containers
echo "Stap 9: Verwijder containers"
docker rm container1 container2 container3

# Stap 10: Optioneel: verwijder image
# echo "Verwijder image runlab_alpine"
# docker rmi runlab_alpine

echo "Experiment klaar!"
