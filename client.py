import grpc
import sys
from protos import hello_pb2
from protos import hello_pb2_grpc

def run(server_ip="localhost", nome="Aluno"):
    with grpc.insecure_channel(f"{server_ip}:50051") as channel:
        stub = hello_pb2_grpc.SaudacaoServiceStub(channel)
        resposta = stub.Saudar(hello_pb2.Mensagem(nome=nome))
        print("Resposta do servidor:", resposta.texto)

if __name__ == '__main__':
    ip = sys.argv[1] if len(sys.argv) > 1 else "localhost"
    nome = sys.argv[2] if len(sys.argv) > 2 else "Aluno"
    run(ip, nome)
