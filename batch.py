#!/usr/bin/env python
# This script is used for convert pickle to instruction json

# 处理一组数据
from ast import List, Tuple
import os
import pickle
from typing import Any

from utils.chain import dynamic_chain_exec_one_sample


def _func(sample, proc_sample, log, dynamic_chain_log_list, final_result, index):
  pass

def load_pickle(pickle_file) -> Any:
  pickle_data = open(pickle_file, 'rb')
  return pickle.load(pickle_data)

def load_data(dir_path:str):
  cases = []
  # load index from 0 to 1042
  for i in range(1043):
    case_i = load_pickle(os.path.join(dir_path, 'cache', f'case-{i}.pkl'))
    cases.append(case_i)

  # load dynamic chain log
  dynamic_chain_log_list = load_pickle(os.path.join(dir_path, 'dynamic_chain_log_list.pkl'))

  # load final_result
  final_result = load_pickle(os.path.join(dir_path, 'final_result.pkl'))

  return cases, dynamic_chain_log_list, final_result

def main():
  dir_path = './results/tabfact'
  cases, dynamic_chain_log_list, final_result = load_data(dir_path)
  for i, case in enumerate(cases):
    _func(**case, dynamic_chain_log_list=dynamic_chain_log_list, final_result=final_result, index=i)

if __name__ == '__main__':
  main()
