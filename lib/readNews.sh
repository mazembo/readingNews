#!/bin/bash
python /mnt/volume_dielais/readingNews/lib/extract_links.py
sleep 60 
python /mnt/volume_dielais/readingNews/lib/reading8.py
sleep 60
/usr/local/rvm/rubies/ruby-2.6.0/bin/ruby /mnt/volume_dielais/readingNews/lib/tweeting.rb
sleep 60
python /mnt/volume_dielais/readingNews/lib/reading10.py rdc
sleep 60
/usr/local/rvm/rubies/ruby-2.6.0/bin/ruby /mnt/volume_dielais/readingNews/lib/tweetingd.rb


