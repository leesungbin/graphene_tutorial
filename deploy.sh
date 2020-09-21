docker-compose build && \
docker-compose push && \
gcloud --project=custom-dominion-289913 run deploy test --image gcr.io/custom-dominion-289913/test --platform managed --region asia-northeast1