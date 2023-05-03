
cd keras-io/guides/gke/text2img/

docker build -t myimage .
docker tag myimage us-central1-docker.pkg.dev/ayaps-poc/docker-test/txt2img:latest
docker push us-central1-docker.pkg.dev/ayaps-poc/docker-test/txt2img:latest

gcloud auth configure-docker us-central1-docker.pkg.dev

docker pull us-central1-docker.pkg.dev/ayaps-poc/docker-test/txt2img:latest

docker run -d -p 80:8080 us-central1-docker.pkg.dev/ayaps-poc/docker-test/txt2img:latest

wget https://github.com/openai/CLIP/blob/main/clip/bpe_simple_vocab_16e6.txt.gz
wget https://huggingface.co/fchollet/stable-diffusion/resolve/main/kcv_encoder.h5
wget https://huggingface.co/fchollet/stable-diffusion/resolve/main/kcv_diffusion_model.h5
wget https://huggingface.co/fchollet/stable-diffusion/resolve/main/kcv_decoder.h5

docker run -d -p 80:8080 -v /home/ayaps/localkeras:/root/.keras/datasets us-central1-docker.pkg.dev/ayaps-poc/docker-test/txt2img:latest

kubectl apply -f deployment.yaml