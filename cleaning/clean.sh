### "fetch"
wget -O https://dl.dropboxusercontent.com/u/18070942/crimes.csv

### "check-file"
head -5 crimes.csv

### "check-end-file"
tail -5 crimes.csv

### "size-file"
du -h crimes.csv

### "slice-file"
sed -n '/01\/01\/2010/,$p' > crimes_since_2010.csv && du -h crimes_since_2010.csv

### "remove-unneeded-geolocation-1"
head -1 crimes_since_2010.cv | sed 's/[^,]//g' | wc -c
### "remove-unneeded-geolocation-2"
cut -d, -f1-21 crimes_since_2010.csv > crimes_final.csv
### "remove-unneeded-geolocation-3"
du -h crimes_final.csv

### "open-ipython"
conda run -- ipython
