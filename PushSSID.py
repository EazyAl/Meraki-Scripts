import meraki
import os
from dotenv import load_dotenv

load_dotenv()

key = os.environ.get('API_KEY')
org_id = os.environ.get('ORG_ID')

dashboard = meraki.DashboardAPI(key)

networks = dashboard.organizations.getOrganizationNetworks(
    org_id, total_pages='all'
)

for n in networks:
    dashboard.wireless.updateNetworkWirelessSsid(
    n['id'], 5,
    name='API TEST',
    enabled=True
)
