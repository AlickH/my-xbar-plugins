#!/bin/bash
curl -s -o /dev/null -X POST -H "Content-Type:application/json" -H "X-Key: examplekey" -d "{\"group_name\": \"$1\", \"policy\": \"$2\"}" "http://127.0.0.1:6166/v1/policy_groups/select"