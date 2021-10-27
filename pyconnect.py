
from pysnow import CreateConnection
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('SNOW_URL_PDI')
snow_user = os.getenv('SNOW_USER_PDI')
snow_user_password = os.getenv('SNOW_USER_PWD_PDI')

request = CreateConnection(
    base_url,
    snow_user,
    snow_user_password
)

print(request.get_user('aileen.mottern@example.com'))