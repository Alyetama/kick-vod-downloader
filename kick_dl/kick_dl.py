#!/usr/bin/env python
# coding: utf-8

import argparse
import json
from pathlib import Path

import cloudscraper
from yt_dlp import YoutubeDL


def get_data_file(channel_name):
    data_file = f'{channel_name}_data.json'

    if not Path(data_file).exists():
        scraper = cloudscraper.create_scraper()
        data_url = f'https://kick.com/api/v1/channels/{channel_name}'
        r = scraper.get(data_url)
        data = json.loads(r.text)
        with open(data_file, 'w') as j:
            json.dump(data, j, indent=4)
    else:
        with open(data_file) as j:
            data = json.load(j)
    return data


def list_all_vods(data):
    for n, x in enumerate(data['previous_livestreams']):
        print(f'index: {n} |', x['session_title'], f'({x["created_at"]})')


def parse_download_url(data: dict, stream_idx: int):
    stream = data['previous_livestreams'][stream_idx]
    stream_slug = stream['slug']

    url = 'https://stream.kick.com/ivs/v1/'
    url += data['playback_url'].split('channel')[0].split('.')[-2] + '/'

    url += stream['thumbnail']['src'].split('/')[4] + '/'

    ts = stream['created_at'].replace('-', '/').split(' ')
    date = ts[0] + '/'
    time = ts[1].replace(':', '/')[:-2]
    time = '/'.join([str(int(x)) for x in ts[1].split(':')[:-1]]) + '/'
    url += date + time

    url += stream['thumbnail']['src'].split('/')[5]
    url += '/media/hls/master.m3u8'

    return url, stream_slug


def download_vod(vod_url, file_name, quality=None, n_concurrent_downloads=1):
    options = {
        'noplaylist': True,
        'concurrent_fragment_downloads': n_concurrent_downloads,
        'outtmpl': file_name,
    }
    if quality:
        options['format'] = quality

    with YoutubeDL(options) as ydl:
        ydl.download([vod_url])


def opts() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download Kick VoDs from a specified channel.")
    parser.add_argument('-c',
                        '--channel_name',
                        help='The name of the channel to fetch VoDs from.',
                        type=str,
                        required=True)
    parser.add_argument(
        '-i',
        '--vod_index',
        help=
        ('The index or list of indexes of the VoD(s) to download. '
         'Use 0 for the most recent VoD, 1 for the second most recent, and so on. '
         'Provide a single index or a comma-separated list of integers.'),
        type=lambda s: [int(item) for item in s.split(',')])
    parser.add_argument(
        '-l',
        '--list_indexes',
        action='store_true',
        help=
        'List all available VoDs with their titles and dates for easy selection.'
    )
    parser.add_argument(
        '-a',
        '--download_all',
        action='store_true',
        help='Download all available VoDs without selecting specific indexes.')
    parser.add_argument(
        '-nd',
        '--no_download',
        action='store_true',
        help='Do not download the VoD. Instead, output the VoD download URL(s).'
    )
    parser.add_argument(
        '-q',
        '--quality',
        help=
        ('Specify the desired quality of the VoD. Defaults to the highest quality '
         'available. Common options include 160p, 360p, 480p, 720p60, and 1080p60.'
         ),
        type=str)
    parser.add_argument(
        '-C',
        '--n_concurrent_downloads',
        help='Set the number of concurrent downloads. Defaults to 1.',
        type=int,
        default=1)
    return parser.parse_args()


def main():
    args = opts()
    data = get_data_file(args.channel_name)

    if args.list_indexes:
        list_all_vods(data)
        return

    if args.download_all:
        indexes_to_download = list(range(0, len(data['previous_livestreams'])))
    else:
        indexes_to_download = [int(x) for x in args.vod_index]

    for idx in indexes_to_download:
        d_url, stream_slug = parse_download_url(data, int(idx))
        print(d_url)
        print(stream_slug)

        if args.no_download:
            continue

        download_vod(vod_url=d_url,
                     file_name=stream_slug + '.mp4',
                     quality=args.quality,
                     n_concurrent_downloads=args.n_concurrent_downloads)


if __name__ == '__main__':
    main()
