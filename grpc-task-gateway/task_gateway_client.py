import grpc

from task_gateway_pb2 import Task
from task_gateway_pb2_grpc import TaskGatewayStub


def main():
    channel = grpc.insecure_channel('localhost:50051')
    client = TaskGatewayStub(channel)

    with open('task_gateway.proto', 'rb') as task_file:
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


if __name__ == '__main__':
    try:
        main()
    except:
        raise
