docker build -t calcom .
docker login
docker tag calcom pycalcx/calcom
docker push pycalcx/calcom
aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/l7l3b6y2
docker build -t calcom .
docker tag calcom:latest public.ecr.aws/l7l3b6y2/calcom:latest
docker push public.ecr.aws/l7l3b6y2/calcom:latest