# >>> ExamKill: ExamBrowser killer
# ... Author            : P4kL0nc4t [(https://github.com/p4kl0nc4t) / (p4kl0nc4t@loncatbyte.space)]
# ... Date              : 19/3/2018
# ... Description       : Monitor for ExamBrowser and kill it after few seconds to bypass restrictions that was created
# ... Expectation       : ExamKiller expects that the created child process (Chrome browser) remains even its parent killed
# ... Used software     : Google Chrome (64.0.3282.186), ExamBrowser (17.0428)
# ... Disclaimer        : This script is intended only for educational purposes

import sys
import subprocess
import time
import thread

class conf:
        prog_name = "ExamKill"
        pn_chrome = "chrome.exe" # process name for Chrome browser (child process opened by exambrowser)
        pn_exambrowser = "exambrowser.exe" # process name for ExamBrowser
        pn_list = [ pn_chrome, pn_exambrowser ]
        delay = 10 # time to wait after both Chrome and ExamBrowser appeared
        expected_condition = { pn_chrome: True, pn_exambrowser: True }
        log_filename = "log.txt"
class stats:
        processes_running = {
                conf.pn_chrome: False,
                conf.pn_exambrowser: False,
                }
        reached_expected_condition = False
        last_condition = None

def custom_print(string):
        if getattr(sys, 'frozen', False):
                logfile = open(conf.log_filename, 'a')
                logfile.write(string + "\n")
                logfile.close()
        else:
                print(string)

def timestamp():
        ctime = time.strftime("%d/%m/%Y %H:%M:%S")
        return ctime

def remove_trailing_spaces(string):
        while "  " in string:
                string = string.replace("  ", " ")
        return string

def _is_running(proc_name):
        return_val = False
        proc_list = subprocess.Popen("tasklist", shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().lower()
        proc_list = proc_list.split("\n")
        for proc_entry in proc_list:
                if proc_name in proc_entry:
                        proc_detail = remove_trailing_spaces(proc_entry).split(" ")
                        if type(return_val) == type(list()):
                                return_val[1] = return_val[1] + "," + proc_detail[1]
                        else:
                                return_val = [proc_detail[0], proc_detail[1]]
        return return_val

def kill_proc(name):
        _kill = subprocess.Popen("taskkill /F /IM " + str(name), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read().lower()
        if "success" in _kill:
                return True
        else:
                return False

def _monitor_proc(proc_name):
        if proc_name not in conf.pn_list: return False
        while True:
                proc_check = _is_running(proc_name)
                if proc_check:
                        stats.processes_running[proc_name] = True
                        # thread.exit()
                else:
                        stats.processes_running[proc_name] = False
def start_countdown(timex):
        elapsed = 0
        time_out = timex
        while time_out > elapsed:
                custom_print(timestamp() + ": killing {} in {} seconds . . .".format(conf.pn_exambrowser, timex))
                time.sleep(1)
                elapsed += 1
                timex -= 1
                      
def main_routine():
        custom_print("""\
{-----------------------------------------------------}
| ExamKill: Monitor and kill ExamBrowser to bypass    |
|           its restrictions                          |
| - Author: P4kL0nc4t (https://github.com/p4kl0nc4t)  |
| - Date: 19/03/2018                                  |
{-----------------------------------------------------}
""")
        custom_print(timestamp() + ": started " + conf.prog_name + " process monitor")
        thread.start_new_thread(_monitor_proc,( conf.pn_chrome, ))
        thread.start_new_thread(_monitor_proc,( conf.pn_exambrowser, ))
        time.sleep(1)
        while True:
                custom_print(timestamp() + ": current condition is [{}]".format(stats.processes_running))
                custom_print(timestamp() + ": expected condition is [{}]".format(conf.expected_condition))
                custom_print(timestamp() + ": waiting to reach expected condition . . .")
                while stats.processes_running != conf.expected_condition:
                        pass
                custom_print(timestamp() + ": reached expected condition, countdown started")
                start_countdown(conf.delay)
                custom_print(timestamp() + ": killing {} . . .".format(conf.pn_exambrowser))
                work_done = False
                while work_done == False:
                        if(kill_proc(conf.pn_exambrowser)):
                                work_done = True
                custom_print(timestamp() + ": process {} successfully killed".format(conf.pn_exambrowser))
                stats.reached_expected_condition = True
                time.sleep(1)
                while stats.reached_expected_condition == True:
                        if _is_running(conf.pn_chrome) and _is_running(conf.pn_exambrowser):
                                custom_print(timestamp() + ": expected condition reached again! starting over . . .")
                                break
                        else:
                                pass
                
if __name__ == "__main__":
        try:
                main_routine()
        except KeyboardInterrupt:
                custom_print("\r" + timestamp() + ": KeyboardInterrupt detected! Exiting . . .")
                thread.exit()
                sys.exit()
        except Exception as e:
                custom_print(timestamp() + ": exception -> {}".format(str(e)))
