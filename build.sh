docker build -t calcom .
docker login
docker tag calcom pycalcx/calcom
docker push pycalcx/calcom