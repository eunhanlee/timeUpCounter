from threading import Timer,Thread,Event
import time
import datetime

class perpetualTimer():

   def __init__(self,hFunction):
      self.t=1
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.t=1
      self.thread.start()

   def cancel(self):
      self.thread.cancel()