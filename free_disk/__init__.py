"""
Delete file with the oldest modification date
until a minimum of --free-bytes are available on the respective disk.
"""

import argparse
import datetime
import logging
import os
import shutil
import re

# https://en.wikipedia.org/wiki/Template:Quantities_of_bytes
DATA_SIZE_UNIT_BYTE_CONVERSION_FACTOR = {
    "B": 1,
    "kB": 10 ** 3,
    "KB": 10 ** 3,
    "MB": 10 ** 6,
    "GB": 10 ** 9,
    "TB": 10 ** 12,
    "KiB": 2 ** 10,
    "MiB": 2 ** 20,
    "GiB": 2 ** 30,
    "TiB": 2 ** 40,
}


def data_size_to_bytes(size_with_unit: str) -> int:
    match = re.match(r"^([\d\.]+)\s*([A-Za-z]+)?$", size_with_unit)
    if not match:
        raise ValueError("Unable to parse data size {!r}".format(size_with_unit))
    unit_symbol = match.group(2)
    if unit_symbol:
        try:
            byte_conversion_factor = DATA_SIZE_UNIT_BYTE_CONVERSION_FACTOR[unit_symbol]
        except KeyError:
            raise ValueError("Unknown data size unit symbol {!r}".format(unit_symbol))
    else:
        byte_conversion_factor = 1
    byte_size = float(match.group(1)) * byte_conversion_factor
    return int(round(byte_size, 0))


def main():
    argparser = argparse.ArgumentParser(description=__doc__)
    argparser.add_argument("-d", "--debug", action="store_true")
    argparser.add_argument(
        "--free-bytes",
        type=data_size_to_bytes,
        required=True,
        help="examples: 1024, 1024B, 4KiB, 4KB, 2TB",
    )
    argparser.add_argument("root_dir_path", metavar="ROOT_DIR")
    args = argparser.parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.debug else logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S%z",
    )
    logging.debug("Required free bytes: %d", args.free_bytes)
    disk_usage = shutil.disk_usage(args.root_dir_path)
    logging.debug(disk_usage)
    if disk_usage.free >= args.free_bytes:
        logging.debug("Requirement already fulfilled")
        return
    file_paths = [
        os.path.join(dirpath, filename)
        for dirpath, _, filenames in os.walk(args.root_dir_path)
        for filename in filenames
    ]
    file_mtime_paths = [(os.stat(p).st_mtime, p) for p in file_paths]
    file_mtime_paths.sort()
    removed_files_counter = 0
    last_mtime = None
    for file_mtime, file_path in file_mtime_paths:
        if shutil.disk_usage(args.root_dir_path).free >= args.free_bytes:
            break
        os.remove(file_path)
        logging.debug("Removed file %s", file_path)
        removed_files_counter += 1
        last_mtime = file_mtime
    if removed_files_counter == 0:
        logging.warning("No files to remove")
    else:
        logging.info(
            "Removed %d file(s) with modification date <= %sZ",
            removed_files_counter,
            datetime.datetime.utcfromtimestamp(last_mtime).isoformat("T"),
        )


if __name__ == "__main__":
    main()
