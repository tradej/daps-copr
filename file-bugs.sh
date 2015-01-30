#!/usr/bin/bash

STORAGE="https://tradej.fedorapeople.org/reviews/daps"

for shortname in $(cat specs.list); do
dap="devassistant-dap-${shortname}"
srpm="$(basename rpms/${dap}-*)"

summary="$(rpm -qp --qf '%{summary}' rpms/${srpm})"
description="$(rpm -qp --qf '%{description}' rpms/${srpm})"
title="Review Request: ${dap} - ${summary}"
product="Fedora"
component="Package Review"
blocks="1186748"
version="rawhide"
base_url="${STORAGE}/${dap}/0"
spec_url="${base_url}/${dap}.spec"
srpm_url="${base_url}/${srpm}"
comment="Spec URL: ${spec_url}
SRPM URL: ${srpm_url}
Description: ${description}

Fedora Account System Username: tradej"

bugzilla new --product="${product}" --version="${version}" \
    --component="${component}" --summary="${title}" --comment="${comment}" --blocked="${blocks}"
sleep 2
done
