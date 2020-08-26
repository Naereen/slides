#!/usr/bin/env bash

sed -i s_'^\\begin{frame}$'_''_ "$@"
sed -i s_'\(^\\tableofcontents\)'_'\\begin{frame}\n\1'_ "$@"
