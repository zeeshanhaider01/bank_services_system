from datetime import datetime
def curnt_time(): #This function will provide the time at that time when its is called
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_time