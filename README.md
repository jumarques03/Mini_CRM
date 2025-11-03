# 🚀 Mini CRM de Leads

Este é um projeto de um sistema de "Mini CRM" (Customer Relationship Management) focado no gerenciamento de leads. Ele foi desenvolvido como um exercício prático para aplicar conceitos fundamentais de Programação Orientada a Objetos (POO).

O sistema é executado inteiramente via terminal e armazena os dados localmente em um arquivo `.json`, permitindo também a exportação dos dados para `.csv`.

## ✨ Funcionalidades

O menu principal oferece as seguintes operações:

* **[1] Adicionar lead:** Cadastra um novo lead (nome, empresa, e-mail) e o define com um stage inicial.
* **[2] Listar leads:** Exibe todos os leads cadastrados em uma tabela formatada, incluindo seus stages.
* **[3] Buscar lead:** Permite a busca de leads por nome, empresa ou e-mail.
* **[4] Exportar CSV:** Salva a lista atual de leads em um arquivo `leads.csv` dentro da pasta `data/`.
* **[5] Atualizar estágio do lead:** Permite selecionar um lead pelo ID (linha) e alterar seu stage (Novo, Em contato, Interessado, etc.).
* **[0] Sair:** Encerra o programa.

## 🏛️ Conceitos de POO Aplicados

Este projeto foi estruturado para demonstrar os pilares da Programação Orientada a Objetos:

* **Classes e Objetos:** O sistema é dividido em classes com responsabilidades únicas:
    * `Lead`: Modela o que é um lead, seus atributos e informações.
    * `Stages`: Modela o conceito de "stage" (estágio) do lead.
    * `LeadRepository`: Responsável por toda a persistência de dados (ler e salvar no arquivo `.json`, exportar `.csv`).
* **Herança:** A classe `Lead` herda da classe `Stages` (`class Lead(Stages):`) para reutilizar o comportamento e atributos do estágio.
* **Polimorfismo:** Um objeto `Lead` pode utilizar métodos da sua classe pai (`Stages`), como o `show_stage()`.

## 🛠️ Tecnologias Utilizadas

* **Python 3**
    * `pathlib` (para manipulação de caminhos de arquivos)
    * `json` (para persistência de dados)
    * `csv` (para exportação)
    * `datetime` (para salvar a data de criação do lead)

## 🏁 Como Executar

1.  Clone este repositório:
    ```bash
    git clone https://github.com/jumarques03/Mini_CRM.git
    ```
2.  Navegue até a pasta do projeto:
    ```bash
    cd Mini_CRM-main
    ```
3.  Execute o arquivo principal:
    ```bash
    python app.py
    ```
