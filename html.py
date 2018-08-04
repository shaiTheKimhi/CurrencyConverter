def get_value_by_tagId(html, tag, id):
    parts = html.split("<"+tag)
    for item in parts:
        id = item.split("id=\"")[1].split("\"")[0]
        if(id == id):
            return item.split(">")[1]