import threading,os


def rename(old, new):
    os.rename(old,new)

if __name__ == '__main__':
    path = 'test'
    for index,file in enumerate(os.listdir(path)):
        subthread = threading.Thread(target=rename, args=(f'{path}/{file}',f'{path}/{index+1}.txt'))
        subthread.start()
        