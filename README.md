# fraud-detector-AI-agent
## Analyzes investment offers to detect scam red flags and return a clear RED / AMBER / GREEN risk rating with supporting evidence.

## It gives you a risk assessment of an investment offer:

a rating (RED / AMBER / GREEN)

a score (numerical risk level)

the reasons why it was flagged

any evidence links from regulators or credible sources

plus a disclaimer reminding you it’s only educational, not financial advice.


cd src 
set PYTHONPATH=.


cd ..
docker build -t my-fraud-agent-app . -f ./src/Dockerfile

docker run -p 8001:8001 --env-file .env my-fraud-agent-app