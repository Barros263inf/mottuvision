# Mottu Vision Reconhecimento de Placas

## Introdução

O Sistema de Reconhecimento de Placas Veiculares é uma solução de visão computacional desenvolvida em Python que utiliza técnicas de processamento de imagem e reconhecimento óptico de caracteres (OCR) para identificar automaticamente placas de veículos a partir de vídeos. O projeto é composto por dois módulos principais:

1. **Módulo de Análise de Placas (main.py)**: Converte vídeos em frames individuais, processa cada imagem utilizando EasyOCR para extrair texto, valida se o texto corresponde ao padrão de placas brasileiras (formato Mercosul: ABC1D23) e armazena os resultados em arquivo JSON com as precisões de detecção.

2. **API Flask (api.py)**: Uma API REST simples que lê o arquivo JSON gerado pelo módulo de análise e disponibiliza um endpoint para consultar todas as placas identificadas no formato padronizado.

O sistema foi desenvolvido especificamente para o padrão de placas brasileiras Mercosul e é ideal para análise de vídeos de monitoramento de tráfego, controle de acesso e sistemas de segurança veicular.

## Desenvolvedores

Este projeto foi desenvolvido por:

- **Daniel Barros RM 556152** - *Desenvolvedor Python* - [GitHub](https://github.com/Barros263inf) | [LinkedIn](https://www.linkedin.com/in/danielbarros63)
- **Luccas Alencar RM 558253** - *Desenvolvedor em Back-End* - [GitHub](https://github.com/LuccasAlencar) | [LinkedIn](https://www.linkedin.com/in/luccasalencar/)


## Link para Vídeo de Apresentação

📺 **Demonstração Completa do Sistema**: [YouTube](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

O vídeo apresenta uma demonstração prática do sistema em funcionamento, incluindo:
- Processo de detecção de placas em tempo real
- Interface da API e seus endpoints

## Tecnologias Utilizadas

### Módulo de Análise de Placas (main.py)
- **Python 3.8+** - Linguagem principal do projeto
- **OpenCV 4.8.0** - Processamento de vídeo e extração de frames
- **EasyOCR 1.7.0** - Reconhecimento óptico de caracteres (OCR)
- **Loguru 0.7.0** - Sistema de logging avançado
- **tqdm 4.65.0** - Barras de progresso para processamento
- **Regex (re)** - Validação de padrões de placas brasileiras

### API Flask (api.py)
- **Flask 2.3.0** - Framework web minimalista para Python
- **JSON** - Formato de dados para armazenamento e comunicação

### Ferramentas de Desenvolvimento
- **pip** - Gerenciador de pacotes Python
- **Git** - Controle de versão

## Passo a Passo para Execução Local

### Pré-requisitos

Certifique-se de ter instalado em sua máquina:
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Git
- Arquivo de vídeo para análise (formato .mp4)

### 1. Clone do Repositório

```bash
git clone https://github.com/Barros263inf/mottuvision.git
cd mottuvision
```

### 2. Configuração do Ambiente Virtual

```bash
# Criação do ambiente virtual
python -m venv venv

# Ativação do ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instalação das Dependências

```bash
# Criar arquivo requirements.txt com as dependências necessárias
pip install opencv-python==4.8.0
pip install easyocr==1.7.0
pip install loguru==0.7.0
pip install tqdm==4.65.0
pip install flask==2.3.0

# Ou instalar diretamente:
pip install opencv-python easyocr loguru tqdm flask
```

### 4. Execução do Módulo de Análise de Placas

```bash
# Executar o processamento do vídeo
python main.py
```

O script irá:
- Converter o vídeo em frames individuais (salvos na pasta `images/`)
- Processar cada frame com OCR para detectar placas
- Validar se o texto detectado corresponde ao padrão de placas brasileiras
- Gerar um arquivo JSON com os resultados (`plates_beamsearch.json`)

### 6. Execução da API

```bash
# Primeiro, certifique-se de que existe o arquivo 'plates_beamsearch.json'
# Se necessário, renomeie o arquivo gerado ou ajuste o código da API

# Executar a API Flask
python api.py
```

A API estará disponível em: `http://localhost:5000`

### 7. Testando a API

```bash
# Testar o endpoint de listagem de placas
curl http://localhost:5000/placas

# Ou acesse diretamente no navegador:
# http://localhost:5000/placas
```

### 8. Configurações Opcionais

#### 8.1. Ajustar Decoder do OCR

No arquivo `main.py`, você pode alterar o tipo de decoder na linha:
```python
# Opções: 'greedy', 'beamsearch', 'wordbeamsearch'
decoder = 'greedy'
```

#### 8.2. Ajustar Precisão Mínima

Para ajustar a precisão mínima de detecção, modifique no `main.py`:
```python
if precision > 0.75 and is_plate:  # Altere 0.75 para o valor desejado
```

#### 8.3. Ajustar Intervalo de Frames

Para processar mais ou menos frames do vídeo, altere no `main.py`:
```python
currentframe += 15  # Altere 15 para o intervalo desejado
```

### Estrutura de Arquivos do Projeto

Após a execução, a estrutura do projeto será:

```
plate-recognition-system/
├── venv/                       # Ambiente virtual
├── api.py                      # API Flask
├── main.py                     # Módulo principal de análise
├── sample.mp4                  # Vídeo de entrada (fornecido pelo usuário)
├── plates_greedy.json          # Resultados com decoder greedy (opicional)
└── plates_beamsearch.json      # Resultados com decoder beamsearch
```

### Formato dos Dados JSON

O arquivo JSON gerado contém as placas detectadas no formato:
```json
{
    "ABC1D23": 0.89,
    "XYZ9A87": 0.92,
    "DEF2B34": 0.85
}
```

Onde:
- Chave: Placa detectada no formato Mercosul
- Valor: Precisão da detecção (0.0 a 1.0)

### Endpoint da API

**GET /placas**
- **Descrição**: Lista todas as placas detectadas
- **Resposta de Sucesso (200)**:
```json
[
    {"Placa": "ABC1D23"},
    {"Placa": "XYZ9A87"},
    {"Placa": "DEF2B34"}
]
```
- **Resposta de Erro (400)**: JSON vazio
- **Resposta de Erro (500)**: Erro interno do servidor

### Solução de Problemas Comuns

**Erro: "No module named 'cv2'"**
```bash
pip install opencv-python
```

**Erro: "No module named 'easyocr'"**
```bash
pip install easyocr
```

**Erro: "FileNotFoundError: sample.mp4"**
- Certifique-se de que o arquivo de vídeo está na raiz do projeto
- Ou altere o nome do arquivo no código `main.py`

**Erro: "plates_beamsearch.json not found" na API**
```bash
# Opção 1: Gere o arquivo com beamsearch
# Altere decoder = 'beamsearch' no main.py e execute novamente

# Opção 2: Altere o nome do arquivo na api.py
# Mude 'plates_beamsearch.json' para 'plates_greedy.json'
```

**API não inicia (porta ocupada)**
```bash
# Verifique se a porta 5000 está ocupada
lsof -i :5000

# Ou altere a porta na api.py adicionando:
app.run(debug=True, port=5001)
```

**Performance baixa no processamento**
- Aumente o intervalo entre frames: `currentframe += 30` (ao invés de 15)
- Reduza a qualidade do vídeo de entrada
- Ajuste a precisão mínima para um valor maior

**EasyOCR demora muito para inicializar**
- Primeira execução sempre demora mais (download de modelos)
- Execute em um ambiente com boa conexão de internet
- Considere usar apenas o decoder 'greedy' para melhor performance

### Próximos Passos

Após a configuração local, você pode:
- Testar com diferentes vídeos de tráfego
- Explorar os três tipos de decoder do EasyOCR ('greedy', 'beamsearch', 'wordbeamsearch')
- Ajustar os parâmetros de precisão para otimizar resultados
- Expandir a API com novos endpoints (filtros, estatísticas, etc.)
- Implementar interface web para visualização dos resultados
- Adicionar suporte para outros formatos de vídeo

### Recursos Adicionais

- **Padrão de Placas Mercosul**: Sistema implementado segue o formato ABC1D23
- **Decoders EasyOCR**: 
  - `greedy`: Mais rápido, menor precisão
  - `beamsearch`: Balanceado entre velocidade e precisão
  - `wordbeamsearch`: Mais lento, maior precisão
- **Logs detalhados**: Utilize o Loguru para monitorar o processamento

Para suporte adicional, consulte a documentação oficial do [EasyOCR](https://github.com/JaidedAI/EasyOCR) e [OpenCV](https://docs.opencv.org/).