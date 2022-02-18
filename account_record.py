acount_record={
    # "zeeshan":{"password":"123",
    #            "balance":"40000",
    #            "history": []
    
    # }
} #this dictionary contains all record of the bank accounts
def json_read():
    import json
    
    with open("data.json","r+") as file:
        
        dict=json.load(file)
        # print("Json_read function: dict:",dict)
        global acount_record
        # old_dict=acount_record
        acount_record.clear()
        acount_record.update(dict)
        # print("Json_read function: acount_record:",acount_record)
        file.seek(0)
        file.close()
# def json_write():
#     import json
#     global acount_record
#     with open("data.json","r+") as file:
#         dict=json.load(file)
#         file.seek(0)
#         dict.update(acount_record)
#         file = json.dump(dict, file)
#         file.close()
def json_write():
    import json
    with open("data.json","r+") as file:
        diction={}
        dict=json.load(file)
        for item in dict:
            diction[item]=dict[item]
        # print("                     diction: ",diction)
        # print("                     diction before writing in write function: ",diction)
        file.seek(0)
        diction.update(acount_record)
        # print("                     diction after writing in write function: ",diction)
        file = json.dump(diction, file)
        # file.close()
