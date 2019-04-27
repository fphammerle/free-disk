import argparse
import datetime
import logging
import os
import shutil


def main():
    argparser = argparse.ArgumentParser(
        description='Delete files with earliest modification date'
                    ' until a minimum of --free-bytes are available on the respective disk')
    argparser.add_argument('-d', '--debug', action='store_true')
    argparser.add_argument('--free-bytes', type=int, required=True)
    argparser.add_argument('root_dir_path', metavar='ROOT_DIR')
    args = argparser.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s',
                        datefmt='%Y-%m-%dT%H:%M:%S%z')
    disk_usage = shutil.disk_usage(args.root_dir_path)
    logging.debug(disk_usage)
    if disk_usage.free >= args.free_bytes:
        logging.debug('Requirement already fulfilled')
        return
    file_paths = [os.path.join(dirpath, filename)
                  for dirpath, _, filenames in os.walk(args.root_dir_path)
                  for filename in filenames]
    file_mtime_paths = [(os.stat(p).st_mtime, p) for p in file_paths]
    file_mtime_paths.sort()
    removed_files_counter = 0
    last_mtime = None
    for file_mtime, file_path in file_mtime_paths:
        if shutil.disk_usage(args.root_dir_path).free >= args.free_bytes:
            break
        os.remove(file_path)
        logging.debug('Removed file %s', file_path)
        removed_files_counter += 1
        last_mtime = file_mtime
    if removed_files_counter == 0:
        logging.warn('No files to remove')
    else:
        logging.info('Removed %d file(s) with modification date <= %s', removed_files_counter,
                     datetime.datetime.utcfromtimestamp(last_mtime).isoformat('T'))


if __name__ == '__main__':
    main()
