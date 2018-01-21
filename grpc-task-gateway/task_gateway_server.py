from concurrent import futures
import datetime
import time

import grpc

import task_gateway_pb2
import task_gateway_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class TaskGateway(task_gateway_pb2_grpc.TaskGatewayServicer):

    def create_task(self, task, context):
        print("Task with identifier {task.identifier}, and name ``{task.name}``, created\n".format(task=task))
        with open(task.filename, 'wb') as storage_file:
            storage_file.write(task.file)
        print("Task execution saved as ``{task.filename}``\n".format(task=task))
        task.created_at.iso8601 = datetime.datetime.now().astimezone().isoformat()
        return task


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    task_gateway_pb2_grpc.add_TaskGatewayServicer_to_server(TaskGateway(), server)
    server.add_insecure_port('[::]:50051')
    print('Starting the TaskGateway server...')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
    print('Done')


if __name__ == '__main__':
    main()
