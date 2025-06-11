# -*- coding: utf-8 -*-

from concurrent import futures
import grpc
from protos import hello_pb2
from protos import hello_pb2_grpc
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

class SaudacaoService(hello_pb2_grpc.SaudacaoServiceServicer):
    def Saudar(self, request, context):
        texto = f"Ola, {request.nome}"
        return hello_pb2.Resposta(texto=texto)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_SaudacaoServiceServicer_to_server(SaudacaoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC rodando na porta 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
