# Copyright (c) 2019 Matija Mazalin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Thread safe base card multiplexer interface."""
__author__ = "Matija Mazalin"
__email__ = "matija.mazalin@abrantix.com"
__license__ = "MIT"


from Parsers.ParseXml import XmlParser
from Exception.Exception import Error
from Base.DeviceBase import DeviceBase;
from Message.HardwareMagics import HardwareMagics;
import traceback;


class BaseMultiplexer(DeviceBase):

    tag = "invalid";
    magic = HardwareMagics.Invalid;

    def __init__(self, id, mac_address, enable_statistics=False):
        super().__init__(id, XmlParser.parse_muxs, enable_statistics);
        self.mac_address = bytearray.fromhex(mac_address);
  
    def send_command(self, action):
        Result = False
        try:
           action_value = int(self.layout[action].Value);
           send_to = self.device.get_sender_for_device(self.mac_address);
           Result = send_to.set_port(action_value);
           self.log_info("execution of {} was successful".format(action))
        except TimeoutError as e:
            self.log_error("device {} did not respond in time".format(self.get_mac_address()));
        except KeyError as e:
            pass;
        except AssertionError as e:
            self.log_error("device {} returned an error".format(self.get_mac_address()));
        except:
            traceback.print_exc()
            self.log_error("device {} returned a general error".format(self.get_mac_address()));

        return Result;

    def get_mac_address(self):
        return ''.join('{:02x}:'.format(x) for x in self.mac_address)[:-1];

        






