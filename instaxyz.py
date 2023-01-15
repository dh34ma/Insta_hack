import os

if __name__ == "__main__":

   try:

       os.system("git pull");os.system('xdg-open ')

       __import__("run").__main__()

   except Exception as e: 

       exit(str(e))
