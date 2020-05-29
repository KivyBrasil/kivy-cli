# kivy-cli (EM DESENVOLVIMENTO)
Gerenciador de templates para o Kivy.

## Objetivo
É usado para:
- a criação da estrutura de uma aplicação de exemplo.
- para separar arquiteturas
- agilizar processo de criação de arquivos

## Exigências
```
python >= 3.7

click == 7.0
```

## Como utilizar
```
pip3 install -e .

or

pip3 install setup.py --editable .
```

## Após instalar as dependências, no terminal/cmd:

Mostra se tudo está ok:
```
kv init
```

Cria uma estrutura simple de aplicação com a arquitetura mvc:
```
kv create ONomeDoMeuApp
```

Inicia a aplicação, procurando pelo arquivo main.py ou passando como argumento o nome do arquivo principal.
```
kv run

or

kv run app
```
