''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''

# import require modules
import ftplib
import os
import shutil
import schedule
import time
import log
from ftplib import FTP

running = True

# logging configuration
# logging.basicConfig(filename=r"D:\autocad\loginfo.log", format="%(asctime)s - %(process)d - %(levelname)s - %(message)s")

def automate_file_trnasfer():
    # createing a server instance
    remote_server = FTP()

    # making a connection
    server_connection = remote_server.connect('ftp.us.debian.org')
    print(server_connection)

    '''
    # checking the connection
    welcome = remote_server.getwelcome()
    print(welcome)
    '''
    # login
    server_login = remote_server.login()
    print(server_login)

    log.logger.info("server login status: ", server_login)

    # check the preesent working directory
    def current_directory():
        return remote_server.pwd()

    # change working directory to Pub
    def change_directory(path: str):
        new_directory = remote_server.cwd(path)
        # calling to know current working directory function
        return current_directory()

    # use the shutil to move the files
    def move_files(local_dir:str,file:str):
        remote_dir = "D:\\autocad"
        try:
            moving_status = shutil.move(os.path.join(local_dir,file),remote_dir)
            log.logger.info("shutil used to move files ",moving_status)
        except shutil.Error as e:
            #print(e)
            # logging.exception("exception occured")
            log.logger.error("Exception occured",exc_info=True)

    """
    # check the nlst
    for item in remote_server.nlst():
        print(item)
    """
    # download the files
    # def download_to_local(path):
    def download_to_local():
        # calling the change directory function
        new_working_dir = change_directory('debian')
        print(new_working_dir)
        for item in remote_server.nlst():
            # file_path = path+"\\"+item
            # with open(file_path,"wb") as file:
            with open(item,"wb") as file:
                try:
                    download_status = remote_server.retrbinary(f"RETR {item}",file.write)
                    log.logger.info("download_status")
                    # result = remote_server.retrbinary(f"RETR {item}",file.write) 
                    # print(result)
                except ftplib.error_perm as e:
                    # print(e)
                    # logging.exception("excepion occured")
                    log.logger.error("Exception occured",exc_info=True)
                    
            
            move_files(os.getcwd(),item)
        
        """
        code issue all files in the folder moving to new floder
        # using shutil module to move
        current_path = os.getcwd()
        if os.path.isdir(current_path):
            for n_file in os.listdir(current_path):
                if os.path.isfile(os.path.join(current_path,n_file)):
                    move_files(current_path,n_file)
                else: 
                    print(f"{n_file} it is not a file")
        """
    # checking the local directory existed or not
    local_directory = "D:\\autocad"
    if os.path.isdir(local_directory):
        # download_to_local(local_directory)
        download_to_local()

    else:
        print(f"{local_directory} does not exist")



    remote_server.quit()

    global running
    running = False
    print("stopped")
    log.logger.info("automation schudule job stopped")
    return schedule.CancelJob


schedule.every(10).minutes.do(automate_file_trnasfer)

# schedule.every().hour.do(automate_file_trnasfer)

# schedule.every(2).hours.do(automate_file_trnasfer)

# schedule.every().day.do(automate_file_trnasfer)

# schedule.every(2).days.do(automate_file_trnasfer)

# schedule.every().day.at("00:00").do(automate_file_trnasfer)

# schedule.every().monday.do(automate_file_trnasfer)

# schedule.every(5).to(10).hours.do(automate_file_trnasfer)

# schedule.every().tuesday.at("18:00").do(automate_file_trnasfer)
while running:
    schedule.run_pending()
    time.sleep(1)
