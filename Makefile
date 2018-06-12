#------------------------------Information Of Directories------------
s = ./src/
r = ./reports/
d = ./CSVData/
p = ./plots/

#--------------------------------INPUTS-------------------------------
baseTemp = 10
stationId = -st 50089 51442 51459
cityName = -ct 'St_Johns' 'Vancouver' 'Toronto'

all : report.pdf

$(d)GDDData.csv : $(s)download.py $(s)GDD.py $(s)GDD_plot.py $(s)GDDcalculate.py
	python $(s)download.py $(stationId) $(year)
	python $(s)GDDcalculate.py $(tempmin) $(tempmax) $(tbase)$(tupper) $(length)
	python $(s)GDD.py .py 
	python $(s)GDD_plot.py.py 

	
$(p)minMaxPlot.png : $(s)download.py $(s)MinMaxPlot.py 
	mkdir -p plots
	python $(s)MinMaxPlot.py $(stationId) $(cityName) $(year)
	python $(s)download.py $(stationId) $(year)




	
report.pdf : $(r)report.tex  $(p)GDDPlotIMG.png $(p)minMaxPlot.png 
	pdflatex $(r)report.tex
	pdflatex $(r)report.tex
	rm -f report.log report.aux report.toc report.out
	
clean : 
	rm -rf *.csv $(s)__pycache__ CSVData plots
	rm -f report.log report.aux report.pdf report.toc


help:
	@echo "# Calling the Makefile"
	@echo "$ make"
	@echo "# Clean the complied and data files"
	@echo "#$ make clean"
	@echo "# Calling by file name"
	@echo "#$ make report.pdf"