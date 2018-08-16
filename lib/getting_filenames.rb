@filenames = []
Dir.foreach('/home/mavungu/Lecongolais.net/facebook/images/2016-08-03a') do |fname|
  next if fname == '.' or fname == '..'
  @filenames << fname
end
puts @filenames
puts "The folder has #{@filenames.length} files "
