
import subprocess
import shutil
from os import path


def setup_conf():
    if not path.exists('./.env'): 
        shutil.copyfile('./.env.example', './.env')
    
    
class DockerCompose:
    def __init__(self):
        self.__docker_compose_files = []
        
    def add_docker_compose(self, docker_compose_file):
            self.__docker_compose_files.append(docker_compose_file)
            
    def get_docker_compose_files(self):
        return self.__docker_compose_files
    

def run_all_services():
    compose = DockerCompose()
    
    compose.add_docker_compose('docker-compose.yml')
    
    print(compose.get_docker_compose_files())
    
    subprocess.run([
        f"sudo docker compose {' '.join(map(lambda x: f'-f {x}', compose.get_docker_compose_files()))} up -d"
    ], shell=True)
    
def docker_up_all():
    setup_conf()
    run_all_services()