#!/usr/bin/env ruby
#This script matched string with h followed by 0 or
# 1 occurence of b then tn

puts ARGV[0].scan(/hb{0,1}tn/).join
