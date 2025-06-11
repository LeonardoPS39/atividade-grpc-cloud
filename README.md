# Projeto Final - Sistemas Distribuídos (Cesupa)

## 🧠 Objetivo

Este projeto demonstra uma aplicação distribuída simples baseada em gRPC e AWS, atendendo aos requisitos propostos na disciplina de Sistemas Distribuídos. A aplicação consiste em um servidor gRPC hospedado na nuvem (AWS EC2) e um cliente local que se comunica com ele remotamente.

---

## ⚙️ Tecnologias Utilizadas

- **AWS CloudFormation** – provisionamento da infraestrutura como código.
- **EC2 (Amazon Linux 2023)** – servidor gRPC hospedado na nuvem.
- **gRPC (Python)** – comunicação entre cliente e servidor.
- **Python 3.11** – linguagem utilizada para o backend.
- **Infrastructure as Code (IaC)** – via `stack.yaml`.

---

## 📂 Estrutura do Repositório

```
projeto-distribuida/
├── protos/
│ ├── hello.proto
│ ├── hello_pb2.py
│ └── hello_pb2_grpc.py
├── server.py
├── client.py
├── requirements.txt
└── stack.yaml
```


---

## 🚀 Como Executar Localmente

1. Instale as dependências:
	```bash
	pip install -r requirements.txt
	```

2. Rode localmente (opcional):
	```bash
	python server.py
	```

3. Rode o cliente apontando para o IP da instância EC2:
	```bash
	python client.py <IP_DA_EC2> SeuNome
	```

---

## ☁️ Como Subir na Nuvem (AWS)
- Acesse o Console AWS > CloudFormation > Create Stack.

- Faça upload do arquivo stack.yaml.

- Aguarde a criação da stack.

- O IP público da EC2 aparecerá nos Outputs.

- Rode o client.py apontando para esse IP.

---

## ✅ Requisitos atendidos
- Infraestrutura como código (CloudFormation)

- Sistema distribuído cliente-servidor

- Comunicação moderna via gRPC

- Código modularizado em Python

- Testes entre cliente local e servidor na nuvem

## 🔚 Considerações
Este projeto demonstra uma arquitetura enxuta e funcional, com possibilidade de expansão para balanceamento, escalabilidade e monitoramento no futuro.

