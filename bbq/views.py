from django.shortcuts import render

def index(request):
    import gspread
    import datetime
    x = datetime.datetime.now()
    from oauth2client.service_account import ServiceAccountCredentials
    # Maenin Google sheet
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json",scope)
    client = gspread.authorize(creds)
    sheet = client.open("BBQ").sheet1
    sample = sheet.get_all_records()
    full = []
    today = []
    for dct in sample:
        temp1 = []
        for key in dct:
            if key != "Timestamp":
                temp1.append(dct[key])
        full.append(temp1)
    for items in full:
        if str(items[2][0:6]) == str(x.strftime("%x"))[0:6]:
            today.append(items)
    context = {
        "data" : full,
        "jumlah" : len(full),
        "inihari" : today,
    }
    return render(request,"index.html",context)