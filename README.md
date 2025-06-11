# Projeto Final - Sistemas Distribuídos (Cesupa)

## 🧠 Objetivo
Este projeto demonstra uma aplicação distribuída simples baseada em gRPC e AWS, atendendo aos requisitos da disciplina de Sistemas Distribuídos. A aplicação consiste em um servidor gRPC na nuvem (AWS EC2) e um cliente local que se comunica remotamente.

## ⚙️ Tecnologias Utilizadas
- **AWS CloudFormation** – Provisionamento de infraestrutura como código.
- **EC2 (Ubuntu 22.04)** – Servidor gRPC hospedado na nuvem.
- **gRPC (Python)** – Comunicação cliente-servidor eficiente.
- **Python 3.11** – Linguagem de programação.

## 📂 Estrutura do Repositório
```
atividade-grpc-cloud/
├── protos/
│   ├── __init__.py
│   ├── hello.proto
│   ├── hello_pb2.py        # Gerado pelo protoc (comitado ou gerado em deploy)
│   └── hello_pb2_grpc.py    # Gerado pelo protoc
├── server.py
├── client.py
├── requirements.txt
└── stack.yaml               # Template CloudFormation
```

## 🚀 Como Executar Localmente
1. **Clone e instale dependências**:
   ```bash
   git clone <URL-do-repositório>
   cd atividade-grpc-cloud
   pip3 install --upgrade pip
   pip3 install -r requirements.txt
   ```
2. **(Opcional) Gere os módulos gRPC** caso não estejam comitados:
   ```bash
   python3 -m grpc_tools.protoc -I=protos \
     --python_out=protos --grpc_python_out=protos \
     protos/hello.proto
   ```
3. **Configure o PYTHONPATH** para que o pacote \`protos\` seja encontrado:
   ```bash
   export PYTHONPATH=.
   ```
4. **Inicie o servidor** (escutando em 0.0.0.0:50051):
   ```bash
   python3 server.py
   ```
5. **Execute o cliente**, passando o IP (ou hostname) do servidor e seu nome:
   ```bash
   python3 client.py <IP_DA_EC2> SeuNome
   ```

## ☁️ Subindo na Nuvem (AWS)
1. Acesse o Console AWS > CloudFormation > Create Stack.
2. Faça upload do arquivo **stack.yaml**.
3. Aguarde a criação da stack (pode levar até 2 minutos para o UserData concluir).
4. No Outputs do Stack, copie o **PublicIP** da instância EC2.
5. Rode o cliente local usando esse IP.

## ✅ Checklist Final
- [ ] `protos/__init__.py` presente.
- [ ] Deploy finalizou sem erros no CloudFormation.
- [ ] Porta 50051 liberada no Security Group.
- [ ] Servidor escutando em `0.0.0.0`.
- [ ] Teste de conexão com `telnet <IP> 50051` OK.
+
