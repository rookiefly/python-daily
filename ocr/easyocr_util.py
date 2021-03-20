import easyocr
# need to run only once to load model into memory
reader = easyocr.Reader(['ch_sim', 'en'])
result = reader.readtext('chinese.jpeg',  detail=0)
print(result)
