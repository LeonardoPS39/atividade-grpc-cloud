# Relatório Técnico – Projeto Final de Sistemas Distribuídos

## 1. Introdução

O objetivo do projeto é aplicar conceitos de sistemas distribuídos utilizando tecnologias modernas de comunicação (gRPC) e provisionamento de infraestrutura como código (AWS CloudFormation). A arquitetura implementada segue o modelo cliente-servidor, com o servidor hospedado na nuvem AWS e o cliente executando localmente.

---

## 2. Arquitetura Proposta

### Componentes:

- **Servidor gRPC**: hospedado em uma instância EC2 (Amazon Linux 2023).
- **Cliente gRPC**: roda localmente na máquina do aluno.
- **Comunicação**: via protocolo gRPC (HTTP/2 sobre TCP).
- **Provisionamento**: automatizado com CloudFormation (`stack.yaml`).

### Diagrama:

	```
	[ client.py (local) ] --> Internet --> [ EC2 (server.py, porta 50051) ]
	```


---

## 3. Justificativa das Escolhas Tecnológicas

| Tema                          | Tecnologia Usada          | Justificativa                                                  |
|-------------------------------|----------------------------|----------------------------------------------------------------|
| Infraestrutura como Código    | AWS CloudFormation         | Evita complexidade do Terraform e funciona direto na AWS Lab   |
| Comunicação moderna           | gRPC com Python            | Simples de usar, eficiente, concorrente e baseado em HTTP/2    |
| Middleware / Sockets          | gRPC                       | Substitui sockets puros e message brokers com RPC estruturado  |
| Concorrência/Paralelismo      | ThreadPoolExecutor (gRPC)  | Permite múltiplas conexões simultâneas com baixo esforço       |

---

## 4. Infraestrutura como Código (CloudFormation)

A infraestrutura foi definida em um único arquivo `stack.yaml`, que:

- Cria uma instância EC2
- Configura o Security Group (porta 50051 aberta)
- Instala Python, pip, git, e dependências via `UserData`
- Clona o repositório GitHub e inicia o servidor

Trecho do `UserData`:
```bash
dnf install -y python3 python3-pip git
git clone https://github.com/tulipin/projeto-distribuida.git
pip3 install grpcio grpcio-tools
python3 server.py > server.log 2>&1 &
```

## 5. Comunicação entre Componentes
A comunicação é feita via gRPC, conforme o .proto:

```proto
service SaudacaoService {
  rpc Saudar (Mensagem) returns (Resposta);
}
```

Fluxo:

1. Cliente envia Mensagem(nome="Leonardo")

2. Servidor responde Resposta(texto="Olá, Leonardo!")

---

## 6. Escalabilidade e Concorrência
O servidor gRPC utiliza:

```python
grpc.server(futures.ThreadPoolExecutor(max_workers=10))
```

Isso permite o atendimento simultâneo de múltiplos clientes com threads independentes, sem bloqueios.

--- 

## 7. Testes Realizados
- Cliente executado localmente acessando IP da EC2

- Respostas recebidas com sucesso

- Logs verificados no servidor via server.log

- Teste com nomes variados simulando chamadas concorrentes

---

## 8. Considerações Finais
O projeto atingiu todos os objetivos principais de forma funcional e direta. A arquitetura é simples, eficiente e extensível. Melhorias possíveis:

- Adicionar balanceamento com Load Balancer

- Rodar o cliente como outro serviço em EC2

- Automatizar testes com script

- Adicionar monitoramento com CloudWatch

9. Requisitos Atendidos
- ✅ Arquitetura de Nuvem (EC2, SG, CloudFormation)

- ✅ Provisionamento automatizado

- ✅ Comunicação com gRPC

- ✅ Concorrência no servidor

- ✅ Testes e validação local-remoto