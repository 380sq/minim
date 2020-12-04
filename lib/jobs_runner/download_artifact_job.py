import json
from os import path
from time import sleep
from uuid import uuid1

from lib.helpers import get_temp_folder
from lib.socket import send_io_message


def download_artifact(job, step, request):
    print('start downloading artifact >>>>> ')
    name = path.join(get_temp_folder(), 'artifact-' + str(uuid1()))
    with request as r:
        if r.status_code == 404:
            send_io_message(json.dumps({"type": "error", "details": "download"}))
            return None
        sleep(5)
        with open(name, 'wb') as f:
            total = int(r.headers['Content-Length'])
            progress = 0
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    progress += len(chunk)
                    print(str(progress / total))
                    send_io_message({"type": "error", "details": {"job_id": job['id'], "step": step,
                                                                  "progress": str(len(chunk) / total)}})
        return "done"
