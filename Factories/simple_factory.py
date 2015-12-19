from httplib import HTTPConnection
from ftplib import FTP


class SimpleFactory(object):
    @staticmethod   # This decorator allows to run method without class instance
                    # e.i. SimpleFactory.build_connection
    def build_connection(protocol):
        if protocol == 'http':
            return HTTPConnection()
        elif protocol == 'ftp':
            return FTP()
        else:
            raise RuntimeError('Unknown protocol: {}'.format(protocol))

if __name__ == '__main__':
    protocol = raw_input('Which ptocol to use? (http or ftp): ')
    protocol = SimpleFactory.build_connection(protocol)
    protocol.connect()
    print protocol.getresponse()
