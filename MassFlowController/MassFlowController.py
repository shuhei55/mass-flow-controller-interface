import threading

import serial


class MFC:

  def __init__(self, port, baudrate):
    self.m_serial = serial.Serial(port, baudrate)
    self.is_communicate = False
    self.current_flow_list = [0, 0, 0]
    self.target_flow_list = [0, 0, 0]
    self.MAX_NUM = 255
    self.MIN_NUM = 0
    self.run_communication()

  def __del__(self):
    del self.m_serial

  def set_target(self, target_list: list):
    for i in range(3):
      self.target_flow_list[i] = clamp(target_list[i], self.MIN_NUM,
                                       self.MAX_NUM)

  def get_target(self):
    return self.target_flow_list

  def get_current_flow_list(self):
    return self.current_flow_list

  def communication_func(self):
    self.is_communicate = True
    while self.is_communicate:
      self.m_serial.reset_input_buffer()
      self.m_serial.reset_output_buffer()
      self.m_serial.write(
          bytes(
              str(f"{int(self.target_flow_list[0]):03}{int(self.target_flow_list[1]):03}{int(self.target_flow_list[2]):03}"
                 ).encode()))
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
