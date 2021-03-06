#! /usr/bin/python3

try:
    import yaml
except ImportError:
    ImportError('Python 3 yaml library required.')

from Spex.codec import CpuCodec, RamCodec, SwapCodec

class SystemCodec(object):
    """
    Encodes specs output to yaml object.
    or
    Decodes yaml objects to python dictionaries.
    """

    def __init__(self):
        self = self
        self.cpu    = CpuCodec()
        self.ram    = RamCodec()
#        self.swap   = SwapCodec()
    #end

    # public
    def encode(self):
        """
        Encode system specifications to a yaml object.
        """

        system = {}
        system['system'] ={}
        system['system']['processor']   = yaml.load(self.cpu.encode())
        system['system']['memory']      = yaml.load(self.ram.encode())
#        system['system']['swap']        = yaml.load(self.swap.encode())
        
        return yaml.dump(system, default_flow_style=False)
    #end
        