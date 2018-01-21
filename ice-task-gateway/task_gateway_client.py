import Ice

import task_gateway

def main():
    with Ice.initialize() as communicator:
        base = communicator.stringToProxy("task_gateway:default -p 10000")
        client = task_gateway.TaskGatewayPrx.checkedCast(base)
        if not client:
            raise RuntimeError("Invalid proxy")

        with open('task_gateway.ice', 'rb') as task_file:
            task = task_gateway.Task(
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
