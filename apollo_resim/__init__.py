import os
import time
from pathlib import Path

from cyber_record.record import Record
from loguru import logger

from apollo_container.container import ApolloContainer
from apollo_container.map_service import MapService


def load_routing_request(path: str):
    r = Record(path)
    for _, msg, t in r.read_messages('/apollo/routing_request'):
        x, y, h = (
            msg.waypoint[0].pose.x,
            msg.waypoint[0].pose.y,
            msg.waypoint[0].heading,
        )
        return (x, y), h

    raise Exception('Routing coordinate not found')


def get_scenario_length(path: str):
    r = Record(path)
    start = r.get_start_time() / 1e9
    end = r.get_end_time() / 1e9
    return end - start


def re_simulate(
    apollo_root: str,
    container_name: str,
    start_script: str,
    map_bin: str,
    src: str,
    dst: str,
    remove_container: bool = True
):
    if Path(dst).exists():
        raise FileExistsError(f'Destination file {dst} exists!')
    ms = MapService()
    ms.load_map_from_file(map_bin, load_only=True)

    ctn = ApolloContainer(
        apollo_root,
        container_name,
    )
    ctn.start_container(start_script)
    ctn.start_dreamview()
    logger.debug(f'Dreamview running at http://{ctn.container_ip}:8888')

    ctn.copy_file_from_host(
        src, f"/home/{os.environ.get('USER')}/apollo_resim/input.00000"
    )

    (x, y), h = load_routing_request(src)
    total_t = get_scenario_length(src)

    logger.debug(f'{ctn.ctn_name} initializing scenario.')
    ctn.stop_ads_modules()
    ctn.stop_sim_control()
    ctn.start_sim_control(x, y, h)
    ctn.start_ads_modules()
    logger.debug(f'{ctn.ctn_name} running scenario.')
    ctn.start_recorder(f"/home/{os.environ.get('USER')}/apollo_resim/output")
    ctn.start_replay(f"/home/{os.environ.get('USER')}/apollo_resim/input.00000")
    time.sleep(total_t + 5)
    logger.debug(f'{ctn.ctn_name} finished scenario.')
    ctn.stop_recorder()
    ctn.stop_replay()
    ctn.stop_ads_modules()
    ctn.stop_sim_control()
    logger.debug(f'{ctn.ctn_name} reset complete.')
    time.sleep(5)

    result = ctn.copy_file_to_host(
        f"/home/{os.environ.get('USER')}/apollo_resim/output.00000", dst
    )

    if result.returncode != 0:
        logger.error(f"return code: {result.returncode}")
        logger.error("stderr: result.stderr")
        raise Exception(result.stderr)

    if remove_container:
        ctn.rm_container()
    # clean_apollo_logs(apollo_root)
