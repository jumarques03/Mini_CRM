from pathlib import Path
import json, csv

class LeadRepository:
    def __init__(self, db_path="data/leads.json"):
        self.db_path = Path(db_path)

        self.db_path.parent.mkdir(exist_ok=True) 

    def _load(self):
        if not self.db_path.exists():
            return []
        try:
            return json.loads(self.db_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, leads):
        self.db_path.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

    def list_leads(self):
        return self._load()

    def add_lead(self, lead_dict):
        leads = self._load()
        leads.append(lead_dict)
        self._save(leads)

    def export(self):
        path_csv = self.db_path.parent / "leads.csv"

        leads= self._load()

        try:
            with path_csv.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["name", "company", "email", "stage", "created"])
                writer.writeheader()
                for row_lead in leads:
                    writer.writerow(row_lead)

            return path_csv         

        except PermissionError:
            return None
        

    def update_stage(self, lead_index, new_stage):
        leads = self._load()
        
        if 0 <= lead_index < len(leads):
            try:

                leads[lead_index]['stage'] = new_stage 
                self._save(leads) 
                return True  
            except Exception as e:
                print(f"Erro ao salvar: {e}")
                return False
        
        return False