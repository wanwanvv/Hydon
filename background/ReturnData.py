'''
Descripttion: 
version: 
Author: Wan Jingyi
Date: 2021-08-26 16:39:10
LastEditors: Wan Jingyi
LastEditTime: 2021-08-26 20:20:17
'''
import os
import json
import psutil
import time

cpu_fields=["cpu_time","cpu_percent"]
cpu_time_fields=["user","nice","system","idle","iowait","irq","softirq","steal","guest"]
memory_basic_fields=["total","available","percent","used","free","active","inactive","buffers","cached","shared","slab"]
memory_appendix_fields=["active","inactive","active_anon","inactive_anon","active_file","inactive_file"]
disk_fields=["disk_usage","disk_io"]
disk_usage_fields=["total","used","free","percent"]
disk_io_fields=["read_count","write_count","read_bytes","write_bytes","read_time","write_time","read_merged_count","write_merged_count","busy_time"]
net_fields=["bytes_sent","bytes_recv","packets_sent","packets_recv","errin","errout","dropin","dropout"]

json_template={
    "cpu_data":{
        "cpu_time":{
            "user":24194.81,
            "nice":206.0,
            "system":4100.11,
            "idle":9141941.8,
            "iowait":531.48,
            "irq":439.35,
            "softirq":456.76,
            "steal":0.0,
            "guest":0.0
        },
        "cpu_percent":[0.0,0.0,0.1,0.1,0.1,0.0,0.1,0.1]
    },

    "memory_data":{
        "basic_info":{
            "total":7135100928,
            "available":26055413760,
            "percent":52.7,
            "used":6236758016,
            "free":22440312832,
            "active":7554965504,
            "inactive":2196578304,
            "buffers":577658880,
            "cached":3858157568,
            "shared":348487680,
            "slab":655302656
        },
        "appendix_info":{
            "active":7341656,
            "inactive":2157704,
            "active_anon":5576252,
            "inactive_anon":330128,
            "active_file":1765404,
            "inactive_file":1827576
        }
    },

    "disk_data":{
        "disk_usage":{
            "total":104412327936,
            "used":20087566336,
            "free":84324761600,
            "percent":19.2
        },
        "disk_io":{
            "read_count":239318,
            "write_count":1173702,
            "read_bytes":14496033280,
            "write_bytes":55531739648,
            "read_time":1025964,
            "write_time":83116518,
            "read_merged_count":1288,
            "write_merged_count":466996,
            "busy_time":4361130
        }
    },

    "net_data":{
        "bytes_sent":1166094394,
        "bytes_recv":5130755104,
        "packets_sent":2188507,
        "packets_recv":4795914,
        "errin":0,
        "errout":0,
        "dropin":0,
        "dropout":0
    }
}

def read_and_return_monitor_data():
    print("Read data and return!")

#directly return
def return_monitor_data():
    return json_template

#dynamicly return
def return_monitor_data_dynamic_one():
    cpu_times = psutil.cpu_times()
    cpu_counts = psutil.cpu_count()
    cpu_percent_list = psutil.cpu_percent(0.6, 1)
    mem = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    disk_io = psutil.disk_io_counters()
    net_io = psutil.net_io_counters()
    json_template_new=json_template
    for i,item in enumerate(cpu_time_fields):
        json_template_new["cpu_data"][cpu_fields[0]][item]=cpu_times[i]
    cpu_percent_tmp=[]
    for i, item in enumerate(cpu_percent_list):
        cpu_percent_tmp.append(item)
    json_template_new["cpu_data"][cpu_fields[1]]=cpu_percent_tmp

    for i,item in enumerate(mem):
        json_template_new["memory_data"]["basic_info"][memory_basic_fields[i]]=item
    with open('/proc/meminfo') as f:
        lines=f.readlines()[6:12]
        for line_idx,line in enumerate(lines):
            line=line.rstrip('\n')
            items=line.split(":")
            val=int(items[1].lstrip().split(' ')[0])*1024
            json_template_new["memory_data"]["appendix_info"][memory_appendix_fields[line_idx]]=val

    for i,item in enumerate(disk_usage_fields):
        json_template_new["disk_data"]["disk_usage"][item]=disk_usage[i]
    for i,item in enumerate(disk_io_fields):
        json_template_new["disk_data"]["disk_io"][item]=disk_io[i]
    for i,item in enumerate(net_fields):
        json_template_new["net_data"][item]=net_io[i]
    return json_template_new

def return_monitor_data_dynamic(n):
    return_json=[]
    interval=(1.0-0.05*float(n))/float(n)
    for i in range(n):
        cpu_times = psutil.cpu_times()
        cpu_counts = psutil.cpu_count()
        cpu_percent_list = psutil.cpu_percent(interval, 1)
        mem = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        disk_io = psutil.disk_io_counters()
        net_io = psutil.net_io_counters()
        json_template_new={
            "cpu_data":{
                "cpu_time":{
                    "user":24194.81,
                    "nice":206.0,
                    "system":4100.11,
                    "idle":9141941.8,
                    "iowait":531.48,
                    "irq":439.35,
                    "softirq":456.76,
                    "steal":0.0,
                    "guest":0.0
                },
                "cpu_percent":[0.0,0.0,0.1,0.1,0.1,0.0,0.1,0.1]
            },

            "memory_data":{
                "basic_info":{
                    "total":7135100928,
                    "available":26055413760,
                    "percent":52.7,
                    "used":6236758016,
                    "free":22440312832,
                    "active":7554965504,
                    "inactive":2196578304,
                    "buffers":577658880,
                    "cached":3858157568,
                    "shared":348487680,
                    "slab":655302656
                },
                "appendix_info":{
                    "active":7341656,
                    "inactive":2157704,
                    "active_anon":5576252,
                    "inactive_anon":330128,
                    "active_file":1765404,
                    "inactive_file":1827576
                }
            },

            "disk_data":{
                "disk_usage":{
                    "total":104412327936,
                    "used":20087566336,
                    "free":84324761600,
                    "percent":19.2
                },
                "disk_io":{
                    "read_count":239318,
                    "write_count":1173702,
                    "read_bytes":14496033280,
                    "write_bytes":55531739648,
                    "read_time":1025964,
                    "write_time":83116518,
                    "read_merged_count":1288,
                    "write_merged_count":466996,
                    "busy_time":4361130
                }
            },

            "net_data":{
                "bytes_sent":1166094394,
                "bytes_recv":5130755104,
                "packets_sent":2188507,
                "packets_recv":4795914,
                "errin":0,
                "errout":0,
                "dropin":0,
                "dropout":0
            }
        }

        for i,item in enumerate(cpu_time_fields):
            json_template_new["cpu_data"][cpu_fields[0]][item]=cpu_times[i]
        cpu_percent_tmp=[]
        for i, item in enumerate(cpu_percent_list):
            cpu_percent_tmp.append(item)
        json_template_new["cpu_data"][cpu_fields[1]]=cpu_percent_tmp
        for i,item in enumerate(mem):
            json_template_new["memory_data"]["basic_info"][memory_basic_fields[i]]=item
        with open('/proc/meminfo') as f:
            lines=f.readlines()[6:12]
            for line_idx,line in enumerate(lines):
                line=line.rstrip('\n')
                items=line.split(":")
                val=int(items[1].lstrip().split(' ')[0])*1024
                json_template_new["memory_data"]["appendix_info"][memory_appendix_fields[line_idx]]=val

        for i,item in enumerate(disk_usage_fields):
            json_template_new["disk_data"]["disk_usage"][item]=disk_usage[i]
        for i,item in enumerate(disk_io_fields):
            json_template_new["disk_data"]["disk_io"][item]=disk_io[i]
        for i,item in enumerate(net_fields):
            json_template_new["net_data"][item]=net_io[i]
        #print("json_template:")
        #print(json_template)
        #print("json_template_new:")
        #print(json_template_new)
        return_json.append(json_template_new)
        #time.sleep(interval)
    return return_json
