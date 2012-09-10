Enclosure
=========

ZooKeeper configuration tool

Run ./Enclosure.py -s [_ZK server ip_] -mod [_root node directory_]
This will build a znode for each directory inside the provided root node directory.
The first file in that directory will have it's data loaded into the znode (no error handling for large files at the moment).

e.g: _./Enclosure.py -s 127.0.0.1:2181 -mod ~/Documents/enctest
run against a directory structured like so:
```
~/Documents/enctest
└── environments
    ├── dev
    │   └── demo
    ├── prod
    └── test
```

Would build an /environments node with 3 children (dev, test & prod) and the file "demo" would have it's data loaded into the dev node.

Enc
=========

The join method in: Enc-py/Enc.py will create an ephemeral node under the provided environment for the supplied name. If that name ends in a hyphen then the node name will be sequential. An optional callback can be provided, this funtion will fire once, initially, then once each time the parent nodes data is set. This method passes back the ZooKeeper client it used to connect to the server.

e.g: calling:
```python
Enc.join(   server ='127.0.0.1:2181',
            environment ='environments/dev',
            name = 'test-py',
            on_parent_environment_change=foo)
```
Would create an ephemeral znode under /environments/dev called /test-py
that would call the foo method whenever /environments/dev's data was changed.
