# Internet Banking


## Sobre o projeto

### Requisitos

#### Identificação/Login do correntista 

entradas: conta corrente (5 dígitos) e senha (4 dígitos)
  
Haverá pelo menos 2 correntistas "cadastrados". Pelo menos um correntista terá o perfil "Normal" e o outro terá o perfil "VIP" 

#### Opções

  1. Ver Saldo
  2. Extrato
  3. Saque
  4. Depósito
  5. Transferencia
  6. Solicitar visita do gerente 
  7. Trocar de usuário

#### Saldo
Apenas o valor atualizado em R$.

#### Extrato
O extrato exibirá data, hora, descrição e valor (entre parênteses quando negativo) de cada movimentação

#### Saque
O usuário Normal não pode sacar além do valor em saldo. O VIP pode, mas terá seu saldo reduzido em 0.1% por minuto até que sejam feitos depósitos suficientes para cobrir o saldo negativo.

#### Transferências
Cada usuário poderá realizar transferências informando o valor e a conta corrente do destinatário (não pode transferir para si mesmo nem para conta inexistente).
- As transferências aparecerão nos extratos tanto do cedente quanto do sacado.
- O usuário Normal poderá fazer transferências de até R$1000,00. O VIP não terá limite. 
- O usuário Normal será debitado em R$8,00 por transferência e o VIP em 0,8% do valor transferido. Deverão ser destacados esses débitos no extrato.

#### Visita do gerente
Apenas o usuário VIP pode ver a opção "Solicitar visita do gerente". Esta opção precisa ser confirmada pelo usuário e, após a confirmação, apenas debita R$50,00 da conta do usuário.

#### Trocar de usuário
Deve ser possível sair da conta de usuário e entrar em outro para verificar as movimentações

## Como utilizar

Por conflitos de caracteres ou de traduções, o sistema não funciona adequadamente em alguns sistemas, principalmente no windows.
Procure realizar sua implementação em um ambiente linux, preferencialmente no Ubuntu.
As seguintes tecnologias são necessárias para o bom funcionamento do sistema:

- Python 3

Todas as outras dependências e bibliotecas externas já estão acopladas nesse repositório e não necessitam de maior atenção do usuário. O sistema de banco de dados utilizado foi o `sqlite3` fornecido pelo próprio Django.

### Inicializando o ambiente

- Faça download ou clone o repositório para um diretório dentro de sua preferência.
- Utillizando o terminal, navegue até o diretório que você extraiu o repositório e digite o seguinte comando:
```
source env/bin/activate
```

### Inicializando o servidor

Para usuários do sistema operacional Linux, basta navegar até o diretório em que foi extraido o repositório e digitar o comando a seguir no terminal de controle.

```
python3 manage.py runserver
```

- Acesse a aplicação em `http://127.0.0.1:8000/` ou `localhost:8000/` 

### Contas Cadastradas

Para testes iniciais, algumas contas já estão cadastradas no sistema, e todas não possuem transações associadas.
O Django não permite cadastro de contas com senhas de quatro dígitos, então foram utilizados 8 dígitos de senha.

| Conta | Senha    | Saldo | Tipo   |
| ----- | -------- | ----- | ------ |
| 54103 | 0rL9uVDM | 5000  | Normal |
| 36780 | 2OiNYwy8 | 73,2  | Normal |
| 72154 | 1DGoNNAf |  610  |  Vip   |
| 10284 | 9exGhMW7 | 12,3  |  Vip   |

