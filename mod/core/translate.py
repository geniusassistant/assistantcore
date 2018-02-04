def substring_after(s, delim):
    return s.partition(delim)[2]

def outsource(text):
    if 'translate' in text:
        totranslate = text.replace('translate', '').replace(substring_after(text, 'into'), '').replace('into', '')
        lang = substring_after(text, 'into')


        import goslate

        gs = goslate.Goslate()
        translatedText = gs.translate(totranslate,'fr')

        print(translatedText)

        return 'translating ' + totranslate + ' into ' + lang