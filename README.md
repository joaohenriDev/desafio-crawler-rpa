Markdown
# 🚀 Automated Web Scraper & RPA Solution — Books to Scrape

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Docker Support](https://img.shields.io/badge/docker-enabled-blue.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

Esta é uma solução corporativa de automação de processos e mineração de dados estruturados (RPA/Web Scraper) focada na extração resiliente de catálogos de produtos da plataforma `books.toscrape.com`. O sistema foi concebido sob princípios rigorosos de arquitetura de software (SOLID), engenharia de confiabilidade (SRE) e segurança cibernética.

---

## 🎯 1. Funcionalidades de Engenharia Operacional

* **Gerenciamento de Estado de Conexão**: Utilização de pooling HTTP persistente via `requests.Session()` para otimizar o handshake TCP e mitigar overhead de rede.
* **Políticas de Resiliência (Polite Scraping)**: Headers com User-Agent rotativo realista para contornar bloqueios elementares por assinaturas de robôs e aplicação de tempos de espera dinâmicos (throttling).
* **Camada de Tratamento Antirruído (Regex)**: Higienização cirúrgica de caracteres especiais, truncamento de codificações corrompidas no Windows (`Â£`) e normalização monetária para o tipo flutuante (`float`).
* **Arquitetura Isolada de Testes**: Suite de validação sem acoplamento com a internet através de injeção de fixtures HTML estruturadas locais.

---

## 📂 2. Arquitetura do Repositório (Layout de Pastas)

O projeto adota o padrão de organização modular, isolando as responsabilidades de rede, parsing, persistência e infraestrutura:

```text
desafio-crawler-rpa/
├── .gitlab-ci.yml          # Definição e esteira do pipeline CI/CD de 4 estágios
├── docker-compose.yml      # Orquestrador local de serviços e montagem de volumes
├── Dockerfile              # Pipeline de build conteinerizado Multi-Stage
├── requirements.txt        # Manifesto de dependências rígidas da aplicação
└── src/                    # Código-fonte isolado do ecossistema
    ├── crawler/            # Camada de requisições de rede (Engine HTTP)
    │   └── static_html.py
    ├── parser/             # Camada de inteligência e interpretação estrutural
    │   └── html_parser.py
    ├── storage/            # Camada de serialização e persistência de arquivos
    │   └── file_exporter.py
    ├── tests/              # Suite de testes unitários e de integração de software
    │   └── test_parser.py
    ├── config.py           # Parametrização centralizada de variáveis operacionais
    └── main.py             # Ponto de entrada (Entrypoint) e orquestrador do fluxo
```

# 🛠️ 3. Tecnologias Utilizadas

## Backend

- Python 3.11
- Requests
- BeautifulSoup4
- Regex
- Pytest
- Flake8

---

## DevOps & Infraestrutura

- Docker
- Docker Compose
- GitLab CI/CD
- Docker-in-Docker (DinD)
- AWS ECS (simulado)

---

# ▶️ 4. Como Executar o Projeto

## 🔹 Execução Local

### Pré-requisitos

- Python 3.11+
- Pip

---

## Clonar o Repositório

```bash
git clone <URL-DO-REPOSITORIO>
cd desafio-crawler-rpa
````

---

## Criar Ambiente Virtual

### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## Executar Aplicação

```bash
python -m src.main
```

Os arquivos serão exportados automaticamente para:

```text
./output
```

---

## Executar Testes

```bash
pytest -v
```

---

# 🐳 5. Execução com Docker

## Build da Imagem

```bash
docker build -t desafio-crawler .
```

---

## Executar Container

### Linux/macOS

```bash
docker run --rm -v "$(pwd)/output:/app/output" desafio-crawler
```

### Windows PowerShell

```powershell
docker run --rm -v "${PWD}/output:/app/output" desafio-crawler
```

---

# 📊 6. Estrutura dos Dados

Os dados são exportados simultaneamente em:

* JSON
* CSV

Com codificação:

```text
UTF-8
```

---

## Exemplo JSON

```json
[
  {
    "title": "A Light in the Attic",
    "price_gbp": 51.77,
    "in_stock": true,
    "rating": 3
  }
]
```

---

# 🧩 7. Schema dos Dados

| Campo     | Tipo    | Descrição                  |
| --------- | ------- | -------------------------- |
| title     | string  | Título completo do livro   |
| price_gbp | float   | Preço monetário tratado    |
| in_stock  | boolean | Disponibilidade em estoque |
| rating    | integer | Avaliação de 1 a 5         |

---

# ⛓️ 8. Pipeline CI/CD

O pipeline foi estruturado em quatro estágios principais:

```text
[Lint] → [Test] → [Build] → [Deploy]
```

---

## ✅ Lint

Validação de:

* PEP8
* qualidade de código
* padronização

Ferramenta utilizada:

```bash
flake8
```

---

## 🧪 Test

Execução automatizada com:

```bash
pytest
```

Garantindo:

* integridade
* previsibilidade
* estabilidade

---

## 🐳 Build

Responsável por:

* autenticação no GitLab Registry
* build da imagem Docker
* push automatizado

---

## 🚀 Deploy

Simulação de deploy contínuo no AWS ECS.

Execução restrita à branch:

```bash
main
```

---

# 🧠 9. Decisões Técnicas e Arquitetura

## SOLID

Aplicação de princípios como:

* responsabilidade única
* desacoplamento
* abstração reutilizável

---

## Segurança

* containers sem root
* isolamento de execução
* login seguro no registry

---

## Performance

* Session pooling
* cache de dependências
* otimização de requests HTTP

---

# 🤖 10. Uso de Inteligência Artificial

A IA foi utilizada como ferramenta de apoio técnico para:

* refinamento arquitetural
* geração de boilerplates
* regex
* debugging
* estruturação do CI/CD

Todas as implementações foram revisadas e refinadas manualmente para adequação às exigências técnicas do projeto.

---

# 🔮 11. Roadmap e Melhorias Futuras

## Browser Automation

* Selenium
* Playwright

---

## Observabilidade

* Prometheus
* Grafana
* métricas customizadas

---

## Persistência

* PostgreSQL
* MongoDB

---

## Cloud & Infra

* Terraform
* Kubernetes
* ECS real
* Helm Charts

---

# 📌 12. Possíveis Evoluções

* Retry automático
* Proxy rotation
* Rate limiting
* Logs distribuídos
* Mensageria com RabbitMQ
* Dead Letter Queue
* Feature Flags

---

# 👨‍💻 Autor

Desenvolvido por **João Henrique de Oliveira** como solução para o desafio técnico de automação, scraping e engenharia de software.

* **LinkedIn:** [linkedin.com/in/joão-henrique-de-oliveira-dev](https://www.linkedin.com/in/jo%C3%A3o-henrique-de-oliveira-dev/)
* **GitHub:** [github.com/joaohenriDev](https://github.com/joaohenriDev)
* **E-mail:** joaohenri293@gmail.com

---
