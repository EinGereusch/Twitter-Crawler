import csv
import logging
import sys
import asyncio

import download_media
from arguments import parser
import twint
import os

args = parser.parse_args()

csv_file_path = f"{args.destination_directory.rstrip(os.sep)}{os.sep}{args.user}{os.sep}data.csv"
if os.path.isfile(csv_file_path):
    logging.info(f"{csv_file_path} already exists; exiting.")
    sys.exit(-1)

destination_directory = f"{args.destination_directory.rstrip(os.sep)}{os.sep}{args.user}"
os.makedirs(destination_directory)

twint_config = twint.Config()
twint_config.Username = args.user
twint_config.Store_csv = True

twint_config.Output = csv_file_path
twint_config.Profile_full = True


async def main():
    with open(csv_file_path) as csv_vile:
        for row in csv.DictReader(csv_vile, delimiter=","):
            photos = eval(row['photos'])
            await download_media.download_photos(photos, destination_directory)
            if row['video'] == "1":
                await download_media.download_video(row['link'], destination_directory)

twint.run.Search(twint_config)
asyncio.get_event_loop().run_until_complete(main())
