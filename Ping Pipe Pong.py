from multiprocessing import Process, Pipe
from time import sleep
from os import getpid

def ponger(receiver,response):
  while True:
      msg = receiver.recv()
  #receive a message
      print(f"Process{getpid()} got message: {msg}")
  # print it as f"Process{getpid()} got message: {msg}"
      sleep(2)
  # sleep before responding
      receiver.send(response)
  # send response message back

if __name__ == "__main__":
    receiver_1, responser_1 = Pipe()
    # create 2 pipes
    process_1 = Process(target=ponger, args=(receiver_1,'Ping'))
    process_2 = Process(target=ponger, args=(responser_1,'Pong'))

    process_1.start()
    process_2.start()

    responser_1.send('Pong!')


# create 2 processes that will use ponger, give them different sides of pipes

# they also need a specific message (either ping or pong)
# start both processes
# initiate ping-pong by sending first message to one of the pipes