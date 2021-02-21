from datetime import datetime
from getpass import getpass
import caldav

caldav_servers = [{
    'url': "https://timscheuermann.ddns.net/remote.php/dav/calendars/admin/geburtstage/",
    'username': "admin",
    'password': "NULL"
}]
print(caldav_servers[0]["username"])
if(caldav_servers[0]["password"]=="NULL"):
    caldav_servers[0]["password"] = getpass("Please enter WebDav password: ")

vcal = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Example Corp.//CalDAV Client//EN
BEGIN:VEVENT
UID:1234567890
DTSTAMP:20100510T182145Z
DTSTART:20100512T170000Z
DTEND:20100512T180000Z
SUMMARY:This is an event
END:VEVENT
END:VCALENDAR
"""

client = caldav.DAVClient(**(caldav_servers[0]))
principal = client.principal()
calendars = principal.calendars()
if len(calendars) > 0:
    calendar = calendars[2]
    print("Using Calendar "+str(calendar))

    event = calendar.add_event(vcal)
    print("Event" + str(event) + "created")

    print("Looking for events in 2010-05")
    results = calendar.date_search(datetime(2010, 5, 1), datetime(2010, 6, 1))

    for event in results:
        print("Found" + str(event))