sys.path = sys.path.append("..") # our fake sigrokdecode lives one dir upper

from pd import Decoder

class SD_card_(SPI_mode)():
  def __init__(self):
    self.sigrokDecoder = Decoder()
    pass

  def get_capabilities(self):
    pass

  def set_settings(self, settings):
    pass

  def decode(self, data):
    self.sigrokDecoder.processSPI(data)
    if (not self.packet == {}) :
        ret = self.generate_logic_result()
        self.packet = {}
        return ret
    pass