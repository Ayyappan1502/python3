import multiprocessing
import os

def download_file(url,output):
    os.system('wget -o {output} {url}'.format(output=output , url=url))
 
if __name__ == "__main__":
    try: 
        while True: 
            multiprocessing.Process(target=download_file, args=(input("Enter a file :"),input("output a file :"))).start()
    except KeyboardInterrupt as e :
        print("Exiting...")