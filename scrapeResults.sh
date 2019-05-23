#!/usr/bin/env bash

scrapy crawl cw-all-candidates-ls -t csv -o - > results/cw-all-candidates-ls.csv
scrapy crawl cw-all-candidates -t csv -o - > results/cw-all-candidates.csv
