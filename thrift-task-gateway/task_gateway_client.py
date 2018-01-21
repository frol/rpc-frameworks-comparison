import sys
sys.path.append('gen-py')

from thrift import Thrift
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

from task_gateway.ttypes import Task
from task_gateway import TaskGateway


def main():
    transport = TSocket.TSocket('localhost', 9090)
    transport = TTransport.TBufferedTransport(transport)

    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    
    client = TaskGateway.Client(protocol)

    transport.open()

    with open('task_gateway.thrift', 'rb') as task_file:
        task = Task(
            identifier=1,
            name="First experimental task",
            filename='some_file.txt',
            file=task_file.read(),
        )
    print("Creating task %s..." % task)
    created_task = client.create_task(task)
    print("Task was created at %s" % created_task.created_at) 
    print("Done!")

    transport.close()

if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)
