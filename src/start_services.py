import os
import time
import subprocess
import core.ports as ports

def start_service(service, port):
    print(f'Starting {service} service..')
    return subprocess.Popen(
        ['uvicorn', f'services.{service}:app', '--host', '0.0.0.0', '--port', str(port)],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        )

def start():
    services = [
        {'file': 'text_processing', 'port': ports.TEXT_PROCESSING_PORT},
        {'file': 'preprocessing', 'port': ports.PRE_PROCESSING_PORT},
        {'file': 'indexing', 'port': ports.INDEXING_PORT},
        {'file': 'query_processing', 'port': ports.QUERY_PROCESSING_PORT},
        {'file': 'matching', 'port': ports.MATCHING_PORT},
        {'file': 'searching', 'port': ports.SEARCHING_PORT},
    ]

    processes = []

    for service in services:
        proc = start_service(service['file'], service['port'])
        processes.append(proc)
        time.sleep(3)
        print('--------------------------------')

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for proc in processes:
            proc.terminate()

if __name__ == '__main__':
    start()