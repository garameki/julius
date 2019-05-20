#!/bin/bash

iconv -f utf8 -t eucjp meirei.txt | yomi2voca.pl | iconv -f eucjp -t utf8 >> meirei.voca
