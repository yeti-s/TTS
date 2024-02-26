#@title Install Dependencies (and load your cached install if it exists to boost times)
# Required Libraries
import os
import tarfile

WORKING_DIR = '/workspace'
CACHED_RVC = f'{WORKING_DIR}/CachedRVC.tar.gz'
WAV2LIP = f'{WORKING_DIR}/wav2lip-cache.tar.gz'

# Unzip EVC
with tarfile.open(WAV2LIP, 'r:gz') as tar:
    for member in tar.getmembers():
        target_path = os.path.join('/', member.name)
        try:
            tar.extract(member, '/')
        except:
            pass

with tarfile.open(f'{WORKING_DIR}/wav2lip-HD.tar.gz') as tar:
    tar.extractall(f'{WORKING_DIR}')


with tarfile.open(CACHED_RVC, 'r:gz') as tar:
    for member in tar.getmembers():
        target_path = os.path.join(WORKING_DIR, member.name)
        try:
            tar.extract(member, WORKING_DIR)
        except Exception as e:
            print('Failed to extract a file (this isn\'t normal)... forcing an update to compensate')
    print(f'Extraction of {CACHED_RVC} to {WORKING_DIR} completed.')
