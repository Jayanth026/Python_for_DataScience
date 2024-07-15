'''
Multiprocessing -> creating multiple processors and working on it 

'''

import time 
import multiprocessing
import os 

def india():
  print(f'C1 Processor id : {os.getpid()}')
  for i in range(1,11):
    time.sleep(0.5)
    print('india->',i)


def usa():
  print(f'C2 Processor id : {os.getpid()}')
  for i in range(51,61):
    time.sleep(0.5)
    print('usa->',i)


if __name__ == "__main__":
    starting_time = time.time()
    print(f'Main Processor is Started and ID : {os.getpid()}')

    c1 = multiprocessing.Process(target=india,args=())
    c2 = multiprocessing.Process(target=usa,args=())

    c1.start()
    c2.start()

    c1.join()
    c2.join()

    print('I am exisiting ')
    print(f'Total time : {time.time() -  starting_time}')



