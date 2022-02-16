from dotenv import load_dotenv

import os 


dotenv_values = load_dotenv('.env')
print(os.getenv("DBDATABASE"))