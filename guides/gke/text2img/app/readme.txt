
cd keras-io/guides/gke/text2img/

docker build -t myimage .
docker tag myimage us-central1-docker.pkg.dev/ayaps-poc/docker-test/txt2img:latest
 docker push us-central1-docker.pkg.dev/ayaps-poc/docker-test/txt2img:latest

docker pull us-central1-docker.pkg.dev/ayaps-poc/docker-test/txt2img:latest


gcloud auth configure-docker us-central1-docker.pkg.dev


kubectl apply -f deployment.yaml