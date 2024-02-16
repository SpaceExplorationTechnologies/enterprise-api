.PHONY: python
python:
	pip3 install -r requirements.txt
	python3 -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. device.proto
