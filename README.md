Enclosure
=========

Zookeeper configuration tool

Enclosure was built to model a set of logical environments inside Zookeeper.
It models these environments based on an, on disk, file structure used to store the configuration information.
The Enc library was written to allow client applications to join these environments, download the configuration information and react to changes in that configuration (usually by reloading it into the process)

Enclosure relies on a handful of conventions:
* Each directory will store a single file < 1MB that holds the configuration information.
* A client will join the environment as an ephemeral node
* A client can store information about itself against its own node

To model an environment on a folder structure run:
./Enclosure.py -s [_ZK server ip_] -mod [_root node directory_]

This will build a znode for each directory inside the root node directory.  The first file in that directory will be loaded into the znode (no error handling for large files at the moment).

e.g: _./Enclosure.py -s 127.0.0.1:2181 -mod ~/Documents/enctest
run against a directory structured like so:
```
~/Documents/enctest
└── environments
    ├── dev
    │   └── test-app
    ├── prod
    └── test
```

Would build an /environments node with 3 children (dev, test & prod) and the file "test-app" would have it's data loaded into the dev node.

Enc
=========

Enc is a very simple library using an existing ZooKeeper client that allows an application to join one of the logical environment discussed above.
The join method in: Enc.py will create an ephemeral node under the provided environment for the supplied name. If that name ends in a hyphen then the node name will be sequential (see ZooKeeper documentation). An optional callback can be provided, this function will fire once, initially, then once each time the parent nodes data is set, typically this function is what will be used to load the configuration from the parent node into our application.  This method passes back the ZooKeeper client it used to connect to the server.

e.g: calling:
```python
Enc.join(   server ='127.0.0.1:2181',
            environment ='environments/dev',
            name = 'test-py',
            on_parent_environment_change=load-config)
```
Would create an ephemeral znode under /environments/dev called /test-py
that would call the load-config method whenever /environments/dev's data was changed.
