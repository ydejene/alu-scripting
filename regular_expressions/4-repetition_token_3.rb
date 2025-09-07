#!/usr/bin/env ruby

regex = /hbt*n/

ARGV.each do |arg|
  if arg.match?(regex)
    puts arg
  else
    puts ''
  end
end
