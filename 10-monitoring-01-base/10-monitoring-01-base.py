#!/usr/bin/env python
'''
123
'''

import os
import sys
import subprocess
import json
import time
from datetime import datetime


def loadlavg():
    '''Read file: /proc/loadavg
    File /proc/loadavg Content: CPU LA in 1/5/15 min
    Out dict of:
        cpu_treads = amount of CPU treads
        cpu_la1 = CPU LA in 1 min
        cpu_la5 = CPU LA in 5 min
        cpu_la15 = CPU LA in 5 min
    '''
    try:
        loadlavg_dict = {}
        loadlavg_dict['cpu_treads'] = os.cpu_count()
        with open('/proc/loadavg', 'r') as loadavg_file:
            loadavg_line = loadavg_file.readline()
            loadavg_list = loadavg_line.split(' ')[:3]
            loadlavg_dict['cpu_la1'] = loadavg_list[0]
            loadlavg_dict['cpu_la5'] = loadavg_list[1]
            loadlavg_dict['cpu_la15'] = loadavg_list[2]
            return(loadlavg_dict)
    except IOError as e:
        print('ERROR: %s' % e)
        sys.exit(1)


def meminfo():
    '''Read file: /proc/meminfo
    File /proc/meminfo
    Out contents file /proc/meminfo as a dict
    '''
    try:
        file_path = '/proc/meminfo'
        meminfo_dict = {}
        with open(file_path, 'r') as meminfo_file:
            for meminfo_line in meminfo_file:
                meminfo_list = meminfo_line.split()[:2]
                meminfo_dict[meminfo_list[0]] = meminfo_list[1]
            return(meminfo_dict)
    except IOError as e:
        print('ERROR: %s' % e)
        sys.exit(1)


def diskstats():
    '''Get info for disk using /proc/diskstats
    '''
    columns_disk = ['rd_comp', # of reads completed
                    'rd_mrg', # of reads merged, field 6 -- # of writes merged
                    'rd_sector', # of sectors read
                    'ms_reading', # of milliseconds spent reading
                    'wr_comp', # of writes completed
                    'wr_mrg', # of writes merged
                    'wr_sector', # of sectors written
                    'ms_writting', # of milliseconds spent writing
                    'cur_ios', # of I/Os currently in progress
                    'ms_doing_io', # of milliseconds spent doing I/Os
                    'ms_weighted', # weighted of milliseconds spent doing I/Os
                    'disc_comp', # of discards completed
                    'disc_merg', # of discards merged
                    'disc_sect', # of sectors discarded
                    'ms_disc'] # of milliseconds spent discarding


    columns_part = ['rd_issued', # of reads issued
                    'rd_sector', # of sectors read
                    'wr_issued', # of writes issued
                    'wr_sector'] # of sectors written

    try:
        len_columns_disk = len(columns_disk)
        len_columns_part = len(columns_part)
        file_path = '/proc/diskstats'
        diskstats_dict = {}
        with open(file_path, 'r') as diskstats_file:
            for diskstats_line in diskstats_file:
                lines_dict = {}
                diskstats_name = diskstats_line.split()[2]
                diskstats_line = diskstats_line.split()[3:]
                if len(diskstats_line) == len_columns_disk:
                    for metric_name, metric_value in zip(columns_disk, diskstats_line):
                        lines_dict[metric_name] = metric_value
                elif len(diskstats_line) == len_columns_part:
                    for metric_name, metric_value in zip(columns_part, diskstats_line):
                        lines_dict[metric_name] = metric_value

                df_output = subprocess.run(
                    ["df", "-i", f"/dev/{diskstats_name}"], #
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=True)
                df_date = df_output.stdout.decode().split()[8:]
                lines_dict["Inodes"] = df_date[0]
                lines_dict["IUsed"] = df_date[1]
                lines_dict["IFree"] = df_date[2]
                lines_dict["IUsed%"] = df_date[3]

                diskstats_dict[diskstats_name] = lines_dict
            return(diskstats_dict)
    except IOError as e:
        print('ERROR: %s' % e)
        sys.exit(1)


def netdev():
    '''Get info for disk using /proc/net/dev
    '''
    columns_net = ['rv_bytes',
                   'rv_packets',
                   'rv_errs',
                   'rv_drop',
                   'rv_fifo',
                   'rv_frame',
                   'rv_comp',
                   'rv_mult',
                   'tran_bytes',
                   'tran_packets',
                   'tran_errs',
                   'tran_drop',
                   'tran_fifo',
                   'tran_colls',
                   'rv_carr',
                   'rv_comp']

    try:
        file_path = '/proc/net/dev'
        netdev_dict = {}
        with open(file_path, 'r') as netdev_file:
            lines = netdev_file.readlines()[2:]
            for netdev_line in lines:
                lines_dict = {}
                line_list = netdev_line.split()
                interface = line_list[0]
                interface_data = line_list[1:]
                for metric_name, metric_value in zip(columns_net, interface_data):
                    lines_dict[metric_name] = metric_value
                netdev_dict[interface] = lines_dict
            return(netdev_dict)
    except IOError as e:
        print('ERROR: %s' % e)
        sys.exit(1)


def main():
    result_dict = {}
    date_of_file = datetime.today().strftime('%y-%m-%d')
    print(date_of_file)
    file_name = f'/var/log/{date_of_file}-awesome-monitoring.log'

    result_dict['timestamp'] = int(time.time())
    result_dict['loadlavg'] = loadlavg()
    result_dict['meminfo'] = meminfo()
    result_dict['diskstats'] = diskstats()
    result_dict['netdev'] = netdev()

    try:
        with open(file_name, 'ab') as output_file:
            output_file.write(json.dumps(result_dict, indent=2).encode("utf-8"))
    except:
        print(f'ERROR: {e}')
        sys.exit(1)

    return result_dict



if __name__ == '__main__':
    main()
