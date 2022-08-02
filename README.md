# huggingface-sentiment-analysis
Sentiment Analysis API Server with Huggingface and FastAPI.

### How to setup the project(For dev)
1. Install requirements
```shell
pip install -r requirements-dev.txt
```

2. Install pre-commit
```shell
pre-commit install
```


### How to run server
1. Build Docker image
```shell
docker build -t <YOUR IMAGE NAME> .
```

2. Run FastAPI Server
```shell
docker run -it -p 8000:8000 <YOUR IMAGE NAME>
```

### Test Examples
Health check
```shell
$ curl http://localhost:8000/healthz
"healthy"
```
Sentiment Analysis
```shell
$ curl --request POST "http://localhost:8000/analysis" --header "Content-Type: application/json" --data-raw '{"text": "hello"}'
{
  "text": "hello",
  "label": "neural",
  "scores": [
    0.08270365744829178,
    0.5090620517730713,
    0.40823420882225037
   ]
}
```
