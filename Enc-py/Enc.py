from kazoo.client import KazooClient

def join(server, environment, name, on_parent_data_change = None):
    zk = KazooClient(hosts=server)
    zk.start() # connect to zookeeper

    # create an ephemeral znode under the given environment,
    # if the given name ends in '-' make it sequential.
    zk.create( path = '{0}/{1}'.format(environment, name),
               ephemeral = True,
               sequence = (name[-1:] == '-'))

    # if a callback was provided trigger it whenever parents data changes...
    # for example to update variables on config changes.
    if on_parent_data_change:
        zk.DataWatch(environment, func = on_parent_data_change)

    #hand zookeeper client back to caller
    return zk
