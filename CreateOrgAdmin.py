import meraki
import pprint
import sys

#implement click

print("Enter your API_KEY and press Enter")
API_KEY = input()

try:

    dashboard = meraki.DashboardAPI(API_KEY)
    orgs = dashboard.organizations.getOrganizations()

except meraki.APIError as e:

    print("Invalid API key entered. Terminating script")
    sys.exit()

print("PLEASE ENSURE CORRECT FORMAT, THIS SCRIPT DOES NOT CONTAIN ERROR CHECKS FOR TYPOS")

email = input("Enter Admin Email: ")
name = input("Enter Admin Name: ")

access = 'read-only'

missed_orgs = []

org_count = 0

for o in range(len(orgs)):

    try:
         pprint.pprint("Creating Admin for " + orgs[o]['name'])

         dashboard.organizations.createOrganizationAdmin(
             orgs[o]['id'], email, name, access,
         )

         org_count = org_count + 1

    except meraki.APIError as e:

        missed_orgs.append(orgs[o]['name'])


if not missed_orgs:
    print("Admin successfully added to all " + str(org_count) + " orgs ")

else:
    print("Admin was not added to the following orgs")
    print(missed_orgs)
    print("Admin added to " + str(org_count) + " orgs ")
