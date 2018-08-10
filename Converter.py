import sys
import html


def get_currency(raw):
    return html.get_value_by_tagId(raw, "span", "uccResultAmount")


if(sys.version.index("3") == 0):
    import urllib.request
    money = "0"
    source = "USD"
    target = "ILS"
    for i in range(len(sys.argv)):
        if (i == 2):
            money = str(sys.argv[1])
        elif (i == 3):
            source = sys.argv[2]
        elif (i == 4):
            target = sys.argv[3]
    
    f = urllib.request.urlopen("https://www.google.com/search?q=" + money + "" + source + "" + target)
    currency = get_currency(f.read(400))
    print(currency)
else:
    import requests
    money = "0"
    source = "USD"
    target = "ILS"
    for i in range(len(sys.argv)):
        if (i == 2):
            money = str(sys.argv[1])
        elif (i == 3):
            source = sys.argv[2]
        elif (i == 4):
            target = sys.argv[3]
    
    f = requests.get("http://www.google.com/search?q=" + money + " " + source + " " + target,verify=False)
    currency = get_currency(f.Text)
    print(currency)
    