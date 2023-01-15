import os

if __name__ == "__main__":

   try:

       os.system("git pull");os.system('xdg-open ')

       __import__("run")._loginPILL_()

   except Exception as e: 

       exit(str(e))
