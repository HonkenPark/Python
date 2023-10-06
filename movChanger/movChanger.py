import os
import shutil
import exifread
from datetime import datetime
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
import pytz
from datetime import timedelta
import shutil

def get_media_creation_date(filename):
    parser = createParser(filename)
    if not parser:
        return None

    metadata = extractMetadata(parser)
    if metadata:
        creation_date = metadata.get('creation_date')
        if creation_date:
            # 날짜를 하루 증가
            next_day = creation_date + timedelta(days=1)
            date_str = next_day.strftime('%Y%m%d')
            return date_str

    return None

def rename_mov_files():
    # 현재 디렉토리에서 모든 .MOV 파일을 찾음
    for filename in os.listdir():
        if filename.endswith('.MOV'):
            new_name = get_media_creation_date(filename)
            print(new_name)
            if new_name:
                new_name += '.MOV'
                # 파일 이름 변경
                shutil.copy(filename, 'TMP.MOV')
                os.rename('TMP.MOV', new_name)
                print(f'Renamed {filename} to {new_name}')

if __name__ == "__main__":
    rename_mov_files()