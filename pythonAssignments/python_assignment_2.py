from sys import exit # I'm using this function to exit from the code block, if not we will not be able to get out from the code block

from psutil import cpu_percent # Importing this library to check the CPU utilization of the local machine

def get_cpu_utilization():
    try:  
        cpu_usage = cpu_percent(interval=1)  # try and except method is used to handle the errors. Try means without any error, the code block will be executed
        return cpu_usage
    
    except KeyboardInterrupt:  # In exception, we interupt the process if we find any error or to stop the process manually by interupting the process
        print("Exception occurred by keyboard interruption!!") # as soons as we press ctrl+c, this message will be popped up
        exit()
        
    except Exception:
        print("Exception Occurred!",Exception.__name__)

while(True):
    threshold=80 # for our local machine we can check this by entering 2 as s threshold value, so that "Alert! CPU usage exceeds threshold: 4.3%" will be printed
    cpu_utilization=get_cpu_utilization()
    if cpu_utilization>threshold:
        print("Alert! CPU usage exceeds threshold: {0}%".format(cpu_utilization))
    else:
        print("Monitoring CPU usage...")
