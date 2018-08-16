# This script takes a directory of yamlfiles and read the content and insert it into mysql database
require "yaml"
require "mysql2"
require "active_record"
load "helper.rb"

ActiveRecord::Base.establish_connection(
  :adapter => "mysql2",
  :host => "localhost",
  :username => "root",
  :password => "nditukulu77",
  :database => "newsapp"
  )

class Article < ActiveRecord::Base
end

# I provide a directory and the output is a list of files from that directory
@directory = "C:/Lecongolais.net/ymlfiles2"
@filenames = []
Dir.foreach(@directory) do |fname|
  next if fname == '.' or fname == '..'
  absolute_file = @directory + "/" + fname
  @filenames << absolute_file
end

# I then proceed with processing one file at a time
# A yaml file produces first a dictionnary, later a list of individual news articles
# The list of articles is iterated and a news item is inserted in the DB at a time
@filenames.each do |filename|
     begin
      @articles = YAML.load(File.read(filename))
      @articles_list = @articles.values
      @articles_list.each do |article|
        article["date_published"] = convert_to_date(article["date_published"])
        Article.create(:title => article["title"], :picture => article["picture"], :original_url => article["original_url"],
                      :lecongolais_url => article["lecongolais_url"], :message => article["message"],
                      :short_message => article["short_message"], :tweet_message => article["tweet_message"],
                      :date_published => article["date_published"], :date_accessed => article["date_accessed"],
                      :categories => article["categories"])
        # my_article.title = article["title"]
        # my_article.picture = article["picture"]
        # my_article.original_url = article ["original_url"]
        # my_article.lecongolais_url = article["lecongolais_url"]
        # my_article.message = article["message"]
        # my_article.short_message = article["short_message"]
        # my_article.tweet_message = article["tweet_message"]
        # my_article.date_published = article["date_published"]
        # my_article.date_accessed = article ["date_accessed"]
        # my_article.categories = article["categories"]
        # my_article.save
       end
     rescue
      puts "there was an error either in reading file or inserting in DB"
     end
end
puts "we have successfully saved the articles into the MySQL"
