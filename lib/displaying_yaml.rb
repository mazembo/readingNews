require "yaml"

puts "write the file name in the format 2018-01-31.yml"
filename = gets.chomp
yaml_folder = "/mnt/volume_dielais/readingNews/assets/content_yaml_files/"
image_folder = "/mnt/volume_dielais/readingNews/assets/images/"
full_filename= yaml_folder + filename
@articles = YAML.load(File.read(full_filename, :encoding => 'utf-8'))
@size = @articles.length
#@articles = YAML.load(File.read("2017-07-19.yml"))
# @articles2 = YAML.load(File.read("2017-02-02-1.yml"))
#
# puts "the first list has #{@articles1.length} elements"
# puts "the second list has #{@articles2.length} elements"
#
# puts @articles1.class
#
# @articles = @articles1 - @articles2 // not possible as these elements are hashes. Operation only exist on arrays
# puts "the third list (substraction) is made of #{@articles.length} elements"

@articles.each do |article|
   puts article[0]
   puts article[1]["title"]
   puts article[1]["tweet_message"]
   puts article[1]["original_url"]
   puts article[1]["picture"]
   puts "\n"
 end
 puts @articles.length
