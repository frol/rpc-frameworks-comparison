typedef i32 id
typedef string datetime

struct Task {
    1: id identifier = 0,
    2: string name,
    3: string filename,
    4: binary file,
    5: datetime created_at,
}

exception TaskException {
    1: string reason,
}

service TaskGateway {
    Task create_task(1:Task task) throws(1:TaskException e)
}
