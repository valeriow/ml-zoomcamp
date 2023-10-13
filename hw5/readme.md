docker build -t zoomcamp-hw5 .

docker run -it -p 9696:9696 --rm zoomcamp-hw5


docker run -it --entrypoint=bash --rm zoomcamp-hw5
