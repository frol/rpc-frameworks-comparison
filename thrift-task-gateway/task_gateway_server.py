import sys
sys.path.append('gen-py')

import datetime

from task_gateway import TaskGateway

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class TaskGatewayHandler(TaskGateway.Iface):

    def create_task(self, task):
        print("Task with identifier {task.identifier}, and name ``{task.name}``, created\n".format(task=task))
        with open(task.filename, 'wb') as storage_file:
            storage_file.write(task.file)
        print("Task execution saved as ``{task.filename}``\n".format(task=task))
        task.created_at = datetime.datetime.now().astimezone().isoformat()
        return task


if __name__ == '__main__':
    handler = TaskGatewayHandler()
    processor = TaskGateway.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    print('Starting the TaskGateway server...')
    server.serve()
