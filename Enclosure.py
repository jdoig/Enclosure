import argparse
import os
from kazoo.client import KazooClient
from kazoo.exceptions import NodeExistsException

def main():
    parser = argparse.ArgumentParser(description='Enclosure: environment management tool')
    parser.add_argument('-s', '--server', help='the ZooKeeper server to use', required=True)
    parser.add_argument('-mod','--model', help='model the environments on a directory structure from the file system', metavar='file-path')

    args = parser.parse_args()

    if args.model:
        model_environments(args.server, args.model)

def model_environments(ip_address, file_path):
    zk = KazooClient(hosts=ip_address)
    zk.start()
    for root, dirs, files in os.walk(file_path):
        node_path = root.replace(os.path.dirname(file_path),'') # trim root from path, except parent
        try:
            zk.create(node_path, makepath=True) # make parent directories as needed

        except NodeExistsException:
            print "%s already exists" %node_path

        if len(files) > 0:
            file = os.path.join(root,files[0])
            __load_file_into_znode(zk, file, node_path)

    zk.stop()

def __load_file_into_znode(client, file_path, node_path):
    with open(file_path, mode='rb') as file:
        data = file.read()
        client.set(node_path, data)

if __name__ == "__main__":
    main()