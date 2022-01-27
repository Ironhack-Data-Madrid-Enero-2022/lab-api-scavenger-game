def Read_files_in(url):
    token = open ("../token.txt").readlines()[0]
    params = {"Authorization": f"token {token}"} # This should enter as a parameter in a proper function, this is not a proper function
    first_read = req.get(url, headers = params).json()
    files_dict = dict()
    message, message_dic = '' , dict()
    for directory in first_read:
        name = directory['name']
        resposta = req.get(url+f'/{name}', headers = params).json()
        if type(resposta) == list: # We access all the directories in the repo, only reading lists helps ignoring other files that might be in the repo, such as gitignore
            for file in resposta:
                file_name =file['name']
                if 'scavengerhunt' in file_name: files_dict[name] = file_name # Now we got all the files and where to find them

    for key in files_dict.keys(): # now we access every file to read it and decode 
        resposta = req.get(url+ f'/{key}/{files_dict[key]}', headers = params).json() # getting the file
        content = base64.b64decode(resposta['content']) # Decoding it
        message_dic[int(files_dict[key][1:5])] = content.decode('utf-8') # We store the extracted data into a dictonary with the number in the file so we can sort them afterwards
    llista= list(message_dic.keys())
    llista.sort()
    for i in llista:
        message += message_dic[i]
    return message.replace('\n', ' ')

# Your code
URL = 'https://api.github.com/repos/ironhack-datalabs/scavenger/contents'
Read_files_in(URL)