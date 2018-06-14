#------------------------------Information Of Directories------------
s = ./src/
d = ./input/
p = ./docs/

#--------------------------------INPUTS-------------------------------
startYear = 2014
endYear = 2017
baseTemp = 10
#stationId = -st 50089 51442 51459
Namecity = -ct 'Victoria' 'Montreal' 'Toronto'
year = -st 2014 2015 2016 2017


all : report.pdf

$(d)Victoria_2014.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Victoria_2015.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Victoria_2016.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Victoria_2017.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Montreal_2014.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Montreal_2015.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Montreal_2016.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)	
$(d)Montreal_2017.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Toronto_2014.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Toronto_2015.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)
$(d)Toronto_2016.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)	
$(d)Toronto_2017.csv : $(s)downloadData.py 
	python $(s)DownloadData.py $(Namecity) $(year)	
	

	
$(p)Min_Max_Temp_Montreal.png : $(s)MinMaxPlot.py $(d)Montreal_2017.csv
	mkdir -p docs
	python $(s)MinMaxPlot.py $(cityname) $(year)
$(p)Min_Max_Temp_Toronto.png : $(s)MinMaxPlot.py $(d)Toronto_2017.csv
	mkdir -p docs
	python $(s)MinMaxPlot.py $(cityname) $(year)
$(p)Min_Max_Temp_Victoria.png : $(s)MinMaxPlot.py $(d)Victoria_2017.csv
	mkdir -p docs
	python $(s)MinMaxPlot.py $(cityname) $(year)	
	


$(p)task1.png : $(s)task1.py $(s)GDD.py $(s)GDDcalculate$(d)Victoria_2017.csv $(d)Montreal_2017.csv $(d)Toronto_2017.csv$(d)Victoria_2016.csv $(d)Victoria_2015.csv $(d)Victoria_2014.csv$(d)Montreal_2016.csv $(d)Montreal_2015.csv $(d)Montreal_2014.csvToronto$(d)Toronto_2016.csv $(d)Toronto_2015.csv $(d)Toronto_2014.csv
	mkdir -p docs
	python $(s)task1.py $(tempList)
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)
$(p)histogram2014.png : $(s)histograms.py $(s)GDD.py $(s)GDDcalculate $(d)Victoria_2014.csv $(d)Montreal_2014.csv $(d)Toronto_2014.csv
	mkdir -p docs
	python $(s)task1.py 
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)
$(p)histogram2015.png : $(s)histograms.py $(s)GDD.py $(s)GDDcalculate $(d)Victoria_2015.csv $(d)Montreal_2015.csv $(d)Toronto_2015.csv
	mkdir -p docs
	python $(s)task1.py
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)
$(p)histogram2016.png : $(s)histograms.py $(s)GDD.py $(s)GDDcalculate $(d)Victoria_2016.csv $(d)Montreal_2016.csv $(d)Toronto_2016.csv
	mkdir -p docs
	python $(s)task1.py
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)
histogram2017.png : $(s)histograms.py $(s)GDD.py $(s)GDDcalculate $(d)Victoria_2017.csv $(d)Montreal_2017.csv $(d)Toronto_2017.csv
	mkdir -p docs
	python $(s)task1.py	
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)

aprildaily.png : $(s)aprildaily.py $(s)GDD.py $(s)GDDcalculate $(d)Victoria_2017.csv $(d)Montreal_2017.csv $(d)Toronto_2017.csv$(d)Victoria_2016.csv $(d)Victoria_2015.csv $(d)Victoria_2014.csv$(d)Montreal_2016.csv $(d)Montreal_2015.csv $(d)Montreal_2014.csvToronto$(d)Toronto_2016.csv $(d)Toronto_2015.csv $(d)Toronto_2014.csv
	mkdir -p docs
	python $(s)aprildaily.py
    python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)	
	
Montreal_2017.html : $(s)GDD_bokeh.py $(s)GDD.py $(s)GDDcalculate $(d)Montreal_2017.csv 
	mkdir -p docs
	python $(s)GDD_bokeh.py 
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)
$(p)VictoriaGDD.png : $(s)GDD_plot.py  $(s)GDD.py $(s)GDDcalculate $(s)GDD.py $(s)GDDcalculate$(d)Victoria_2017.csv $(d)Victoria_2016.csv $(d)Victoria_2015.csv $(d)Victoria_2014.csv
	mkdir -p docs
	python $(s)GDD_plot.py $(cityname)
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)
$(p)MontrealGDD.png : $(s)GDD_plot.py  $(s)GDD.py $(s)GDDcalculate$(d)Montreal_2017.csv $(d)Montreal_2016.csv $(d)Montreal_2015.csv $(d)Montreal_2014.csv
	mkdir -p docs
	python $(s)GDD_plot.py $(cityname)
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)
$(p)TorontoGDD.png : $(s)GDD_plot.py  $(s)GDD.py $(s)GDDcalculate$(d)Toronto_2017.csv $(d)Toronto_2016.csv $(d)Toronto_2015.csv $(d)Toronto_2014.csv
	mkdir -p docs
	python $(s)GDD_plot.py $(cityname)
	python $(s) GDD.py.py 
	python $(s) GDDcalculate.py $(tempmin)$(tempmax)$(tbase)$(tupper)$(length)

testSuite : $(s)test_gdd.py 
	python $(s)test_gdd.py
	
	
report.pdf : $(r)report.tex  $(p)MontrealGDD.png$(p)TorontoGDD.png $(p)VictoriaGDD.png $(p)minMaxPlotToronto.png $(p)Montreal_2017.html $(p)aprildaily.png $(p)histogram2017.png $(p)histogram2016.png $(p)histogram2015.png  $(p) histogram2014.png  $(p)task1.png  $(p)Min_Max_Temp_Victoria.png$(p)Min_Max_Temp_Toronto.png $(p)Min_Max_Temp_Montreal.png
	pdflatex $(r)report.tex
	pdflatex $(r)report.tex
	rm -f report.log report.aux report.toc report.out
	
clean : 
	rm -rf *.csv $(s)__pycache__ CSVData docs
	rm -f report.log report.aux report.pdf report.toc


help:
	@echo "Please make sure you have installed pdflatex program.
	@echo "# Calling the Makefile"
	@echo "$ make"
	@echo "# Clean the complied and data files"
	@echo "#$ make clean"
	@echo "# Calling by file name"
	@echo "#$ make report.pdf"
