Enclosure
=========

ZooKeeper configuration tool

Run ./Enclosure.py -s [_ZK server ip_] -mod [_root node directory_]
This will build a znode for each directory inside the provided root node directory.
The first file in that directory will have it's data loaded into the znode (no error handling for large files at the moment).

The join method in: Enc-py/Enc.py will create an ephemeral node under the provided environment for the supplied name. If that name ends in a hyphen then the node name will be sequential. An optional callback can be provided, this funtion will fire once, initially, then once each time the parent nodes data is set. This method passes back the ZooKeeper client it used to connect to the server.
