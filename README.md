# Projeto Verão

## OBJETIVO
Este é um projeto que servirá de base para medir a proficiência dos estudantes do Aqui Educa. Ele deverá ser feito respeitando os prazos abaixo. Ao final, uma apresentação será feita pelo time com as seguintes explicações:

- `Técnica`: **como o código foi implementado e o porque das escolhas das bibliotecas envolvidas** <br>
O time deverá explicar detalhes do código, e responder a perguntas técnicas durante a apresentação 

- `Funcional`: **explicação das funcionalidades implementadas e do layout escolhido** <br>
Explicação das funcionalidades envolvidas no projeto, as telas, e os motivos de ter escolhido o tema em questão.

- `Softskills`: **impedimentos, dificuldades e dúvidas** <br>
O time deverá anotar todos os impedimentos, dificuldades e dúvidas, tanto as que foram solucionadas ou não, durante a construção do projeto, e demonstrar essa relação na apresentação.  

<br>

## TIMES
1. **Huan** e Bruna Costa
2. **Rafael Aquino, Marlon** e César
3. **Leo** e Bruna Lima
4. **Gustavo** e Lívia
5. **Harry** e Thiago

> As pessoas em negrito são os **Ponto Focais** do time e terão a obrigação de representar o time (líderes), organizando os encontros, passando o conhecimento aprendido para o(s) colega(s) do time e comunicando com o facilitador os impedimentos, dificuldades e pontos de atenção.

<br>

## O PROJETO

Seguindo o exemplo do projeto deste repositório, o time deverá **escolher um tema** para o seu projeto, e que seja diferente do tema deste projeto em questão, e construir ao menos **nove funcionalidades** em seu sistema, e para cada funcionalidade, no mínimo **três ações**.

## TEMA
O tema é composto pelo negócio para o qual o seu sistema será desenvolvido. Alguns exemplos: 

- sistema de salão de beleza
- sistema de jogos do campeonato brasileiro
- sistema de filmes, gêneros, salas de cinema, etc
- sistema de livros, autores, livrarias, etc
- sistema de viagens, passagens, aeronaves, aeroportos, etc

## FUNCIONALIDADE
Funcionalidade é um conjunto de ações de uma tela específica. Por exemplo, um sistema de loja possui algumas funcionalidades tais quais:

- Cliente
- Fornecedor
- Produto
- Venda

## AÇÕES
As ações das funcionalidades são consistidas por estas:

- Inserir
- Listar
- Deletar

> O projeto deste repositório possui uma tela Home e a funcionalidade **CLIENTE** com duas telas, uma tela de consulta dos clientes e outra tela com o cadastro dos clientes. Utilize este exemplo para produzir as funcionalidades e ações do seu sistema.

### Especificação geral do projeto:
- O arquivo de API deverá ser único;
- As telas do sistema precisarão ser relacionadas para garantir uma navegação nítida, ou seja, ao clicar no botão inserir, o usuário irá para a tela de cadastro da funcionalidade em questão, e ao clicar no botão voltar, o usuário será levado de volta para a tela de consulta;
- Se achar interessante, adicione um menu de navegação para garantir a navegação entre as funcionalidades;
- Para cada ação da funcionalidade em questão, adicione um end-point na API (incluir, obter, listar, atualizar, etc)
- 

## BANCO DE DADOS
O banco de dados em uso é uma planilha com **extensão .csv**. Caso não possua nenhum editor de planilhas instalado em seu computador, recomendo baixar e instalar o Libre Office [neste link](https://pt-br.libreoffice.org/baixe-ja/libreoffice-novo/?type=win-x86_64&version).

> Como no exemplo deste repositório, o seu projeto deverá utilizar a **biblioteca csv** para a edição do conteúdo do arquivo que irá armazenar os dados

Naturalmente para cada funcionalidade você precisará ter um arquivo csv correspondente. Como no exemplo, adicione os seus arquivos csv na pasta **db** para garantir organização do seu projeto.


## APRESENTAÇÃO
No dia 03/01 teremos as apresentações dos times. A apresentação será de 30 minutos por time e será dividido da seguinte maneira:

- 10 minutos de apresentação do projeto
- 15 minutos de perguntas dos demais times - item obrigatório: se o seu time não estiver apresentando, assista com muita atenção ao time que estará realizando a apresentação para que vocês possam elaborar perguntas que serão feitas neste momento
- 5 minutos de perguntas do facilitador @Dan

> Com o intuito de maximizar a proficiência e o desafio, as pessoas que **NÃO SÃO** pontos focais é que deverão ser as apresentadoras

<br><br>

# EXECUTANDO ESTE REPOSITÓRIO

## Baixando o repositório
Com o Git instalado em seu computador, abra o prompt de comando (Commander, DOS, GitBash, etc) e faça o seguinte:

1. Navegue até a pasta que gostaria de usar para armazenar este projeto. No meu caso é a C:/repo/aqui-educa/
> cd C:/repo/aqui-educa/
2. Realize o *clone* do repositório com o comando abaixo
> git clone https://github.com/Aqui-Educa/projeto-verao.git 

## Instalando as bibliotecas do projeto
Perceba que existe um arquivo neste projeto chamado **requirements.txt**. Este arquivo possui todas as bibliotecas que o projeto necessita. Utilize ele para instalar estas bibliotecas em seu computador. Faça o seguinte:
1. Abra a pasta raiz do projeto via console
2. Entre na pasta **api** 
>cd api
2. Rode o seguinte comando para instalar as bibliotecas
> pip install -r requirements.txt
3. As bibliotecas serão instaladas

> Você poderá utilizar este mesmo arquivo em seu projeto para garantir que ao ser baixado, o usuário possa instalar todas as bibliotecas da mesma forma que você está fazendo agora

## Rodando a API

1. Via console, a partir da pasta raiz do projeto, entre na pasta **api** e rode os seguintes comandos
>  set FLASK_APP=api.py
<br>
> flask run

A partir de agora a sua API está em execução. Para finalizar, basta pressionar **CTRL+C** que a console voltará para a linha de comando tradicional.

## Executando o front-end

As telas do front-end são arquivos HTML e que possuem internamente códigos Javascript que fazem as requisições a API de forma simples, e utilizando fetch como ferramenta de requisições (veja um exemplo no **cadastro_cliente.html**).

1. Utilizando o explorador de arquivos do Windows, abra a pasta deste projeto e clique duas vezes no arquivo **home.html**
2. O projeto front-end será aberto e as ações realizadas nele serão convertidas em requisições para a API

## CORS

Para conseguirmos ter acesso a API a partir de uma aplicação Javascript Web, é necessário declararmos em nossa API alguns comandos CORS conforme segue a imagem abaixo. Por enquanto abstraia e decore a necessidade destes comandos, o entendimento sobre ele será feito no futuro.

![CORS](/images/cors.png)

<br><br>

# REFERÊNCIAS BIBLIOGRÁFICAS

Caso você não esteja familiarizado(a) com alguns dos conceitos acima, sugiro uma atenção especial nesta seção. Leia, assista e consuma o máximo de conteúdos listados a seguir. Siga a ordem sugerida abaixo.

## HTML

1. [W3School - HTML](https://www.w3schools.com/html/)
2. [Vídeo aula - série de 4 vídeos](https://www.youtube.com/watch?v=1LJGQb_pn6k)

## Javascript

1. [Curso completo de Javascript para iniciantes](https://www.youtube.com/watch?v=i6Oi-YtXnAU)
2. [W3School - Javascript](https://www.w3schools.com/js/default.asp)

## Python - conceitos básicos

1. [Aula com o Amoedo](https://drive.google.com/file/d/1cfXNQoplI0m9DaqyFDnHbI-PoCyyf8X4/view?usp=sharing)

## Programação Orientada a Objetos em Python

1. [Aula com o Amoedo](https://drive.google.com/file/d/1acwYGBxs9ccwtP8U4Uw3i5mcj_Lz8ZPc/view?usp=sharing)

## API com Python + Flask

1. [Conceitos básicos sobre API - @Dan](https://drive.google.com/file/d/1KoTFUEu0nfGTTTMfEYq0KcWEG8ha58VV/view?usp=sharing)
2. [Vídeo aula 1 - @Dan](https://drive.google.com/file/d/19YxGJhOCbpFEd2I18XY2DVLUTmKICEjz/view?usp=sharing)
3. [Vídeo aula 2 - @Dan](https://drive.google.com/file/d/1gK4Md-e39WhKuYei-vsxaDOqMiXdJ6BW/view?usp=sharing)

## Python + CSV

1. [Construindo um projeto - parte 1](https://drive.google.com/file/d/1D7wCTnpCiBk46ZFyN6YDcM2levaxMot0/view?usp=sharing)
2. [Construindo um projeto - parte 2](https://drive.google.com/file/d/186KmpIWzFbERerbzqa6Uo5iH7bYUUc2H/view?usp=sharing)