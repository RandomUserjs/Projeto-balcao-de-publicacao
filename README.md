# Publicapy

Este é um programa em python que possívelmente será utilizado para realizar um movimento mensal de publicações para salões do reino

## Dependências

1. Git (Para instruções de como instalar veja [Instalando o Git](https://git-scm.com/book/pt-br/v2/Come%C3%A7ando-Instalando-o-Git))
2. Python 3 (Para instruções de como instalar, veja [Instalando o Python 3 no Windows](https://python.org.br/instalacao-windows/) (Para Windows) e [Instalando o Python no Linux](https://python.org.br/instalacao-linux/) (Para Linux))
3. Pip (Para instruções de como instalar veja [Instalar pacotes usando pip](https://packaging.python.org/pt-br/latest/guides/installing-using-pip-and-virtual-environments/#prepare-pip))
4. Plataformdirs library (instruções de como instalar abaixo)
5. SQL3 (Para instruções de como instalar veja [Instalando o SQLite3 no Windows](https://dev-to.translate.goog/dendihandian/installing-sqlite3-in-windows-44eb?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc) (Para Windows). Para linux verifique se o binário está disponível no repositório da sua distro, geralmente se chama sqlite ou sqlite3)

## Como instalar:

> [!NOTE]
> Execute os comandos abaixo em seu terminal preferido, ou em qualquer um mesmo.

Clone o projeto:

```bash
git clone https://github.com/RandomUserjs/Projeto-balcao-de-publicacao.git
```

Vá para a pasta do projeto:

```bash
cd Projeto-balcao-de-publicacao
```

Crie um ambiente virtual do Python com venv e ative-o (Para mais informações veja [Instalar pacotes em um ambiente virtual usando pip e venv](https://packaging.python.org/pt-br/latest/guides/installing-using-pip-and-virtual-environments/)):

### Linux / macOS

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Confirme que ele está ativado com `which python`, se estiver ativo, o caminho do arquivo incluirá a pasta `venv`

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute o arquivo app.py:

```bash
python app.py
```

> [!NOTE]
> Caso você feche o terminal, é preciso ativar o ambiente virtual novamente, utilizando o mesmo comando que na primeira vez, não é necessário criar o ambiente virtual novamente.

### Windows

Crie o ambiente virtual:

```shell
py -m venv venv
```

Ative o ambiente virtual:

```shell
venv\Scripts\activate
```

Confirme que ele está ativado com `where python`, se estiver ativo, o caminho do arquivo incluirá a pasta `venv`

Instale as dependências:

```shell
py -m pip install -r requirements.txt
```

Execute o arquivo app.py:

```shell
py app.py
```

> [!NOTE]
> Caso você feche o terminal, é preciso ativar o ambiente virtual novamente, utilizando o mesmo comando que na primeira vez, não é necessário criar o ambiente virtual novamente.
