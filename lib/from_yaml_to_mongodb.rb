<<<<<<< HEAD
# This script takes a directory of yamlfiles and read the content and insert it into mongodb
require "yaml"

directory_path = gets ("provide full directory path")
@filenames = []
Dir.foreach(directory_path) do |fname|
  next if fname == '.' or fname == '..'
  @filenames << fname
end
=======
# This script takes a directory of yamlfiles and read the content and insert it into mongodb
require "yaml"

directory_path = gets ("provide full directory path")
@filenames = []
Dir.foreach(directory_path) do |fname|
  next if fname == '.' or fname == '..'
  @filenames << fname
end
>>>>>>> sinatra stuff and docker scripts
