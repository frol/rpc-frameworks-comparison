module task_gateway
{
    sequence<byte> ByteSeq;

    struct DateTime
    {
        string iso8601;
    }

    struct Task
    {
        int identifier;
        string name;
        string filename;
        ByteSeq file;
        DateTime created_at;
    }

    interface TaskGateway
    {
        Task create_task(Task task);
    }
}
