from queue import Queue
import random
import time

# create a request with a unique number and a random number of operations.
class Request:
  def __init__(self, nmbr):
    self.nmbr = nmbr
    self.operations = random.randint(1, 5)


# create a queue of requests.
class Process:
  def __init__(self):
    self.queue = Queue()

  def generate_request(self, request):
    self.queue.put(request)

  def process_request(self):
    if self.queue.empty():
      print('Черга пуста')
    else:
      current_reques = self.queue.get()
      print(f"process request {current_reques.nmbr} with {current_reques.operations} operations")
      time.sleep(1)# service time.

process = Process()
counter = 0

while True: # infinite loop for automatic generation and processing of requests.
  counter += 1
  new_request = Request(f"request-{counter}")
  process.generate_request(new_request)
  process.process_request()