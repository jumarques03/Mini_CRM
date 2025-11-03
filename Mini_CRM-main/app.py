from models.Lead import Lead
from models.LeadRepository import LeadRepository
from models.Stages import Stages
from pathlib import Path 


APP_DIR = Path(__file__).parent 
DB_PATH = APP_DIR / "data" / "leads.json" 
lead_backend = LeadRepository(DB_PATH)


def stages_options():
    STAGES = [
        "Novo",
        "Em contato",
        "Interessado",
        "Negociando",
        "Fechado",
        "Perdido"       # lead que não deu certo
    ]

    print("\nOpções de Stages:")
    for stage in STAGES:
        print(f" - {stage}")

    stage_option = input("Stage: ")

    if stage_option not in STAGES: 
        print("Selecione apenas as opções válidas")
        return None

    stage = Stages(stage_option)

    return stage.show_stages()
    

def add_flow():
    name = input("Nome: ").strip()
    company = input("Empresa: ").strip()
    email = input("E-mail: ").strip()
    stage = stages_options()

    if not stage:
        print("Cadastro cancelado devido ao stage inválido.")
        return

    if not name or not email or "@" not in email:
        print("Nome e e-mail válido são obrigatórios.")
        return

    lead = Lead(name, company, email, stage)
    modeled_lead = lead.model_lead()
    print(lead.show_lead()) 

    lead_backend.add_lead(modeled_lead)


def list_flow():
    leads = lead_backend.list_leads()
    if not leads:
        print("Nenhum lead ainda.")
        return
    
    # Mostra o stage na lista
    print("\n# | Nome                 | Empresa            | E-mail                | Stage")
    print("--+----------------------+-------------------+-----------------------+----------------")
    for i, l in enumerate(leads):
        print(f"{i:02d} | {str(l.get('name', '')).ljust(20)} | {str(l.get('company', '')).ljust(17)} | {str(l.get('email', '')).ljust(21)} | {str(l.get('stage', '')).ljust(14)}")


def search_leads():
    search_info = input("Buscar por (nome/empresa/email): ").strip().lower()
    if not search_info:
        print("Consulta vazia")
        return
    
    leads = lead_backend.list_leads()
    results = []

    for i, lead in enumerate(leads):
        string_lead = f"{lead.get('name', '')}  {lead.get('company', '')}  {lead.get('email', '')}".lower()
        
        if search_info in string_lead:
            results.append(lead)

    if not results:
        print("Nenhum lead encontrado.")
        return


    print("\n# | Nome                 | Empresa            | E-mail                | Stage")
    print("--+----------------------+-------------------+-----------------------+----------------")
    for i, l in enumerate(results):
        print(f"{i:02d} | {str(l.get('name', '')).ljust(20)} | {str(l.get('company', '')).ljust(17)} | {str(l.get('email', '')).ljust(21)} | {str(l.get('stage', '')).ljust(14)}")


def export_csv():
    path_csv = lead_backend.export()

    if path_csv != None:
        return print(f"Arquivo exportado para: {path_csv}")
    else:
        return print(f"Erro ao exportar o arquivo")


def update_stage_lead():
    print("--- Atualizar Stage do Lead ---")
    list_flow() 
    leads = lead_backend.list_leads()

    if not leads:
        return

    try:
        id = input("\nQual o ID (linha #) do lead que deseja atualizar? ")
        id_to_update = int(id)

        if not (0 <= id_to_update < len(leads)):
            print("ID inválido. Tente novamente.")
            return

        current_lead = leads[id_to_update]
        print(f"\nAtualizando o lead: {current_lead.get('name', 'N/A')}")
        print(f"Stage atual: {current_lead.get('stage', 'N/A')}")
        
        new_stage = stages_options() 

        if new_stage:
            success = lead_backend.update_stage(id_to_update, new_stage)
            
            if success:
                print(f"Stage do lead '{current_lead.get('name', 'N/A')}' atualizado para '{new_stage}' com sucesso!")
            else:
                print("Erro ao atualizar o stage.")
        else:
            print("Operação de atualização cancelada (stage inválido).")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número (ID).")


def main():
    while True:
        print_menu()
        op = input("Escolha: ").strip()
        if op == "1":
            print("\n")
            add_flow()
        elif op == "2":
            print("\n")
            list_flow()
        elif op == "3":
            print("\n")
            search_leads()
        elif op == "4":
            print("\n")
            export_csv()
        elif op == "5":
            print("\n")
            update_stage_lead()
        elif op == "0":
            print("\n")
            print("Até mais!")
            break
        else:
            print("\n")
            print("Opção inválida.")

def print_menu():
    print("\nMini CRM de Leads")
    print("[1] Adicionar lead")
    print("[2] Listar leads")
    print("[3] Buscar lead (nome/empresa/e-mail)")
    print("[4] Exportar CSV")
    print("[5] Atualizar estágio do lead")
    print("[0] Sair")

if __name__ == "__main__":
    main()