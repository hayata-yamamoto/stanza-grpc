# Stanza gRPC server 

## Get started

### local

```bash 
git clone https://github.com/hayata-yamamoto/stanza-grpc.git
cd stanza-grpc

# for mac 
brew upgrade 
brew install protobuf 

# poetry install 
# please follow messages after the below
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3

# if you want to make virtual env on this directory
# poetry config virtualenvs.in-project true

poetry sync

make protoc  # compile .proto 
make start-server # start grpc server
```

Open another console,

```bash 
# for mac 
brew install grpcurl

grpcurl -plaintext localhost:50051 health.Health/Check
grpcurl -plaintext -d '{"sentence": "stanza gRPC is a server of stanza"}' localhost:50051 stanza.grpc.v1.Stanza/Recognize
```


### docker

```bash 
git clone https://github.com/hayata-yamamoto/stanza-grpc.git
cd stanza-grpc

# for mac 
brew upgrade 
brew install protobuf 

make protoc
docker build -t stanza-grpc .
```


## Server features

### Endpoints

```bash 
$ grpcurl -plaintext localhost:50051 list
grpc.reflection.v1alpha.ServerReflection
health.Health
stanza.grpc.v1.Stanza
```

<details><summary>reflection describe</summary>

```bash
$ grpcurl -plaintext localhost:50051 describe 
grpc.reflection.v1alpha.ServerReflection is a service:
service ServerReflection {
  rpc ServerReflectionInfo ( stream .grpc.reflection.v1alpha.ServerReflectionRequest ) returns ( stream .grpc.reflection.v1alpha.ServerReflectionResponse );
}
health.Health is a service:
service Health {
  rpc Check ( .health.HealthCheckRequest ) returns ( .health.HealthCheckResponse ) {
    option (.google.api.http) = { get:"/health"  };
  }
  rpc Watch ( .health.HealthCheckRequest ) returns ( stream .health.HealthCheckResponse );
}
stanza.grpc.v1.Stanza is a service:
service Stanza {
  rpc Recognize ( .stanza.grpc.v1.RecognizeRequest ) returns ( .stanza.grpc.v1.RecognizeResponse ) {
    option (.google.api.http) = { get:"/v1/recognize" body:"*"  };
  }
}
```
</detail>


## TODO
- [x] enable grpc server
- [ ] enable rest api
- [ ] enable cilent tool
- [ ] deployment
