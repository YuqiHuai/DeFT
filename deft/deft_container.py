import os
import subprocess
from pathlib import Path
from typing import List

import docker


class DeFTContainer:
    def __init__(self, apollo_dir: str, user: str):
        """
        Initialize the DeFTContainer.

        Args:
            apollo_dir (str): The directory where Apollo is located.
            user (str): The user to run the container as.
        """
        self.apollo_dir = Path(apollo_dir)
        self.user = user
        self.container_name = f'apollo_dev_{user}'
        self.client = docker.from_env()

    def install(self, show_container_output=False):
        """
        Install the DeFT container.

        Args:
            show_container_output (bool): Whether to show the container output.
        """
        if not self.apollo_dir.exists():
            git_url = 'git@github.com:YuqiHuai/BaiduApollo.git'
            self._execute_command(
                [
                    'git',
                    'clone',
                    '--branch',
                    'deft',
                    '--single-branch',
                    git_url,
                    self.apollo_dir,
                ],
                show_container_output=show_container_output,
            )

        subprocess.run(['git', 'clean', '-fd'], cwd=self.apollo_dir, check=True)
        subprocess.run(['git', 'restore', '.'], cwd=self.apollo_dir, check=True)
        subprocess.run(['git', 'pull'], cwd=self.apollo_dir, check=True)

        self.start()
        command = [
            'docker',
            'exec',
            '-u',
            self.user,
            self.container_name,
            'sh',
            '-c',
            'bash /apollo/apollo.sh build deft',
        ]
        self._execute_command(
            command=command, show_container_output=show_container_output
        )

    def _get_container_object(self):
        try:
            return self.client.containers.get(self.container_name)
        except docker.errors.NotFound:
            return None

    def set_map(self, map_name: str):
        """
        Set the map directory for the DeFT container.

        Args:
            map_name (str): The name of the map to set.
        """
        flagfile = Path(
            self.apollo_dir, 'modules', 'common', 'data', 'global_flagfile.txt'
        )
        new_line = f'--map_dir=/apollo/modules/map/data/{map_name}'
        with open(flagfile, 'a') as fp:
            fp.write('\n' + new_line + '\n')

    def is_running(self) -> bool:
        """
        Check if the DeFT container is running.

        Returns:
            bool: True if the container is running, False otherwise.
        """
        ctn = self._get_container_object()
        return ctn and ctn.status == 'running'

    def start(self, show_container_output=False):
        """
        Start the DeFT container.

        Args:
            show_container_output (bool): Whether to show the container output.
        """
        my_env = os.environ.copy()
        my_env['USER'] = self.user
        my_env['DEV_CONTAINER'] = self.container_name
        command = [
            'bash',
            str(Path(self.apollo_dir, 'docker', 'scripts', 'dev_start.sh')),
            # '--fastest',
        ]
        subprocess.run(command, check=True, capture_output=True, text=True, env=my_env)
        self._execute_command(
            ['docker', 'exec', '-u', self.user, self.container_name, 'bazel', 'info'],
            show_container_output,
        )

    def stop(self):
        """
        Stop the DeFT container.
        """
        if self.is_running():
            ctn = self._get_container_object()
            ctn.stop()

    def remove(self):
        """
        Remove the DeFT container.
        """
        ctn = self._get_container_object()
        if ctn:
            ctn.remove()

    def load_testdata(self, testdata_dir: Path):
        """
        Load test data into the DeFT container.

        Args:
            testdata_dir (Path): The directory containing the test data to load.
        """
        docker_path = Path(f'/home/{self.user}/deft/testdata')
        self._execute_command(
            [
                'docker',
                'exec',
                '-u',
                self.user,
                self.container_name,
                'mkdir',
                '-p',
                str(docker_path.parent),
            ]
        )
        self._execute_command(
            [
                'docker',
                'exec',
                '-u',
                self.user,
                self.container_name,
                'rm',
                '-rf',
                str(docker_path.parent),
            ]
        )
        self._execute_command(
            [
                'docker',
                'exec',
                '-u',
                self.user,
                self.container_name,
                'mkdir',
                str(docker_path.parent),
            ]
        )
        copy_command = [
            'docker',
            'cp',
            testdata_dir,
            f'{self.container_name}:{docker_path}',
        ]
        subprocess.run(copy_command, check=True, capture_output=True)

    def save_testdata(self, testdata_dir: Path):
        """
        Save test data from the DeFT container.

        Args:
            testdata_dir (Path): The directory to save the test data to.
        """
        docker_path = Path(f'/home/{self.user}/deft/testdata')
        copy_command = [
            'docker',
            'cp',
            f'{self.container_name}:{docker_path}',
            testdata_dir,
        ]
        subprocess.run(copy_command, check=True, capture_output=True)

    def save_genhtml(self, target_dir: Path):
        """
        Save the generated HTML reports from the DeFT container.

        Args:
            target_dir (Path): The directory to save the generated HTML reports to.
        """
        docker_path = Path(f'/home/{self.user}/deft/genhtml')
        # check if docker path exists
        cmd = [
            'docker',
            'exec',
            '-u',
            self.user,
            self.container_name,
            'sh',
            '-c',
            f'test -d {docker_path} && echo exists',
        ]
        check_exists = subprocess.run(cmd, capture_output=True, text=True)
        if check_exists.stdout.strip() != 'exists':
            return
        copy_command = [
            'docker',
            'cp',
            f'{self.container_name}:{docker_path}',
            target_dir,
        ]
        subprocess.run(copy_command, check=True, capture_output=True)

    def _execute_command(self, command: List[str], show_container_output=False):
        """
        Prepares and executes a command in the DeFT container.

        Args:
            command (List[str]): The command to execute.
            show_container_output (bool): Whether to show the container output.
        """
        my_env = os.environ.copy()
        my_env['USER'] = self.user
        try:
            if not show_container_output:
                subprocess.run(
                    command,
                    check=True,
                    env=my_env,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            else:
                subprocess.run(command, check=True, env=my_env)
        except subprocess.CalledProcessError as e:
            raise Exception(
                f'Command failed with exit code {e.returncode}: '
                f'{e.stderr.decode().strip()}'
            )

    def deft_run_tests(self, show_container_output=False):
        """
        Execute the DeFT test suite.

        Args:
            show_container_output (bool): Whether to show the container output.
        """
        command = [
            'docker',
            'exec',
            '-u',
            self.user,
            self.container_name,
            'bash',
            '/apollo/modules/deft/deft.sh',
        ]
        self._execute_command(command, show_container_output)

    def deft_coverage(self, show_container_output=False):
        """
        Obtain code coverage information from the DeFT container.

        Args:
            show_container_output (bool): Whether to show the container output.
        """
        command = [
            'docker',
            'exec',
            '-u',
            self.user,
            self.container_name,
            'bash',
            '/apollo/modules/deft/coverage.sh',
        ]
        self._execute_command(command, show_container_output)
