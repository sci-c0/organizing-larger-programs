import gzip

from demo_reader import util


extension = '.gz'
opener = gzip.open

if __name__ == '__main__':
    util.writer.main(opener)