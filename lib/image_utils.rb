module ImageUtils

   def preview(image)
     puts image
   end
   def transfer(image)
     puts image.reverse
   end

end
class Article
  include ImageUtils
end
# article = Article.new
# article.preview("mazembo")
