from datetime import date
from models.Stages import Stages

class Lead(Stages):
    def __init__(self, name, company, email, stage):
        self.name = name
        self.company = company
        self.email = email
        super().__init__(stage)
        self.created = date.today().isoformat()


    def model_lead(self):
        """Cria um lead como dicionário simples."""
        return {
            "name": self.name,
            "company": self.company,
            "email": self.email,
            "stage": self.stage,
            "created": self.created,
        }
    
    def show_lead(self):
        stage = self.show_stage() if hasattr(self, "show_stage") else self.stage        # ENTENDER MELHOR ISSO AQUI
        return f"\nLead adicionado!\nName:{self.name} | Company:{self.company} | Email:{self.email} | Stage:{stage} | Created:{self.created}"
