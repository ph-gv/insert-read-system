from util.db_connector import initialize_db
from view.main_view import MainView

if __name__ == "__main__":
    # 1. Garante que o banco e as tabelas existam (Util)
    initialize_db()
    
    # 2. Inicia a interface gráfica (View)
    app = MainView()
    app.mainloop() # Ciclo de eventos (Event Loop)
