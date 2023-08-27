import os
import yaml
import logging
import argparse

if __name__=='__main__':
    args=argparse.ArgumentParser()

    args.add_argument('--config',default="default")
    args.add_argument('--datasource',default=None)
    parsed_args=args.parse_args()
    
    print(parsed_args.config,parsed_args.datasource)
