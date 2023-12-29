import multiprocessing

from data_collection.collection import data_collection_process
from conf_sync.main import conf_sync_process

if __name__ == "__main__":
    processes = []

    collection_process = multiprocessing.Process(target=data_collection_process)
    conf_sync_process = multiprocessing.Process(target=conf_sync_process)  # done
    # upload_process = multiprocessing.Process(target=data_sync_process)  # args=(2,)
    processes.append(collection_process)
    # processes.append(conf_sync_process)
    # processes.append(upload_process)
    collection_process.start()
    # conf_sync_process.start()
    # upload_process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    print("All processes finished")
