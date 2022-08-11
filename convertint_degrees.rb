print "Degrees(after teh number write c or f): "
degrees = gets.split

#converting to fahrenheit
if degrees[1] == "c"
  puts "#{(degrees[0].to_i * 9 / 5) + 32}°F"
end

#converting to celsius
if degrees[1] == "f"
  puts "#{(degrees[0].to_i - 32) * 5 / 9}°C"
end
