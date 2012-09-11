import Enc
import unittest


class TestEnc (unittest.TestCase):

    def setUp(self):
        self.foo_was_called = False

    def foo(self, data, stat):
        print "parent data -->" + data
        self.foo_was_called = True

    def test_respond_to_change_in_parent_node_data(self):
        parent_node = 'environments/dev'

        zk = Enc.join(
            server ='127.0.0.1:2181',
            environment ='environments/dev',
            name = 'test-py',
            on_parent_data_change=self.foo)

        print "original parent data --> " +  zk.get(parent_node)[0]

        #set the data of the parent node
        zk.set(parent_node,data= "message : hello james")
        self.assertTrue(self.foo_was_called,msg= "callback method was not called on parent node data change")
        zk.stop()


    if __name__ == '__main__':
        unittest.main()