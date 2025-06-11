# Relatório Técnico – Projeto Final de Sistemas Distribuídos (Cesupa)

## 1. Introdução
Este trabalho explora sistemas distribuídos, IaC e gRPC. Implementamos uma arquitetura cliente-servidor onde o servidor gRPC roda em uma instância EC2 (Ubuntu 22.04) provisionada via AWS CloudFormation.

## 2. Arquitetura Proposta
```
[ client.py (local) ] --> Internet --> [ EC2 (server.py, porta 50051) ]
```
- **protos/**: definições `.proto` e código gerado.
- **server.py**: implementação do serviço gRPC.
- **client.py**: stub e chamada remota.
- **stack.yaml**: template CloudFormation para EC2.

## 3. Justificativa Tecnológica
| Tema                     | Tecnologia                   | Justificativa                                                         |
|--------------------------|------------------------------|------------------------------------------------------------------------|
| IaC                      | AWS CloudFormation           | Nativo AWS, sem dependência de terceiros                               |
| Comunicação              | gRPC (HTTP/2)                | RPC de alto desempenho, fácil geração de código                        |
| Conexões Concorrentes    | ThreadPoolExecutor (gRPC)    | Gerencia múltiplas requisições simultâneas com baixo overhead           |

## 4. Infraestrutura como Código
O `stack.yaml`:
```yaml
ImageId: !Sub "{{resolve:ssm:/aws/service/canonical/ubuntu/server/22.04/stable/current/amd64/hvm/ebs-gp2/ami-id}}"
UserData:
  Fn::Base64: !Sub |
    #!/bin/bash
    set -xe
    apt-get update -y
    apt-get install -y python3 python3-pip git
    cd /home/ubuntu
    git clone ${RepositoryUrl} app
    cd app
    pip3 install -r requirements.txt
    python3 -m grpc_tools.protoc -I=protos --python_out=protos --grpc_python_out=protos protos/hello.proto
    nohup python3 server.py > server.log 2>&1 &
    chown -R ubuntu:ubuntu /home/ubuntu/app
```
- Uso de `!Sub` para AMI via SSM Parameter Store.
- Geração do código Python a partir do `.proto` durante o bootstrap.

## 5. Fluxo de Comunicação
1. Cliente envia `Mensagem(nome)` via stub.
2. Servidor processa e retorna `Resposta(texto)`.

## 6. Concorrência e Escalabilidade
- `max_workers=10` no `ThreadPoolExecutor` suporta múltiplas conexões.
- Pode ajustar conforme carga ou adicionar Auto Scaling Groups.

## 7. Testes Realizados
- **Conexão remota**: `python3 client.py <IP> Teste` → `Olá, Teste!`
- **Concorrência**: script Bash simulando 50 chamadas simultâneas.
- **Logs**: verificação de `server.log` no EC2.

## 8. Considerações Finais
- Arquitetura simples e modular.
- Próximos passos: Load Balancer, CI/CD (CodePipeline), CloudWatch Alerts.

## 9. Referencial
- Utilizamos o ChatGPT o4-mini-high como ferramenta de auxilio no projeto, corrigindo erros e indicando sugestões de melhorias.
