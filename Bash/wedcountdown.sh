#!/bin/bash
days="$(($(date -d 17-Dec +%j) - $(date +%j)))"
echo "$days days to go"

