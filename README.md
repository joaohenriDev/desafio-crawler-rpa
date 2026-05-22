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

### 🔹 Execução Local Nativa
#### Pré-requisitos
Python 3.11+

Pip

1. Clonar o Repositório
   
Bash
```bash
git clone https://github.com/joaohenriDev/desafio-crawler-rpa.git
cd desafio-crawler-rpa
```

2. Criar e Ativar Ambiente Virtual
Windows (PowerShell):

PowerShell
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

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

# 🐳 5. Execução Conteinerizada (Docker)
Opção Recomendada (via Docker Compose)
Para construir a imagem, gerenciar volumes e rodar a aplicação inteira com um único comando:

Bash
docker compose up --build
Opção Alternativa (via Docker CLI)
Caso prefira rodar os comandos de forma manual e individual:

Bash
# Build da imagem local
docker build -t desafio-crawler .

# Execução no Linux/macOS
docker run --rm -v "$(pwd)/output:/app/output" desafio-crawler

# Execução no Windows (PowerShell)
docker run --rm -v "${PWD}/output:/app/output" desafio-crawler

---

# 📊 6. Estrutura e Amostra dos Dados
Os dados são exportados simultaneamente em arquivos JSON e CSV com codificação universal UTF-8 para a pasta ./output.

Exemplo de Saída Estruturada (JSON)
JSON
[
  {
    "title": "A Light in the Attic",
    "price_gbp": 51.77,
    "in_stock": true,
    "rating": 3
  }
]
---

# 🧩 7. Schema dos Dados

| Campo     | Tipo    | Descrição                  |
| --------- | ------- | -------------------------- |
| title     | string  | Título completo do livro   |
| price_gbp | float   | Preço monetário tratado    |
| in_stock  | boolean | Disponibilidade em estoque |
| rating    | integer | Avaliação de 1 a 5         |

---

# ⛓️ 8. Pipeline CI/CD (.gitlab-ci.yml)
A esteira automatizada executa as validações corporativas divididas em quatro estágios em ambientes isolados:

Plaintext
[Lint] ──► [Test] ──► [Build] ──► [Deploy]
✅ Lint (flake8): Valida conformidade estrutural com as boas práticas da PEP8 e qualidade de escrita.

🧪 Test (pytest): Executa os testes de unidade usando injeção de fixtures de texto locais para testar a inteligência do parser sem dependência da rede.

🐳 Build (dind): Realiza o login criptografado no container registry do GitLab, constrói a imagem e realiza o upload seguro.

🚀 Deploy (main branch): Simulação controlada de atualização de infraestrutura contínua na nuvem AWS ECS.
---

# 🧠 9. Decisões Técnicas e Arquitetura
SOLID: Divisão modular estrita onde as camadas de rede, extração e persistência são completamente independentes (Single Responsibility Principle).

Segurança: Dockerfile configurado sob a política de privilégios mínimos utilizando usuário worker sem privilégios administrativos de root.

Performance: Reutilização de conexões e sockets abertos via Session pooling, mitigando latência em requisições consecutivas.

---

# 🤖 10. Uso de Inteligência Artificial
A Inteligência Artificial atuou estritamente como co-piloto técnico no processo de desenvolvimento para:

Refinamento arquitetural e mapeamento inicial de estruturas.

Geração veloz de arquivos de mock (boilerplates HTML) para testes robustos.

Estruturação inicial da árvore de jobs do arquivo do GitLab CI/CD.

Todas as implementações geradas foram auditadas, refinadas e reestruturadas manualmente para conformidade com as regras do edital.

---

# 🔮 11. Roadmap e Evoluções Futuras
Browser Automation
Integração do Playwright ou Selenium em modo Headless caso o alvo mude sua renderização para componentes assíncronos dinâmicos em JavaScript.

Observabilidade
Implementação do prometheus_client para expor volumetria de raspagem, tempo de resposta do servidor e métricas de erros HTTP.

Persistência
Substituição dos arquivos locais por uma conexão transacional de banco de dados estruturado (PostgreSQL) ou NoSQL (MongoDB).

---

# 📌 12. Possíveis Evoluções Técnicas
Implementação de filas com RabbitMQ ou Apache Kafka para arquiteturas distribuídas.

Mecanismos avançados de retry automático com backoff exponencial e rotação de proxies residenciais.

---

# 👨‍💻 Autor

Desenvolvido por **João Henrique de Oliveira** como solução para o desafio técnico de automação, scraping e engenharia de software.

* **LinkedIn:** [linkedin.com/in/joão-henrique-de-oliveira-dev](https://www.linkedin.com/in/jo%C3%A3o-henrique-de-oliveira-dev/)
* **GitHub:** [github.com/joaohenriDev](https://github.com/joaohenriDev)
* **E-mail:** joaohenri293@gmail.com

---
