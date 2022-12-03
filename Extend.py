import meraki
import datetime
import pandas as pd

API_KEY = '7670f3d290a23ae3457b894d369707f6a2beb642'

dashboard = meraki.DashboardAPI(API_KEY)


def updateTime():
    network_id = 'L_645140646620844696'

    today = datetime.datetime.now().replace(microsecond=0)
    new_date = pd.to_datetime(today) + pd.DateOffset(days=7)
    as_string = str(new_date)
    dt = as_string.split()
    date = dt[0]
    time = dt[1]
    real_time = f'{date}T{time}Z'

    dashboard.networks.updateNetworkFirmwareUpgrades(
        network_id,
        products={'switch': {'nextUpgrade': {'time': real_time }}}
    )

def main():
    updateTime()

if __name__ == '__main__':
    main()
