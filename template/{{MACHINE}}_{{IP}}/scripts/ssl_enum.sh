#!/bin/sh

sslyze --certinfo $RHOST:$1 --json_out scans/sslyze_$1.json

cat scans/sslyze_$1.json | jq '.accepted_targets[0].commands_results.certinfo.certificate_chain[0].subject' >> notes.txt


