from download_data_from_iTunes import search_itunes_api

def process_user_input(entries):
    entries_list = [entry.strip().split(",") for entry in entries.splitlines()]
    itunes_data = []
    for entry in entries_list:
        if len(entry) == 2:
            author, title = entry
            result = search_itunes_api(author, title)
            if result:
                itunes_data.extend(result)
    return itunes_data
