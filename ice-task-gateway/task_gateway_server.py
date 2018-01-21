import datetime

import Ice

import task_gateway


class TaskGateway(task_gateway.TaskGateway):

    def create_task(self, task, current=None):
        print(current)
        print("Task with identifier {task.identifier}, and name ``{task.name}``, created\n".format(task=task))
        with open(task.filename, 'wb') as storage_file:
            storage_file.write(task.file)
        print("Task execution saved as ``{task.filename}``\n".format(task=task))
        task.created_at.iso8601 = datetime.datetime.now().astimezone().isoformat()
        return task


if __name__ == '__main__':
    with Ice.initialize() as communicator:
        adapter = communicator.createObjectAdapterWithEndpoints("task_gateway", "default -p 10000")
        obj_instance = TaskGateway()
        adapter.add(obj_instance, communicator.stringToIdentity("task_gateway"))
        adapter.activate()

        print('Starting the TaskGateway server...')
        communicator.waitForShutdown()
