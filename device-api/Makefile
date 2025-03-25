.PHONY: python
python:
	python3 -m pip install -r requirements.txt
	python3 -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. device.proto
