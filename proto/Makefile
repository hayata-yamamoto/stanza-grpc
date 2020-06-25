default: | help

SHELL=/bin/bash

compile: 
	protoc -I=. --python_out=../src/pb2 --grpc_out=../src/pb2 \
		health.proto stanza.proto