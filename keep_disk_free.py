import argparse
import logging
import os
import shutil


def main():
    argparser = argparse.ArgumentParser(
        description='Delete files with earliest modification date'
                    ' until a minimum of --free-bytes are available on the respective disk')
    argparser.add_argument('--free-bytes', type=int, required=True)
    argparser.add_argument('root_dir_path', metavar='ROOT_DIR')
    args = argparser.parse_args()
    logging.basicConfig(level=logging.DEBUG,
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
    removed_files_counter = 0
    for file_path in sorted(file_paths, key=lambda p: os.stat(p).st_mtime):
        if shutil.disk_usage(args.root_dir_path).free >= args.free_bytes:
            break
        os.remove(file_path)
        logging.debug('Removed file %s', file_path)
        removed_files_counter += 1
    logging.info('Removed %d files', removed_files_counter)


if __name__ == '__main__':
    main()
