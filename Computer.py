import time
import random
import math


class Computer:
  def __init__ (self, status = "Off", os = ["macOS"], model = "Macbook Pro", applications = ["Safari","Spotify","Discord","Steam","Pycharm","Netbeans"]):
    
    self.status = status
    self.os = os
    self.model = model
    self.applications = applications
    
  def open_pc(self):
    
     if self.status == "Off":
      print("Booting up...")
      time.sleep(1)
      self.status = "On"
      print("Your computer is turned on...")
            
     elif self.status == "On":
       print("The computer is already on...")
  
            
  def close_pc(self):
    
      if self.status == "On":
        print("Turning off your computer...")
        time.sleep(1)
        self.status = "Off"
        print("Your computer has been shut down...")
      
      elif self.status == "Off":
        print("The computer is already off.")
        
      
 
                  
        
        
    
