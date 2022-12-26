import threading

import serial

class SerialDummy:
  def __init__(self):
    print("Dummy Serial is running!!!!!")
  
  def __del__(self):
    print("Dummy Serial stoped !!!!!")

  def reset_input_buffer(self):
    pass

  def reset_output_buffer(self):
    pass

  def write(self, data):
    pass

  def readline(self):
    return b"1234567890"
  
class MFC:
  def __init__(self, port, baudrate, dummy=False):
    print("MFC start")
    if not dummy:
      self.m_serial = serial.Serial(port, baudrate)
      self.is_communicate = False
      self.is_updated = True
      self.current_flow_list = [0, 0, 0]
      self.target_flow_list = [0, 0, 0]
      self.MAX_NUM = 255
      self.MIN_NUM = 0
    else:
      self.m_serial = SerialDummy()
      self.is_communicate = False
      self.is_updated = True
      self.current_flow_list = [0, 0, 0]
      self.target_flow_list = [0, 0, 0]
      self.MAX_NUM = 255
      self.MIN_NUM = 0

  def __del__(self):
    del self.m_serial

  def set_target(self, target_list: list):
    for i in range(3):
      self.target_flow_list[i] = clamp(target_list[i], self.MIN_NUM,
                                       self.MAX_NUM)
    self.is_updated = True

  def get_target(self):
    return self.target_flow_list

  def get_current_flow_list(self):
    return self.current_flow_list

  def communication_func(self):
    self.is_communicate = True
    while self.is_communicate:
      self.m_serial.reset_input_buffer()
      self.m_serial.reset_output_buffer()
      if self.is_updated:
        self.m_serial.write(
            bytes(
                str(f"{int(self.target_flow_list[0]):03}{int(self.target_flow_list[1]):03}{int(self.target_flow_list[2]):03}"
                  ).encode()))
        self.is_updated = False
      data = self.m_serial.readline()
      self.current_flow_list[0] = int(data[:3])
      self.current_flow_list[1] = int(data[3:6])
      self.current_flow_list[2] = int(data[6:9])

  def run_communication(self):
    if not self.is_communicate:
      threading.Thread(target=self.communication_func).start()

  def stop_communication(self):
    self.is_communicate = False


def clamp(n, smallest, largest):
  return int(max(smallest, min(n, largest)))
